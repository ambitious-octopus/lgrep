import os
import random
import string

# Set up the parameters for the directory
root_dir = "test-tree"
num_files = 30
file_extensions = ['txt', 'csv', 'py', 'jpg', 'pdf', 'docx', 'mp3', "png"]

# Function to generate a random string of fixed length
def random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Function to create a directory with random files
def create_files_in_directory(directory, num_files):
    os.makedirs(directory, exist_ok=True)
    
    for _ in range(num_files):
        file_name = f"{random_string()}.{random.choice(file_extensions)}"
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as f:
            f.write('')  # Create an empty file

# Create the directory and files
create_files_in_directory(root_dir, num_files)

print(f"Random files created in directory {root_dir}")