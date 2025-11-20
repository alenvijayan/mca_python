# Write a program that retrieves all lines from a file having words starting with 's' and ending with 'e'

import re

filename = input("Enter filename: ")

pattern = r"\bs\w*e\b"   

with open(filename, "r") as f:
    for line in f:
        if re.search(pattern, line, re.IGNORECASE):
            print(line.strip())

