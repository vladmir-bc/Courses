from pylab import *

x = linspace(0, 5, 10)
y = x ** 2
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left, bottom,width, height (range 0 to 1) - Добавили оси.
# 0.1, 0.1 - начало: отступ 10% от левого края и 10% от нижнего края; 0,8; 0,8 - масштаб: 80% график занимает
# по ширине и 80% - по высоте
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
plt.show()
