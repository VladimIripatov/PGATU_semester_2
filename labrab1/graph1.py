import matplotlib.pyplot as plt 
import numpy as np


gr_styles = plt.style.available                             #список стилей


x = np.linspace(-5, 5, 100)                                 # координата  x
y = 5 * x**4 + 100                                          # координата y

fig, ax = plt.subplots()                                    #объекты окна и графиков

ax.plot(x, y, color = 'blue',lw = 3)                        # функция

ax.vlines(0, y.min(), y.max(), color = 'black',lw = 0.5)    # ось y
ax.hlines(0, x.min(), x.max(), color = 'black',lw = 0.5)    # ось x

plt.style.use(gr_styles[3])                                 #стиль
fig.set_figwidth(5); fig.set_figheight(5)                   # размер окна


plt.show()                                                  # показать