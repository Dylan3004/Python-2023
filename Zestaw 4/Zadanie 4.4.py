from __future__ import annotations

import functools
# Komentarz do zadania , chcialem zrobić za pomoca samych dekoratorów funkcję sumująca jednakże
# nie udało mi się zrobić tego za pomocą dekoratorów, więc zrobiłem to za pomocą funkcji sum
#ze względu na to że przykładowa funkcja
# @my_fun.register
# def _(arg1: float,arg2: list, verbose=True):
#     if verbose:
#         print("float i lista")
#     print(arg2.insert(0,arg1))
#
# nie działała poprawnie, ponieważ dekorator traktował drugi arguemnt jako float a nie jako listę ponieważ pierwszy z argumentów był float
# i nie mogłem tego naprawić, więc zrobiłem to za pomocą funkcji sum
import math





@functools.singledispatch
def my_fun_bigger(arg1, verbose=True):
    if verbose:
        print("Something")
    raise TypeError("Nie można powiększyć tego typu")

@my_fun_bigger.register
def _(arg1: float, verbose=True):
    if verbose:
        print("liczba zmiennoprzecinkowa")
    if arg1 > 0:
        return arg1**2
    else:
        return math.sqrt(arg1)

@my_fun_bigger.register
def _(arg1: int, verbose=True):
    if verbose:
        print("liczba calkowita")
    if arg1 > 0:
        return arg1**2
    else:
        return -(arg1**2)

@my_fun_bigger.register
def _(arg1: str, verbose=True):
    if verbose:
        print("string")
    return (arg1 + arg1).upper()

@my_fun_bigger.register
def _(arg1: tuple, verbose=True):
    if verbose:
        print("tuple")
    return arg1+arg1


@my_fun_bigger.register
def _(arg1: list, verbose=True):
    if verbose:
        print("list")
    return arg1+arg1

class Klasa:

    @functools.singledispatchmethod
    def my_fun_smaller(arg1, verbose=True):
        if verbose:
            print("Something")
        raise TypeError("Nie można powiększyć tego typu")

    @my_fun_smaller.register
    def _(arg1: float, verbose=True):
        if verbose:
            print("liczba zmiennoprzecinkowa")
        if arg1 > 0:
            return math.sqrt(arg1)
        else:
            return arg1**2

    @my_fun_smaller.register
    def _(arg1: int, verbose=True):
        if verbose:
            print("liczba calkowita")
        if arg1 > 0:
            return math.sqrt(arg1)
        else:
            return math.sqrt(-arg1)

    @my_fun_smaller.register
    def _(arg1: str, verbose=True):
        if verbose:
            print("string")
        if len(arg1) > 1:
            return arg1[0:len(arg1)//2].lower()
        else:
            return arg1.lower()

    @my_fun_smaller.register
    def _(arg1: tuple, verbose=True):
        if verbose:
            print("tuple")
        if len(arg1) > 1:
            return arg1[0:len(arg1)//2]
        else:
            return arg1

    @my_fun_smaller.register
    def _(arg1: list, verbose=True):
        if verbose:
            print("list")
        if len(arg1) > 1:
            return arg1[0:len(arg1)//2]
        else:
            return arg1

    @my_fun_smaller.register
    def _(arg1: dict, verbose=True):
        if verbose:
            print("dict")
        if len(arg1) > 1:
            return list(arg1.keys())[0:len(arg1)//2]+list(arg1.values())[0:len(arg1)//2]
        else:
            return arg1





# a)
#tests
#int
print(my_fun_bigger(2))
#float
print(my_fun_bigger(2.0))
#list
print(my_fun_bigger([1,2,3]))
#string
print(my_fun_bigger("1"))
#tuple
print(my_fun_bigger((1,2,3)))





#b)
#tests
# int
print(Klasa.my_fun_smaller(2))
# float
print(Klasa.my_fun_smaller(2.0))
# list
print(Klasa.my_fun_smaller([1,2,3]))
# string
print(Klasa.my_fun_smaller("1"))
# tuple
print(Klasa.my_fun_smaller((1,2,3)))
# dict
print(Klasa.my_fun_smaller({1:2,3:4}))












