# https://realpython.com/python-property/

# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y

#     def get_x(self):
#         return self._x

#     def set_x(self, value):
#         self._x = value

#     def get_y(self):
#         return self._y

#     def set_y(self, value):
#         self._y = value


# class Circle:
#     def __init__(self, radius):
#         print('init')
#         self._radius = radius

#     def _get_radius(self):
#         print("Get radius")
#         return self._radius

#     def _set_radius(self, value):
#         print("Set radius")
#         self._radius = value

#     def _del_radius(self):
#         print("Delete radius")
#         del self._radius

#     radius = property(
#         fget=_get_radius,
#         fset=_set_radius,
#         fdel=_del_radius,
#         doc="The radius property."
#     )

# Circle(5)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         print(self.x)
#         print(self._x)
#         return self._x

#     @x.setter
#     def x(self, value):
#         try:
#             self._x = float(value)
#             print("Validated!")
#         except ValueError:
#             raise ValueError('"x" must be a number') from None

#     @property
#     def y(self):
#         return self._y

#     @y.setter
#     def y(self, value):
#         try:
#             self._y = float(value)
#             print("Validated!")
#         except ValueError:
#             raise ValueError('"y" must be a number') from None

# Point(1, 1)

# def func(a):
#     return a

# func = decorator(func)


# @decorator
# def func(a):
#     return a


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None


point = Point(12, 5)