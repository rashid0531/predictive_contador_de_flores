'''
Author: Mohammed Rashid Chowdhury
email:  <mrc689@mail.usask.ca>
Script name: slicer.py
'''

# For slicing images a library called image_slicer is used whose details can be found in
# their documentation ("https://media.readthedocs.org/pdf/image-slicer/latest/image-slicer.pdf")
import image_slicer
import os



# This function slices a given image into user given number of tiles.
def make_Tiles(img_path,number_of_tiles,directory):

    tiles = image_slicer.slice('flower.jpg', number_of_tiles,save =False)

    # Check if the given directory exists, if not create new directory.
    if not os.path.exists(directory):
        os.makedirs(directory)

    image_slicer.save_tiles(tiles, directory=directory,prefix='slice')


# test if the function works.
make_Tiles('flower.jpg',5,"../image_tiles")