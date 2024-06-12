#!/usr/bin/env python3
# file_handling_assignment.py

def create_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line.\n")
            file.write("Here is the number 123.\n")
            file.write("Last line of the initial content.\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
        print("File content read successfully. Here it is:")
        print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line.\n")
            file.write("Adding the number 456.\n")
            file.write("This is the last appended line.\n")
        print("Content appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_file()
    read_file()

if __name__ == "__main__":
    main()
