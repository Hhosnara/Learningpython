# iterators

mytuple = ("Apple", "Orange", "Cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#strings iterable

mystr = "Banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Looping iterator for loop

mytuple = ("Apple", "Banana", "Cherry")

for x in mytuple:
    print(x)

#iterate character of a string

mystr = "banana"

for x in mystr:
    print(x)

#     Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


