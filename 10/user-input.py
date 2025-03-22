## input

# input() function is used to take input from the user.

# Syntax:
# input(prompt)

# prompt: A string, representing a default message before the input.

# Example: 
# name = input("Enter your name: ")
# print("Hello", name)

# number = input("please enter the numbner here:")
# print("The number is:", number)

# folders=input("enter the folder with space:").split() ## to take multiple input with space
# print(folders)


# folders=input("enter the folder with space:").split() ## to take multiple input with space
# for folder in folders:
#     print(folder)


# import os
# folders=input("enter the folder with space:").split() ## to take multiple input with comma
# for folder in folders:
#     files = os.listdir(folder)
#     print(files)

# import os
# folders=input("enter the folder with space:").split() ## to take multiple input with comma
# for folder in folders:
#     files=os.listdir(folder)
#     for file in files:
#         print(file)


## If user provided folder are not present then it will throw an error
## so we can handle it using try and except block

import os

folders=input("please enter the folders list with space in between:").split()

for files in folders:
    
    try:
        files=os.listdir(files)
    except FileNotFoundError:
        print("The folder does not exist, seems like does not exist", folders)
        continue
    for file in files:
        print(file)




import sys

print(sys.version)
