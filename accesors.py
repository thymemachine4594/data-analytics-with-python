class grandfather:
    def meth1(self):
        print("car")
class brother(grandfather):
    def meth2(self):
        print("bike")
class sister(grandfather):
    def meth3(self):
        print("bicycle")
        
b=brother()
s=sister()

b.meth1()
s.meth1()

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())