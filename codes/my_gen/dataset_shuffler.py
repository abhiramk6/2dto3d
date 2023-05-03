import os
import random
import shutil

# Set the paths to the source and destination directories
src_dir = '/ext_data'
dst_dir = '/unspliy'

# Set the number of images you want to move
num_images = 10000

# Get a list of all the image files in the source directory
image_files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if f.endswith('.jpg') or f.endswith('.png')]

# Pick a random sample of image files
selected_files = random.sample(image_files, num_images)

# Move the selected files to the destination directory
for file in selected_files:
    shutil.move(file, dst_dir)
