class Animal:
    def __init__(self):
        print("create animal")

    def __del__(self):
        print("delete animal")

    def sound(self):
        print("animal makes a sound")

class Dog(Animal):
    def __init__(self):
        #super().__init__()  # เรียก parent class constructor
        print("dog")

    def __del__(self):
        print("delete dog")

    def sound(self):
        print("dog barks")

class Cat(Animal):
    def __init__(self):
        #super().__init__()  # เรียก parent class constructorr
        print("cat")

    def __del__(self):
        print("delete cat")

    def sound(self):
        print("cat meows")



def animal_sound(animal):
    animal.sound()  # Call the sound method, polymorphic behavior based on object type

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()

print()
# polymorphism
animal_sound(a)  # เรียก Animal's sound method
animal_sound(d)  # เรียก Dog's sound method
animal_sound(c)  # เรียก Cat's sound method
print()

del a
del d
del c

