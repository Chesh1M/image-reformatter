import os
import shutil

# Directories to delete images from
input_dir = 'images'
output_dir = 'reformatted_images'

# Function to empty the directories
def clear_directories(directory):
    try:
        shutil.rmtree(directory)
        os.mkdir(directory)
        print(f'Cleared and recreated {directory}')
    except Exception as e:
        print(f'Error clearing {directory}: {e}')

# Empty both directories
clear_directories(input_dir)
clear_directories(output_dir)
