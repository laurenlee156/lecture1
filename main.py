# m.py -> x = 1
# import m (module), if you want to see x use m.x
# del m.x -> removes x = 1 from m.py

'''
x = ["a", "b"]
y = ["a", "b"]

== compares the value of the object
"is" compares the memory location inside of python
x[0] == y[0] -> returns True
x[0] == y[1] -> returns False
x == y -> returns True
x is y -> returns False bc x and y are in different locations, even though their values r the same

x = [1, 2, 3]
x.append(4) -> appends 4 to the end of the list
x[0] = -1 -> deletes the x[0] = 1 object (cannot access this object), binds x[0] to -1
y = x -> binds y to [1, 2, 3] since the object(x) is in the same memory location
if y[0] = 1, then x[0] will also = 1, so it changes the memory as a whole since y = x
if you  do y = copy(x), y is in a different memory location than the original x, so x[0] is y[0] would return false, but
x[0] == y[0] returns true

another binding operation: :=
if f() > 0: -> quote f() once
    return f() -> quote f() twice, therefore taking 2x the amnt of time
alternative/more efficient way:
x = f()
if x > 0:
    return x
using the new operator (walrus operator):
if x := f() > 0:
    return x

x = [0, [1]]
y = list(x) -> copies the list, doesnt create another list
question: is y[1][0] == x[1][0]? and y[1][0] is x[1][0]? and y is x?
y[1][0] =

shallow copy
copy.copy()
y is a new/independent object with the same contents as x, so when you change something in x, it will change same thing in y

deep copy
import copy
copy.deepcopy()
fully independent objects
y = deepcopy(x) -> makes x and y separate objects

class Calculation
def add(self, a, b):
    return a + b

x = Calculation()
x.add(2, 3)
Calculation.add(x, 2, 3)
? type(x).add(x, 2, 3)

user defined functions
def ....

building method
str.upper()

SCOPE
built-ins -> global -> enclosing -> local
x = 1
def ___
    x = 2 -> local variable
    print(x) -> prints 2

def ___
   print(x) -> prints 1 since theres only a global variable, not local or enclosing


x = "global"
def f():
    x = "local"
    print(x) -> prints "local"

def f():
    x = "enclosing"
    def g():
        x = "local"
        print(x)
    return g -> returns "local"

def f():
    x = "enclosing"
    def g():
        nonlocal x -> "nonlocal" is a keyword that refers to the variable in the next level
        print(x)
    return g -> returns "enclosing"

'''


