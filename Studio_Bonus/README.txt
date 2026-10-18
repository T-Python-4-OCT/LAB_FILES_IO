STUDIO EQUIPMENT MANAGER - BONUS

Run ONLY main_studio.py:
  python main_studio.py

File structure:
  main_studio.py       => displays menu and runs the program
  studio/__init__.py   => marks studio as a Python package
  studio/operations.py => CRUD + borrow/return/history functions
  studio/storage.py    => JSON loading/saving functions

The program automatically creates studio_data.json next to main_studio.py.
All valid changes are saved immediately. Restarting the program loads existing data.
No external libraries are needed.
