import matplotlib.pyplot as plt 
import numpy as np

 

def func(x, a, b, c):                                       #функция
    return (a*x**2 + b*x + c ) / (x + d)

styles = plt.style.available                                #список стилей
plt.style.use(styles[3])                                    #стиль

a,b,c,d = -5,77,34,-33
left,right,step = -100,100,0.5

d_x = np.arange(left, right, step)
d_y = [func(x, a, b, c) for x in d_x]
pos_x = 0

fig = plt.subplots()[0]                                     
fig.set_figwidth(5); fig.set_figheight(5) 

while pos_x <= right:                                       #подбор точки разрыва
    try:
        pos_y = func(pos_x, a, b, c)
        d_x.append(pos_x)
        d_y.append(pos_y)
    except:
        pos_x += step
    pos_x += step

legend = '{}*x**2 + {}*x + {}'.format(a,b,c)                

plt.title("График функции")                                 
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)
plt.plot(d_x, d_y,linewidth = 4, color = 'blue')  
plt.legend([legend])
plt.axhline(linewidth = 2,color = 'gray')
plt.axvline(linewidth = 2,color = 'gray')
plt.xkcd()

plt.show()