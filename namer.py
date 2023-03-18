import os

directory_path = "/Users/abhiramkamini/Downloads/paper/dataset/valid/left"

for filename in os.listdir(directory_path):
    if filename.startswith("left_frame_"):
        new_filename = filename.replace("left_frame_", "")
        os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
