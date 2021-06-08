from PIL import Image

def alphabet():
    alph = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    eng_alph = 'abcdefghijklmnopqrstuvwxyz'
    nums = '1234567890'
    symb = '–:;?!&-+=(){}[]#№*/.,~«»'
    alph += alph.upper() + eng_alph + eng_alph.upper() + nums + symb + '\n'
    alph += '`'
    return alph

picture = 'sifr_r.png'
image = Image.open(picture)
width, height = image.size
rastr = image.load()

alphabet = alphabet()
result = ''
x, y = 0, 0
while True: 
    pos_b = ''
    for shift in range(8): # это сдвиг по битам символа 
        (r,g,b) = rastr[x, y]
        pos_b += str(b&1) # достаём последний бит
        x += 1
        if x == width:
            x = 0
            y += 1
    pos = int(pos_b[::-1], 2)
    if alphabet[pos] == '`':
        break
    result += alphabet[pos]

print(result)