# 9.3.2. Class Objects

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

# creates a new instance of the class and assigns this object to the local variable x.
x = MyClass()

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart
xcomplex = Complex(3.0, -4.5)
print(xcomplex.r,xcomplex.i)


# 9.3.3. Instance Objects

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


# 9.3.4. Method Objects

x.f()
# In the MyClass example, this will return the string 'hello world'.
# However, it is not necessary to call a method right away: x.f is a method object, and can be stored away and called at a later time. For example:

xf = x.f
# while True:
#     print(xf())


# 9.3.5. Class and Instance Variables

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks) # ['roll over']

print(e.tricks) # ['play dead']

# 9.4. Random Remarks

# Each value is an object, and therefore has a class (also called its type).
print(xcomplex.__class__)
print(d.__class__)
print(e.__class__)

# 9.5. Inheritance

# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>


# Python has two built-in functions that work with inheritance:

# Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

# Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

# 9.5.1. Multiple Inheritance

# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>