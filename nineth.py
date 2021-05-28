# zbiornik
# dodawanie to tablicy funkcja append
# sprawdzanie ifem czy index nie jest dluzszy od dlugosci listy


class Zadanie():
    tablica = []
    tablica.append(1)
    tablica.append(2)
    tablica.append(3)

    def __init__(self, newImie, newNazwisko):
        self.imie = newImie
        self.nazwisko = newNazwisko
    def addUser(newUser, self):
        self.tablica.append(newUser)
    def dlugosc(self, ind):
        if len(self.tablica) > ind: 
            return self.tablica(ind)
        
    print(dlugosc(2))