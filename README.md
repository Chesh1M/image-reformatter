# What is this for?  
This is a script to help remove background from your images, resize them to 512x512px (at least one side being 512px and the other at most 512px)

How to use
- Open the folder path in terminal
- Install the necessary packages `pip install -r requirements.txt`
- Load your images into the `images` directory
- Run the `image-reformatter.py` script to reformat all the photos in the `images` directory
- Get your formatted photos from the `reformatted_images` directory
- Run the `cleanup.py` script to clear the `images` and `reformatted_images` folders
