"""Read/write studio records using only Python's standard library."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "studio_data.json"


def save_data(data):
    """Save safely: replace the old file only after JSON is written."""
    temporary = DATA_FILE.with_suffix('.tmp')
    with temporary.open('w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    temporary.replace(DATA_FILE)


def load_data():
    """Create an empty file on first use, otherwise retain saved records."""
    if not DATA_FILE.exists():
        data = {'equipment': [], 'transactions': []}
        save_data(data)
        return data
    with DATA_FILE.open('r', encoding='utf-8') as file:
        data = json.load(file)
    if not isinstance(data, dict) or not isinstance(data.get('equipment'), list) or not isinstance(data.get('transactions'), list):
        raise ValueError('Invalid JSON data format. Existing file was not changed.')
    return data
