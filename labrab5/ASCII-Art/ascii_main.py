from ascii import get_image,symbols,ascii_art,resize

#открываем картинку и меняем размер
image = get_image()
new_size = int(input("Укажите необходимый размер - "))
image = resize(image,new_size)

#выбираем символы, из которых изображение будет состоять
print("Выберите набор символов")
symbols,dict_symbols = symbols()
symbols = int(input())


#выбираем дополнительные модули
invert = int(input("1 - Инвертирование по горизонтали\n\
2 - Инвертирование по вертикали\n\
3 - Инвертирование по горизонтали + вертикали\n\
4 - Инвертирование цвета\n\
5 - Ничего"))
symbols = str(symbols)
final = ascii_art(dict_symbols,symbols,image,invert)

#финал
name = input("Название итогового файла - ")
f1 = open(name + '.txt','w',encoding='utf-8')
f1.write(final)
f1.close()
