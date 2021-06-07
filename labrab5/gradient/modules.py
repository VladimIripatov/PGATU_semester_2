from PIL import Image
from PIL import PSDraw


def get_image(): 
    image = Image.open('gradient.png')
    width, height = image.size
    return image,width,height

def gradient(image,height,width,kx): 
    check = height // 6
    r, g, b = 255, 50, 0    #каждый
    for y in range(height):
        if y <= check * 2:  #охотник желает
            if g < 255:
                g += (2 if g % 3 != 0 else 1)
            for x in range(width):
                image.putpixel((x,y), (r,g,b))
            continue
        if y <= check * 3:  #знать
            if g < 255:
                g += 1
            if r > 0:
                r -= 2
            for x in range(width):
                image.putpixel((x,y), (r,g,b))
            continue
        if y <= check * 4:  #где 
            if g < 255:
                g += 3
            if r > 0:
                r -= 1
            if b < 255:
                b += 4
            for x in range(width):
                image.putpixel((x,y), (r,g,b))
            continue
        if y <= check * 5:  #сидит 
            if g > 0:
                g -= (3 if g % 3 != 0 else 2)
            if r > 0:
                r -= 2
            if b < 255:
                b += 2
            for x in range(width):
                image.putpixel((x,y), (r,g,b))
            continue
        if y <= height:     #фазан
            if r < 255:
                r += 2
            if g > 0:
                g -= 1
            if b < 255:
                b += 2
            for x in range(width):
                image.putpixel((x,y), (r,g,b))
            continue
    return image
