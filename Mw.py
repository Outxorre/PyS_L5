import math
import inspect
import random
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class walk(Animal):
    def __init__(self,name,age,color,walk):
        super().__init__(name,age,color)
        self.walk = walk

    def canWalk(self):
        if self.walk == True:
            print("can walk")
        else:
            print("cant walk")


class Voice(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age, color)
        self.voice = voice

    def canVoice(self):
        if self.voice == True:
            print("can make some voice")
        else:
            print("cant")

olen = walk("Olen", 32, "nigger", True)

#Интерспекция

print(dir(Animal))
print(f"class attr sqrt = {hasattr(math, 'sqrt')}")
print(getattr(olen, 'name'))

def this_is_example():

    """Документация ыееыеыуу я аутист"""
    pass
print(inspect.isfunction(this_is_example)) #True
print(inspect.ismodule(math)) #True
print(inspect.isclass(int)) #True

#print(inspect.getsource(math.sqrt)) Выведет ошибку ведь функция написана на C

print(inspect.getfile(this_is_example))
print(inspect.getdoc(this_is_example))

ui = random.randint(1,2)
print(dir(random))
print(type(ui))
print(getattr(random, 'randint'))

