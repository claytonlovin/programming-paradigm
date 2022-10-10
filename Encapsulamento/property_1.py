
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value
    
    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)

# PRINTAR A SOMA DO @X.SETTER
foo.x = 20
print(foo.x)

#
del foo.x
print(foo.x)