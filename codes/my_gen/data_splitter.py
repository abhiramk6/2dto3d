import os
import shutil

# Set the path to the directory you want to search
directory_path = "/Users/abhiramkamini/Downloads/paper/left_right"

i = 0
# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    i += 1

    if not i % 1000: print(i)
    # Check if the file is not a directory
    if not os.path.isdir(os.path.join(directory_path, filename)):

        # Check if the folder name starts with "right"
        if filename.lower().startswith("right"):
            right_folder_path = "/dataset/train/right"

            # Move the file to the folder
            shutil.move(os.path.join(directory_path, filename), os.path.join(right_folder_path, filename))

        # Check if the folder name starts with "left"
        elif filename.lower().startswith("left"):
            left_folder_path = '/dataset/train/left'

            # Move the file to the folder
            shutil.move(os.path.join(directory_path, filename), os.path.join(left_folder_path, filename))
