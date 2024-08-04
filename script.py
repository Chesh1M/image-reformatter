import os
from PIL import Image
from rembg import remove

# Input & Output directories
input_dir = 'images'
output_dir = 'reformatted_images'

# Make output directory, ignore if already exists
os.makedirs(output_dir, exist_ok=True)

# Define size to resize to
target_size = (512,512)

# Function to resize & remove background from images
def resize_image(image_path, output_path, target_size):
    with Image.open(image_path) as img:
        # Remove background
        img = remove(img)

        img.thumbnail(target_size, Image.LANCZOS)
        img.save(output_path, 'PNG')

# Process all images in the input directory
file_count = 1
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')): # checks for image files
        input_path = os.path.join(input_dir, filename) # get full path of image
        output_path = os.path.join(output_dir, f'photo{file_count}.png') # assign full path of output (resized) image
        
        # Resize image and log successful resizing
        resize_image(input_path, output_path, target_size)
        print(f'Resized and saved {filename} to {output_path}')
        
        # Increase counter
        file_count += 1