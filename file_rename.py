import os

file_source = input("Pls provide a file path to be renamed:\n")
file_destination = input("New file name\n")

new_file_path = os.path.dirname(file_source) + "/" + file_destination

if (os.path.exists(file_source)):
    os.rename(file_source, new_file_path)
else:
    print("error")
