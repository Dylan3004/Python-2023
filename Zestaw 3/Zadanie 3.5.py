
class Bug:


    """
    Klasa reprezentująca robaki.

    Atrybuty:
    licznik - zlicza ilość robaków
    id - identyfikator robaka

    Metody:
    __init__ - inicjalizuje obiekt
    __del__ - niszczy obiekt
    __str__ - zwraca informacje o obiekcie
    docstring - zwraca docstring klasy
    """

    licznik = 0

    def __init__(self):
        type(self).licznik=type(self).licznik+1
        self.id=type(self).licznik

    def __del__(self):
        type(self).licznik = type(self).licznik - 1
        print(self)
        print("Koniec obiektu o numerze",self.licznik)

    def __str__(self):
        return "Bug number: "+str(self.licznik)+" id: "+str(self.id)


Bugs=[]
for i in range(100):
    Bugs.append(Bug())
    print(Bugs[-1])


