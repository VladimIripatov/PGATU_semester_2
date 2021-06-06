import matplotlib.pyplot as plt 
import numpy as np

 

def func(x):                                                #функция
    return x**2

styles = plt.style.available                                #список стилей
plt.style.use(styles[3])                                    #стиль

fig = plt.subplots()[0]                                     
fig.set_figwidth(5); fig.set_figheight(5) 

left,right,step = -10,0,.01                                #левая часть
d_x = np.arange(left, right, step)
d_y = func(d_x)
plt.plot(d_x, d_y,linewidth = 3, color = 'blue')

left,right,step = 0,10,.01                                 #правая часть
d_x = np.arange(left, right, step)
d_y = func(d_x)
plt.plot(d_x, d_y,linewidth = 3, color = 'lightblue')



plt.title("График функции")                                 
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)
plt.axhline(linewidth = 2,color = 'gray')
plt.axvline(linewidth = 2,color = 'gray')
plt.xkcd()

plt.show()