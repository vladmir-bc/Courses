# Практика. Класс Point. Рассмотрим точку в двухмерном пространстве (x, y)

class Point:
    # создадим атрибут, который распространяется на весь класс
    list_points = [] # список всех наших точек


    def __init__(self, coord_x=0, coord_y=0):
        # также перепишем метод init, мы также можем задействовать move_to
        # self.x = coord_x
        # self.y = coord_y
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)  # мы не можем просто так обращаться к атрибуту list_points, это нужно делать через класс

    # Заведем поведение для точек. Например, точки могут перемещаться по координатной плоскости
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    # Создадим метод go_home, который сбрасываает координаты точки на 0,0
    def go_home(self):
        # self.x = 0
        # self.y = 0
        # мы можем использовать метод move_to, чтобы переместить точку в начало координат
        self.move_to(0, 0)

    # такой принцип написания кода называется dry - don't repeat yourself

    # Добавим метод для вывода точки
    def print_point(self):
        print(f"Точка с координатами ({self.x}, {self.y})")

    # Метод, который работает не с одним, а с несколькими экземплярами класса
    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен быть точкой (принадлежать классу Point")
        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5

p1 = Point(3, 4)
p2 = Point(-54, 32)
p3 = Point()
p3.move_to(4, 5)
p3.move_to(-90, 5)
p5 = Point()
p5.move_to(7, -43)
p5.print_point()
p7 = Point(6, 0)
p8 = Point(0, 8)
print(p7.calc_distance(p8))
print(Point.list_points)