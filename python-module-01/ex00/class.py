# CONTROL YOUR OBJECT INSTANTIATION
# Source: https://realpython.com/python-class-constructor/

class SomeClass:
    pass

result = SomeClass()

print(result)

class Point:
    def __new__(cls, *args, **kwargs) -> object:
        print("1. Create a new instance of Point.")
        return super().__new__(cls)

    def __init__(self, x, y)  -> None:
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y
        return None

    def __repr__(self) -> str:
        # provides a proper string representation for your Point class.
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

point = Point.__new__(Point)
print(type(point))
# print(type(point), point)