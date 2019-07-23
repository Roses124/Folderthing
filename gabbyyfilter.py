

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


im = load_img("tiger.jpg")
newthings = blue(im)
save_img(newthings, "dogbama.jpg")
doggo = load_img("dogbama.jpg")
show_img(doggo)
newpic = load_img("dogbama.jpg")
show_img(doggo)
