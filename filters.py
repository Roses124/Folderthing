# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(pic_name):
    im = Image.open(pic_name)
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(pic_name):
    pic_name.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(pic_name, filename):
    pic_name.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(im):
    pixel = list(im.getdata())
    new_image = []
    x = im.width
    y = im.height
    darkblue = (0, 51, 76)
    red = (217, 26, 33)
    lightblue = (112, 150, 158)
    yellow = (252, 227, 166)
    for pix in pixel:
        intensity = pix[0] + pix[1] + pix[2]
        if intensity < 182:
            new_image.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            new_image.append(red)
        elif intensity >= 364 and intensity < 546:
            new_image.append(lightblue)
        elif intensity >= 546:
            new_image.append(yellow)
    newthing = Image.new("RGB", im.size)
    newthing.putdata(new_image)
    return newthing


def blue(im):
    pixel = list(im.getdata())
    new_image = []
    x = im.width
    y = im.height
    darkblue = (9, 48, 141)
    regblue = (105, 148, 249)
    lightishblue = (182, 204, 255)
    lightblue = (204, 255, 255)
    for pix in pixel:
        intensity = pix[0] + pix[1] + pix[2]
        if intensity < 182:
            new_image.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            new_image.append(regblue)
        elif intensity >= 364 and intensity < 546:
            new_image.append(lightishblue)
        elif intensity >= 546:
            new_image.append(lightblue)
    newthing = Image.new("RGB", im.size)
    newthing.putdata(new_image)

    return newthing


def red(im):
    pixel = list(im.getdata())
    new_image = []
    x = im.width
    y = im.height
    darkred = (129, 0, 0)
    regred = (255, 1, 1)
    lightishred = (255, 152, 152)
    lightred = (255, 230, 230)
    for pix in pixel:
        intensity = pix[0] + pix[1] + pix[2]
        if intensity < 182:
            new_image.append(darkred)
        elif intensity >= 182 and intensity < 364:
            new_image.append(regred)
        elif intensity >= 364 and intensity < 546:
            new_image.append(lightishred)
        elif intensity >= 546:
            new_image.append(lightred)
    newthing = Image.new("RGB", im.size)
    newthing.putdata(new_image)

    return newthing

def merica(im):
    pixel = list(im.getdata())
    new_image = []
    iter = 0
    for pix in pixel:
        if iter < im.width / 2:
            darkred = (129, 0, 0)
            regred = (255, 1, 1)
            lightishred = (255, 152, 152)
            lightred = (255, 230, 230)
            for pix in pixel:
                intensity = pix[0] + pix[1] + pix[2]
                if intensity < 182:
                    new_image.append(darkred)
                elif intensity >= 182 and intensity < 364:
                    new_image.append(regred)
                elif intensity >= 364 and intensity < 546:
                    new_image.append(lightishred)
                elif intensity >= 546:
                    new_image.append(lightred)
        elif iter >= im.width / 2:
            darkblue = (9, 48, 141)
            regblue = (105, 148, 249)
            lightishblue = (182, 204, 255)
            lightblue = (204, 255, 255)
            for pix in pixel:
                intensity = pix[0] + pix[1] + pix[2]
                if intensity < 182:
                    new_image.append(darkblue)
                elif intensity >= 182 and intensity < 364:
                    new_image.append(regblue)
                elif intensity >= 364 and intensity < 546:
                    new_image.append(lightishblue)
                elif intensity >= 546:
                    new_image.append(lightblue)
            newthing = Image.new("RGB", im.size)
            newthing.putdata(new_image)
        iter += 1
    newthing = Image.new("RGB", im.size)
    newthing.putdata(new_image)

    return newthing
