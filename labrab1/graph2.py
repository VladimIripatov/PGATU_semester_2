import matplotlib.pyplot as plt 
import numpy as np

 

def func(x, a, b, c):                                       #функция
    return a*x**3 + b*x + c

styles = plt.style.available                                #список стилей
plt.style.use(styles[3])                                    #стиль

fig = plt.subplots()[0]                                     
fig.set_figwidth(5); fig.set_figheight(5)                   #размер окна

a,b,c = -5,77,34
left,right,step = -10,10,.1

d_x = np.arange(left, right, step)
d_y = [func(x, a, b, c) for x in d_x]

legend = '{}*x**2 + {}*x + {}'.format(a,b,c)                
plt.title("График функции")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)
plt.plot(d_x, d_y,linewidth = 4, color = 'blue')  
plt.legend([legend])
plt.axhline(linewidth = 2,color = 'gray')
plt.axvline(linewidth = 2,color = 'gray')



plt.show()