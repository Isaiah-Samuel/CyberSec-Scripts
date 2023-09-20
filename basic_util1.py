# ======================================================================
# Lock a File (Not Witeable) not readable = 0o222, not writeable = 0o444
# ======================================================================
import os

file_path = "example.txt"  # Replace with the path to your file

# Check if the file exists
if os.path.exists(file_path):
    try:
        # Remove read permission for the owner of the file
        os.chmod(file_path, 0o222)  # This sets the file permissions to "--w--w--w-"

        print(f"The file '{file_path}' is no longer readable.")
    except OSError as e:
        print(f"Error: {e}")
else:
    print(f"The file '{file_path}' does not exist.")

# ======================================================
# Check if a File is Locked and Not Writtable 
# =========================================================
 
def is_file_locked(filename):
    try:
        with open(filename, 'w'):
            pass  # Try to open the file in write mode
        return False  # File is not locked and is writable
    except IOError as e:
        return True  # File is locked or not writable

filename = 'login_attempts.txt'  # Replace with the path to your file
if is_file_locked(filename):
    print(f"{filename} is locked or not writable.")
else:
    print(f"{filename} is not locked and is writable.")

