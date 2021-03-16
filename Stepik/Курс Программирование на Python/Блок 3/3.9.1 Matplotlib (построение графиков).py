from pylab import *
x = linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)

figure()
plot(x, y, 'r')
xlabel('x') #Метка для оси Х - Х
xlabel('y') #Метка для оси У - У
title('title') #Название графика
show() #Показ графика