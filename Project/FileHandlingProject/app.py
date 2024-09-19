import os

def create_file(fileName):
    try:
        with open(fileName, 'x') as f:
            print(f"File Name {fileName}: Created Successfully!")
    except FileExistsError:
        print(f"File Name {fileName} already exists")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def view_all_files():
    # List all the files in the current directory.
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        print("Files in directory:")
        for file in files:
            print(file)

def delete_file(fileName):
    try:
        os.remove(fileName)
        print(f"{fileName} has been deleted successfully")
    except FileNotFoundError:
        print(f"File not found: {fileName}")
    except Exception as e:
        print(f"An error occurred while deleting {fileName}: {str(e)}")

def read_file(fileName):
    try:
        with open(fileName, 'r') as f:
            content = f.read()
            print(f"Content of '{fileName}':\n{content}")
    except FileNotFoundError:
        print(f"{fileName} does not exist")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def edit_file(fileName):
    try:
        with open(fileName, 'a') as f:
            content = input("Enter data to add to the file: ")
            f.write(content + "\n")
            print(f"Content added to {fileName} successfully")
    except FileNotFoundError:
        print(f"{fileName} not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    while True:
        print("\nWelcome to File Management App")
        print("1: Create file")
        print("2: View all files")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit from App")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            fileName = input("Enter the file name to create: ")
            create_file(fileName)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            fileName = input("Enter the name of the file you want to delete: ")
            delete_file(fileName)
        elif choice == '4':
            fileName = input("Enter the file name you want to read: ")
            read_file(fileName)
        elif choice == '5':
            fileName = input("Enter the file name to edit: ")
            edit_file(fileName)
        elif choice == '6':
            print("Exiting from App. Goodbye!")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()


