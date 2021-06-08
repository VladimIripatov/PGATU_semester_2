
def sifr(just_an_str,key):  #функция шифратор
    sifr_str = ''
    for pos in range(len(just_an_str)):
        pos_in_list = alph.find(just_an_str[pos])
        new_pos = pos_in_list + key
        if new_pos >= len(alph):
            new_pos -= len(alph)
        sifr_str += alph[new_pos]
    return sifr_str

def desifr(sifr_str,key):   #функция дешфратор
    desifr_str = ''
    for pos in range(len(sifr_str)):
        pos_in_list = alph.find(sifr_str[pos])
        new_pos = pos_in_list - key
        if new_pos <= 0:
            new_pos += len(alph)
        desifr_str += alph[new_pos]
    return desifr_str


#символы
alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
nums = '1234567890'
symbols = ':;?!&-+=()*/.,'
alph += alph.upper() + nums + symbols


#Начало программы
sifr_or_desifr = int(input("1 - шифровать\n2 - расшифровать \n"))


if sifr_or_desifr == 1:
    print(sifr(input("Введите строку - "),int(input("Введите ключ - "))))
if sifr_or_desifr == 2:
    print(desifr(input("Введите строку - "),int(input("Введите ключ - "))))