import os
from PIL import Image, ImageDraw
import random
import numpy as np


imageSize = 16
palette = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]


def mirror_array(array):
    # some numpy magic that mirrors an array vertically
    return np.pad(array, ((0, 0), (0, len(array[0]))), mode="symmetric")


def create_random_array(size, palette):
    # Let's create a random matrix of color, with half the
    # columns we need so it can be mirrored and become symmetric
    array = []
    for row in range(size):
        color_list = []
        for column in range(int(size/2)):
            blackBias = random.randint(0, 9)
            # in 10% increments, how much black is there in the image
            if(blackBias > 5):
                color_list.append(random.choice(palette))
            else:
                color_list.append("#000000")
        array.append(color_list)
    return mirror_array(np.array(array))


# lets do a bunch of avatars, so we can choose from the output
for iteration in range(100):
    # First we create a new image, and draw object, so we can draw on to it
    image = Image.new("RGB", (imageSize, imageSize))
    draw = ImageDraw.Draw(image)
    # then we create the color matrix
    colorMatrix = create_random_array(imageSize, palette)

    # and draw it to the image
    for y, row in enumerate(colorMatrix):
        for x, point in enumerate(row):
            draw.point((x, y), point)

    # finally, we resize the image so it can be more easily used, and save it
    image = image.resize((1024, 1024), resample=Image.NEAREST)
    # lets be tidy and put the output in a folder
    if not os.path.exists('output'):
        os.makedirs('output')
    image.save('output/image{}.png'.format(iteration))
    image.close()
