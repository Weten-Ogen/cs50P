import sys
from PIL import Image

# A list to store the images
images = []

# Loop through the cli arg start at 1
for arg in sys.argv[1:]:
    # Opens the image file 
    image = Image.open(arg)
    # Adds the image to images
    images.append(image)

images[0].save(
    "cosutmes.gif", save_all=True,append_images=[images[1]],duration=200,loop=0
)




