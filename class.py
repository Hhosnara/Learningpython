#classes/objects

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x) 

#Create a class named Person, use the __init__() function to assign values for name and age:

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#car class
class Cars():
    def __init__(self, brand, number):
        self.brand = brand
        self.number = number

c1 = Cars("Toyota", 2015)    

print(c1.brand)
print(c1.number) 

