from modules import get_image,gradient

image,width,height = get_image()
kx = 256 / width
image = gradient(image,height,width,kx)
image.save('gradient.png')