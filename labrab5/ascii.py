from PIL import Image

#открываем картинку
def get_image():
    image = Image.open("krasota.png")
    return image


#изменяем размер картинки
def resize(img, height_new):
    width, height = img.size 
    width_new = width // (height//height_new)
    img_new = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_new

#используем символы
def symbols():
    file = open('symbols.ini', 'r',encoding='utf-8')
    symbols = file.read() 
    file.close()
    symbols = symbols.split('\n')
    dict_symbols = dict()
    for i in range(len(symbols)):
        dict_symbols.update([symbols[i].split('=')])
        print(symbols[i])
    return symbols,dict_symbols

#рисуем сам аски
def ascii_art(dict_symbols,symbols,image,invert):
    count = len(dict_symbols[symbols])
    full = 256 + 256 + 256
    segment = full // count
    final = ''
    width, height = image.size
    for y in range(height):
        result = ''
        for x in range(width):
            if invert == 4:
                r, g, b = image.getpixel((x, y))
                r = 255 - r
                g = 255 - g
                b = 255 - b
                image.putpixel((x, y), (r,g,b))
            r, g, b = image.getpixel((x, y))
            color = r + g + b
            pos = 0
            if color >= segment * 1:
                pos = 1
            if color >= segment * 2:
                pos = 2
            if color >= segment * 3:
                pos = 3
            result += dict_symbols[symbols][pos] * 3
        if invert == 1:
            result = result[::-1] + "\n"
        if invert == 2:
            result += '\n'
            final = result + final
        if invert == 3:
            result = result[::-1] + "\n"
            final = result + final
        if invert == 4 or invert == 5:
            final += result + '\n'
        
    return final


