import random as r
import os
import math

print(os.getcwd())

x = r.randint(1,100)
print(type(x), x)

y = True
print(type(y), y)

class Module1:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"Halo, am a habibi {self.name}")

module1 = Module1("hwobla")
module1.intro()
print(r.randint(1,100))

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Halol mammama {self.name}")

l = MyClass("name")

print(type(l))

print(dir(r)) # r => модуль рандом. Команда получает инфу о используемых в ней чего то там

print(getattr(r, 'randint'))

print(dir(l)) #dir позволяет получить все атрибуты модуля или класса

print(f"math = sqrt {hasattr(math, 'sqrt')}") #Проверяет на наличие атрибута
print(f"math = aaa {hasattr(math, 'aaa')}")