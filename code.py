import os

# def make_file_writable(file_path):
#     try:
#         # Check if the file exists
#         if os.path.exists(file_path):
#             # Add write permission for the owner of the file
#             os.chmod(file_path, 0o644)  # This sets the file permissions to "-rw-r--r--"
#             return f"The file '{file_path}' is now writable."
#         else:
#             return f"The file '{file_path}' does not exist."
#     except OSError as e:
#         return f"Error: {e}"



# def read_locked_file(file_path):
#     try:
#         # Attempt to acquire a shared (read) lock on the file
#         with open(file_path, "r") as file:
#             fcntl.flock(file.fileno(), fcntl.LOCK_SH)
            
#             # Read the contents of the file while holding the lock
#             file_contents = file.read()
#             return file_contents
#     except FileNotFoundError:
#         return f"The file '{file_path}' does not exist."
#     except PermissionError:
#         return f"You do not have permission to read the file."
#     except Exception as e:
#         return f"An error occurred: {e}"

# # Example usage:
# file_path = "example.txt"  # Replace with the path to your file
# file_contents = read_locked_file(file_path)
# if isinstance(file_contents, str):
#     print("File contents:", file_contents)
# else:
#     print(file_contents)



# def read_locked_file(file_path):
#     try:
#         # Attempt to open the file for reading
#         with open(file_path, "r") as file:
#             try:
#                 # Attempt to acquire a lock on the file
#                 msvcrt.locking(file.fileno(), msvcrt.LK_RLCK, 0)
                
#                 # Read the contents of the file while holding the lock
#                 file_contents = file.read()
#                 return file_contents
#             except OSError:
#                 return f"Failed to acquire lock on '{file_path}'. Another process may be accessing it."
#     except FileNotFoundError:
#         return f"The file '{file_path}' does not exist."
#     except PermissionError:
#         return f"You do not have permission to read the file."
#     except Exception as e:
#         return f"An error occurred: {e}"

# Example usage:
# file_path = "example.txt"  # Replace with the path to your file
# file_contents = read_locked_file(file_path)
# if isinstance(file_contents, str):
#     print("File contents:", file_contents)
# else:
#     print(file_contents)

def make_file_writable(path):

    try:
        if os.path.exists(path):
            os.chmod(path,0o644)
            print(f'{path} file now writtable')
        else:
            return f'Error!!! {path} not found'
    except OSError as e:
        return f'Error!!!  {e} '

txt = 'login_attempts.txt'


# make_file_writable(txt)

with open(txt,'w') as file:
    text_file = file.write('write new')
    file.close()

with open(txt,'r') as file:
   file  =  file.read()
print(file)