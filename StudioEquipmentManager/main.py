
from studio.storage import load_data
from studio.menu import run_menu


def main():
    data = load_data()
    run_menu(data)


if __name__ == "__main__":
    main()
