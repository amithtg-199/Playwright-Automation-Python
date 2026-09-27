# file_operations.py
import os
import shutil

# 1. Writing to file (creates new if not exists, overwrites if exists)
def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to {file_path}")


# 2. Appending data into existing file
def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)
    print(f"Content appended to {file_path}")


# 3. Reading text file
def read_file(file_path, mode="all"):
    with open(file_path, 'r') as file:
        if mode == "all":
            return file.read()
        elif mode == "line":
            return file.readline()
        elif mode == "lines":
            return file.readlines()
        else:
            raise ValueError("Invalid mode. Use 'all', 'line', or 'lines'.")


# 4. Renaming a file
def rename_file(source, target):
    os.rename(source, target)
    print(f"File renamed from {source} to {target}")


# 5. Deleting a file
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted")
    else:
        print(f"File {file_path} does not exist")


# 6. Creating a Directory
def create_directory(dir_path):
    os.mkdir(dir_path)
    print(f"Directory {dir_path} created")


# 7. Checking if a Directory Exists
def check_directory_exists(dir_path):
    return os.path.exists(dir_path)


# 8. Renaming a Directory
def rename_directory(source, target):
    os.rename(source, target)
    print(f"Directory renamed from {source} to {target}")


# 9. Removing a Directory
def remove_directory(dir_path, force=False):
    if force:
        shutil.rmtree(dir_path)  # removes even if not empty
    else:
        os.rmdir(dir_path)  # only removes if empty
    print(f"Directory {dir_path} removed")


# 10. Get Current Working Directory
def get_current_working_directory():
    return os.getcwd()
