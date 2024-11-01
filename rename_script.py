import os
import re

def normalize_name(name):
    """
    Normalize a name to lowercase with underscores:
    - Convert to lowercase
    - Replace spaces with underscores
    - Replace multiple underscores with single underscore
    - Remove any special characters except underscores
    """
    # Convert to lowercase
    name = name.lower()
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    # Replace multiple underscores with single underscore
    name = re.sub(r'_+', '_', name)
    # Remove any special characters (keep underscores)
    name = re.sub(r'[^a-z0-9_.]', '', name)
    return name

def rename_items(directory):
    """
    Recursively rename files and folders in the given directory.
    Processes folders first, then files to avoid path issues.
    """
    # Create lists to store all paths
    dir_items = []  # Store (old_path, new_path) for directories
    file_items = []  # Store (old_path, new_path) for files
    
    # Walk through directory tree bottom-up to handle subdirectories first
    for root, dirs, files in os.walk(directory, topdown=False):
        # Process directories
        for dir_name in dirs:
            old_path = os.path.join(root, dir_name)
            new_name = normalize_name(dir_name)
            if new_name != dir_name:
                new_path = os.path.join(root, new_name)
                dir_items.append((old_path, new_path))
                
        # Process PNG files
        for file_name in files:
            if file_name.lower().endswith('.png'):
                old_path = os.path.join(root, file_name)
                name_part, ext_part = os.path.splitext(file_name)
                new_name = normalize_name(name_part) + ext_part.lower()
                if new_name != file_name:
                    new_path = os.path.join(root, new_name)
                    file_items.append((old_path, new_path))
    
    # Perform the renaming
    # Start with files
    for old_path, new_path in file_items:
        try:
            os.rename(old_path, new_path)
            print(f"Renamed file: {old_path} -> {new_path}")
        except Exception as e:
            print(f"Error renaming file {old_path}: {str(e)}")
    
    # Then rename directories (in reverse order to handle nested dirs)
    for old_path, new_path in reversed(dir_items):
        try:
            os.rename(old_path, new_path)
            print(f"Renamed directory: {old_path} -> {new_path}")
        except Exception as e:
            print(f"Error renaming directory {old_path}: {str(e)}")

if __name__ == "__main__":
    # Get the directory path from user input
    directory_path = input("Enter the directory path to process: ")
    
    if os.path.exists(directory_path):
        print(f"Processing directory: {directory_path}")
        rename_items(directory_path)
        print("Renaming completed.")
    else:
        print("Directory not found!")
