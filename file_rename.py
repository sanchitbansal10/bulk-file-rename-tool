import os

def change_individual_files(file_source, new_file_name):
    new_file_path = os.path.dirname(file_source) + "/" + new_file_name
    print(file_source,new_file_path)
    os.rename(file_source, new_file_path)
    return "done"

def get_file_names_with_counter(file_name, index):
    split = file_name.split(".")
    return split[0] + str(index) + "." + split[1]

def change_folder_file_names(folder_path, new_file_name):
    files_in_dir = os.listdir(folder_path)
    for index in range(len(files_in_dir)):
        full_path = os.path.join(folder_path, files_in_dir[index])
        if(full_path):
            change_individual_files(full_path, get_file_names_with_counter(new_file_name, index))
        else:
            print("is not a file {}".format(files_in_dir[index]))
    return "all renamed"

file_source = input("Pls provide a file/folder path to be renamed:\n")

if (not os.path.exists(file_source)):
    raise Exception('File {} does not exist'.format(file_source))

new_file_name = input("New file name\n")

if (os.path.isdir(file_source)):
    change_folder_file_names(file_source, new_file_name)
else:
    change_individual_files(file_source, new_file_name)
    

