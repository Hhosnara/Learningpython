# function
def my_function(a,b):
    print(a+b)

my_function(2, 2) 

def another_function(**args):
    print("lname is : " + args["lname"])

another_function(fname = "Anna", lname = "Haa")    

def print_in_series(a , b):
    print(a + b)
print_in_series(5, 1)
print_in_series(8, 2)
print_in_series(3, 5)

#passing list as argument

def my_fruit_function(diet):
  for x in diet:
    print(x)
fruits = ["apple", "banana", "orange", "papaya"]
my_fruit_function(fruits)

#recursive function

def recurse(R):
    if (R > 0):
        result = R + recurse(R-1)
        print(result)
    else:
        result = 0
    return result    
recurse(7)

# python lambda function
x = lambda a,b,c : a + b +c
print(x(2,3,5))