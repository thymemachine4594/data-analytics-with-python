class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Jenn", 20)
print(s1.name)

d= Dog()
d.sound()
print(len("hello"))   # string
print(len([1,2,3]))   # list