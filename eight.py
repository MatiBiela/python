class Rodzic:
    def __init__(nlf, newImie, newNazwisko):
        nlf.imie = newImie
        nlf.nazwisko = newNazwisko
    def toString(nlf):
        return nlf.imie + " " + nlf.nazwisko


class Dziecko(Rodzic):
    def __init__(nlf, newImie, newNazwisko):
        nlf.imie = newImie
        nlf.nazwisko = newNazwisko

r = Rodzic("Alden", "Praktyczny")
d = Dziecko("Eliza", "Blada")
print(r.toString())
print(d.toString())

from abc import ABC 
from abc import abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def getArea(self):
        pass

class Rectangle(Shape):
    def getArea(self):
        return 5*5

class Circle(Shape):
    def getArea(self):
        return 3.14*(5**2)

class CreatorShape:
    def getInstance(self, type):
        if(type=="Circle"):
            return Circle()
        elif(type=="Rectangle"):
            return Rectangle()
        else:
            return None

s = CreatorShape()
print(s.getInstance("Rectangle").getArea())
