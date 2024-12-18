import argparse
import re

def get_filename() -> str:
    """
    Parses the file name from the command line arguments.

    :return: The file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    return parser.parse_args().filename


def read_file(filename: str) -> str:
    """
    Reads the contents of the file.

    :param filename: The file name
    :return: The file contents
    """
    if filename is not None:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    else:
        raise FileNotFoundError("File not found")


def find_dates(text: str) -> list:
    """
    Finds the dates corresponding to the 21st century.

    :param text: The string to search
    :return: The list of dates corresponding to the 21st century
    """
    pattern = r"\d\d\.\d\d.20\d\d"
    return re.findall(pattern, text)


def print_quantity(dates_list: list):
    """
    Prints the quantity of people born in the 21st century

    :param dates_list: The list of dates corresponding to the 21st century
    """
    print("The number of people born in the 21st century =",
          len(dates_list))


def main():
    try:
        filename = get_filename()
        text = read_file(filename)
        dates_list = find_dates(text)
        print_quantity(dates_list)
    except FileNotFoundError as exc:
        print("Error: ", exc)
    except Exception as exc:
        print("Error: ", exc)


if __name__ == "__main__":
    main()
