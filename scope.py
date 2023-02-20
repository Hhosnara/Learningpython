# python scope

def myfunc():
    x = 300
    def myinnerfunc(): 
     print(x)
    myinnerfunc()

myfunc()

# Module python

import mymodule
mymodule.greeting("Jonathan") 

