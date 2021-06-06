file_txt = open('text.txt', mode='r', encoding='utf-8')
text = file_txt.readlines()
name = text.pop(0)
file_txt.close()

html = open('page.html', mode='r', encoding='utf-8')
html_code = html.read()
html.close()

#ставим лимиты для .find()
limits = [
    '<div class="text">',      
    '</div>',                   
    '<div class="name">',
    '</div>' 
]

#имя в html
to_file = html_code[0 : html_code.find(limits[2]) + 18]
to_file += name
to_file += html_code[html_code.find(limits[3]): html_code.find(limits[0]) + 20]

#стих в код html
for line in text:
    line = line[0:-1]
    line += '<br>'
    to_file += line

#итог
to_file += html_code[html_code.find(limits[0])+ 18 ::]
file_html = open('index.html', mode='w', encoding='utf-8')
file_html.write(to_file)
file_html.close()
