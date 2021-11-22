from PIL import Image, ImageDraw
import random
import numpy as np


imageSize = 16


def create_random_array(size):
    colorArray = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
    array = []
    for i in range((2*size)):
        color_list = []
        for j in range(size):
            blackRandom = random.randint(0, 9)
            if(blackRandom > 5):
                color_list.append(random.choice(colorArray))
            else:
                color_list.append("#000000")
        array.append(color_list)
    return np.array(array)


def mirror_array(array):
    return np.pad(array, ((0, 0), (0, len(array[0]))), mode="symmetric")


for iteration in range(100):

    avatar = Image.new("RGB", (imageSize, imageSize))
    colorArray = []
    colorArray = mirror_array(create_random_array(int(imageSize/2)))
    draw = ImageDraw.Draw(avatar)

    for y, row in enumerate(colorArray):
        for x, point in enumerate(row):
            draw.point((x, y), point)

    avatar = avatar.resize((1024, 1024), resample=Image.NEAREST)
    avatar.save('avatar{}.png'.format(iteration))
    avatar.close()
