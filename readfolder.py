import os

folders = input("Enter the folder names separated by space: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
        print("--- Files from the folder: " + folder)
    except FileNotFoundError:
        print("Kindly provide valid input or folder does not exit" + folder)
        continue
    except PermissionError:
        print("No access to folder:" + folder)
        continue

    for file in files:
        print(file)