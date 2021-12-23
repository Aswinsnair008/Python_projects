# I must be able to run the script in such a way that
# When I give the 2 arguements it must be able to
# first arguement is the folder name in which the images are present
# now i must be able to add a new folder inside that and convert all the jpg to png and put them in new folder

# the modules that we are importing are
import sys
import os
from PIL import Image
# check if the new folder exist or not if doesn't create one and add the files
# loop through the folder and convert them to png
# with the sys module we have to grab the first 2 arguement
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder,output_folder)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for pictures in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{pictures}')
    clean_name = os.path.splitext(pictures)[0]
    print(clean_name)
    img.save(f'{output_folder}{clean_name}.png','png')

