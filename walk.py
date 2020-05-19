
import os

#search for files ending with given extension
starting_directory = input("Enter starting directory: ")
extension = input("Search for files ending with: ")

for root, dirs, files in os.walk(starting_directory):
    for file in files:
        if file.endswith(extension):
            print(os.path.join(root,file))
