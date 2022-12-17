#!/usr/bin/python3

import sys
import os

"""
Rayyaw's line-counting utility
Run with python lineCounter.py [path] [file extensions]
Example: python lineCounter.py . .py .c .rb

In this example, the utility will print the total number of newlines (\n) 
for all .py, .c, .rb files in . or any of its subdirectories. 

Note that path must be a folder, and at least one file extension must be specified.
"""

# Counts the number of lines as above.
# Assumes that the folder path is valid.
# Throws a FileNotFoundError if the folder path is invalid.

# folder is a string containing the folder path.
# extensions is an iterable containing all the file extensions to keep.

# Returns and prints the number of lines.
def countLines(folder, extensions):
    entries = os.listdir(folder)

    lineTotal = 0

    for entry in entries:
        # Get a full path for the entry
        entry_full = folder + "/" + entry

        # If a directory, recursively search it
        if os.path.isdir(entry_full) and entry[0] != '.':
            lineTotal += countLines(entry_full, extensions)

        # If it's any of the file extensions we're using, get the number of lines and add to total
        elif any([entry.endswith(i) for i in extensions]):
            f = open(entry_full, "r")
            f_lines = len(f.readlines())
            print("Number of lines in", entry_full, ":", f_lines)
            lineTotal += f_lines
            f.close()

    print("Total number of lines in", folder, ":", lineTotal)
    return lineTotal

if __name__ == "__main__":
    argv = sys.argv

    # Incorrect number of arguments were passed.
    if len(argv) < 3:
        print("Incorrect syntax, please try again.")
        print("python lineCounter.py [path] [extension1] <extension2> ...")
        sys.exit()

    # The folder passed was invalid.
    if not os.path.isdir(argv[1]):
        print("Invalid filepath specified, please try again.")
        sys.exit()

    # All arguments were valid, proceed to count lines.
    countLines(argv[1], argv[2:])
