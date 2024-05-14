#!/usr/bin/env python3

# Program accepts a filename from the user and prints the extension of the file

filename = input("Enter the filename: ")

# Split the filename by "." and get the last element of the list
file_extension = filename.split(".")[-1]
print(f"The extension of the file is: {"." + file_extension}")
