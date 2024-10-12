import os 
import subprocess

def main():
    while True:
        print("Press 1: To update ameyo app server build")
        print("Press 2: To update art server build")
        print("Press 3: To update djinn server build")
        print("Press 4: To update asterisk server build")
        print("Press q to quit")

        choice = input("Enter your choice: ").strip().lower()
        if choice == "q":
            print("Exiting the script")
            break

        package_path = input("Enter the full path with filename: ").strip()

        if not os.path.exists(package_path):
            print(f"Error: The file '{package_path}' does not exist.")
            continue

        if choice == '1':
            update_server("ameyo app",package_path)
        elif choice == '2':
            update_server("Art", package_path)
        elif choice == '3':
            update_server("djinn",package_path)
        elif choice == '3':
            update_server("asterisk",package_path)
        else:
            print("Invalid choice. Please try again.")



def update_server(server_app_name,file_path):
    command = f"rpm -Uvh {file_path}"
    print(f"updating {server_app_name} with command: {command}")
    try:
        process = subprocess.run(command,shell = True,capture_output=True,text=True)
        print(process.stdout)
        if process.check_returncode !=0:
            print(f"Error Occurred: {process.stderr}")
    except Exception as e:
        print(f"Failed to update {server_app_name}, Error: {e}")
    
if __name__=="__main__":
    main()


'''
Runs the command (command) in a shell environment (because shell=True).
Captures the output (both stdout and stderr) using capture_output=True.
Returns the output as text (because text=True), making it easier to work with in Python.
'''

'''
import subprocess
import os
def main():
    while True:
        print("Press 1: To update ameyo app server build")
        print("Press 2: To update art server build")
        print("Press 3: To update djinn server build")
        print("press 4: To update asterisk server build")
        print("Press q to quit")
        choice = input("Enter your choice: ")
        package_path = input("Enter the fullpath with filename")
        if not os.path.exists(package_path):
            print(f"Error: the file '{package_path}' does not exits.")
            continue
        if choice == "1":
            app_server(package_path)
        elif choice == "2":
            art_server(package_path)
        elif choice == "3":
            djinn_update(package_path)
        elif choice == "4":
            asterisk_update(package_path)
        elif choice.lower() == "q":
            print("Exiting the script...")
            break
        else:
            print("Invalid choice. Please try again.")
    def app_server(file_path):
        command = f"rpm -Uvh {file_path")
        process = subprocess.run(command,shell = True, capture_output=True, text = True)
        print(process.stdout)
    def art_server(file_path):
        command = f"rpm -Uvh {file_path}"
        process = subprocess.run(command,shell = True, capture_output=True, text = True)
        print(process.stdout)
    def djinn_update(file_path):
        command = f"rpm -Uvh {file_path}"
        process = subprocess.run(command,shell = True, capture_output=True, text = True)
        print(process.stdout)
    def asterisk_update(file_path):
        command = f"rpm -Uvh {file_path}"
        process = subprocess.run(command,shell = True, capture_output=True, text = True)
        print(process.stdout)
if __name__ == "__main__":
    main()
'''
