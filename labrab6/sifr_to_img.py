from PIL import Image


#приготовления к шифру
def alphabet():
    alph = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    eng_alph = 'abcdefghijklmnopqrstuvwxyz'
    nums = '1234567890'
    symb = '–:;?!&-+=(){}[]#№*/.,~«»'
    alph += alph.upper() + eng_alph + eng_alph.upper() + nums + symb + '\n'
    alph += '`'
    return alph

def get_bit(pos, shift):
    mask = 1 << shift # формируем маску
    sign = (pos & mask) >> shift # узнаём значение бита
    return sign

file = open('text.txt','r',encoding='utf-8')
text_to_sifr = file.read()
file.close()
name = 'r.png'
img = Image.open(name)
width, height = img.size
rastr = img.load()


alphabet = alphabet()
x, y = 0, 0
symbol = 0

while symbol < len(text_to_sifr):
    if (len(text_to_sifr) * 8) > width * height:
        print("Картинка слишком маленькая")
        break
    pos = alphabet.find(text_to_sifr[symbol])
    for shift in range(8):
        r, g, b = rastr[x, y]
        b = (b & 254) | get_bit(pos, shift)
        rastr[x,y] = (r,g,b)
        x += 1
        if x == width:
            x = 0
            y += 1
    symbol += 1
    if symbol == len(text_to_sifr):
        pos = alphabet.find('`')
        for shift in range(8):
            r, g, b = rastr[x, y]
            b = (b & 254) | get_bit(pos, shift)
            rastr[x,y] = (r,g,b)
            x += 1
            if x == width:
                x = 0
                y += 1
img.save('sifr_' + name)