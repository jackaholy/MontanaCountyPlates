"""
Do Something cool
"""

import sys

# Dictionary to store county data
county_data = {}


def read_file(file):
    try:
        with open(file, 'r') as file:
            for line in file:
                # Split the line by the comma
                info = line.strip().split(',')
                county_name = info[0]
                county_seat = info[1]
                county_number = info[2]
                # Store the county information in the dictionary
                county_data[county_number] = (county_seat, county_name)

    except FileNotFoundError:
        print(f"Error: The file '{file}' cannot be found.")
    except IOError:
        print(f"Error: Unable to read the file '{file}'.")

    return True


def choose_county_number():
    while True:
        chosen_number = input("Please enter a Montana county number (enter 'quit' to exit): ")
        if chosen_number in county_data:
            county_info = county_data[chosen_number]
            print(f"County Number: {chosen_number}\n"
                  f"County Name: {county_info[1]}\n"
                  f"County Seat: {county_info[0]}")
        elif chosen_number.lower() == "quit":
            sys.exit(0)
        elif chosen_number not in county_data:
            print("Invalid county number.")
        else:
            print("Invalid input.")


def main():
    read_file("MontanaCounties.csv")
    choose_county_number()


if __name__ == "__main__":
    main()
