'''Создайте класс Dog, у которого есть:

конструктор __init__, принимающий 2 аргумента: name, age.
метод description, который возвращает строку в виде "<name> is <age> years old"
метод speak принимающий один аргумент, который возвращает строку вида "<name> says <sound>";'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        self.sound = sound
        return f"{self.name} says {self.sound}"



jack = Dog("Jack", 4)

print(jack.description()) # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'