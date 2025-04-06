## list all files in the list of directories that user provided

import os
## read the input from user and print directory/folder name with type
folders = input("Please provides list of folders name and spaces in between:").split()
# print(folders)
# print(type(folders))


for folder in folders:

    try:
        list_of_files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, Looks like the folder does not exist:", folder)
        continue ## break -- if you want quite the pgm here
    except PermissionError:
        print("Permission denied for the folder:", folder)
        continue

    print("===== List of files in the folder: ----->>", folder)
    # print("Folder names:", list_of_files)
    # print(os.listdir(folder))
    # print(folder)
    # print(type(folder))

    for file in list_of_files:
        print("File name:", file)

## Exceptional handling
## If user provided folder are not present then it will throw an error
