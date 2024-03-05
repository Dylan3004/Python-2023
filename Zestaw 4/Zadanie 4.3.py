# podpunkt A)
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo,
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print("foo(", self, ",", x, ")")

    @classmethod
    def class_foo(cls, x):
        print("class_foo(", cls, ",", x, ")")

    @staticmethod
    def static_foo(x):
        print("static_foo(", x, ")")

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def foo(self):
        pass

class Derived1(Base):
    def foo(self):
        print("Derived1.foo()")

class Derived2(Base):
    def foo(self):
        print("Derived2.foo()")

Derived1().foo() # Derived1.foo()
Derived2().foo() # Derived2.foo()

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu
class C:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

c = C()
print(c.x) # 0
c.x = 123
print(c.x) # 123
