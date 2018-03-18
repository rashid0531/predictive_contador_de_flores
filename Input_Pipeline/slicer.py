'''
Author: Mohammed Rashid Chowdhury
email:  <mrc689@mail.usask.ca>
Script name: slicer.py
'''

# For slicing images a library called image_slicer is used whose details can be found in
# their documentation ("https://media.readthedocs.org/pdf/image-slicer/latest/image-slicer.pdf")
import image_slicer
import os
from PIL import Image,ImageFile
import numpy as np

ImageFile.LOAD_TRUNCATED_IMAGES = True

output_directory = "/u1/rashid/Data/predictive_flower_counter/splited_images"
input_directory = "/discus/"

# This function slices a given image into user given number of tiles.
def make_Tiles(img_path,number_of_tiles,directory):
    img = Image.open(img_path)
    print(img.size)

    # if(hasattr(img,'filename')):
    #     print(img.filename)
    #     save_as = 'cropped_'+img.filename+'.jpg'

    # Get the size of the image
    width, height = img.size

    tiles = image_slicer.split_image(img_path, number_of_tiles,save =False)

    # Check if the given directory exists, if not create new directory.
    if not os.path.exists(directory):
        os.makedirs(directory)

    image_slicer.save_tiles(tiles, directory=directory,prefix='slice')


# test if the function works.
make_Tiles('../Preprocess_data/dhiki.jpg', 5,"../image_tiles")