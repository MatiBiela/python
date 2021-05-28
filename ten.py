import pymongo 
import warnings

from pymongo.mongo_client import MongoClient
warnings.filterwarnings("ignore", category=DeprecationWarning) 

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb = myclient["OSOBY"]
myCol = myDb["mieszkancy"]


class ModelOsoba():
    def __init__(self, inImie, inNazwisko, inWiek):
        self.imie = inImie
        self.nazwisko = inNazwisko
        self.wiek = inWiek
    def fillModel(self, osoba):
        self.imie = osoba["imie"]
        self.nazwisko = osoba["nazwisko"]
        self.wiek = osoba["wiek"]

test = ModelOsoba("Maria", "Skłodowska", 45)
# print(test.imie)

class ViewConsole():
    def __init__(self, inModelOSoba):
        self.ModelOsoba = inModelOSoba 
    def showOsoba(self):
        print("Wyświetlona osoba: ")
        print("******************")
        print("Imię: " + self.ModelOsoba.imie)
        print("Nazwisko: " + self.ModelOsoba.nazwisko)
        print("Wiek: " + str(self.ModelOsoba.wiek))
        print("******************")
    def getOsoba(self):
        print("Podaj dane nowej osoby: ")
        print("Podaj imię:")
        self.ModelOsoba.imie = input()
        print("Podaj nazwisko: ")
        self.ModelOsoba.nazwisko = input()
        print("Podaj wiek: ")
        self.ModelOsoba.wiek = input()

class ViewDataBase():
    def __init__(self, inModelOsoba):
        self.ModelOsoba = inModelOsoba
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.myDb = self.myclient["OSOBY"]
        self.myCol = self.myDb["mieszkancy"]
    def showOsoba(self):
        ins =  {
            "Imie":self.ModelOsoba.imie,
            "Nazwisko":self.ModelOsoba.nazwisko,
            "wiek":self.ModelOsoba.wiek
        }
        self.myCol.insert(ins)
    # do poprawki
    def GetOsoba(self):
        query = self.myCol.find()
        if query.count() > 0:
            self.ModelOsoba.imie = query [0]["imie"]
            self.ModelOsoba.nazwisko = query [0]["nazwisko"]
            self.ModelOsoba.wiek = query [0]["wiek"]
            

            

 

class MainController():
    def __init__(self, inModel, inView):
        self.model = inModel
        self.view = inView
    def Init(self):
        self.model = ModelOsoba("Krzychu", "Brzózka", 20)
        self.view.ModelOsoba = self.model
    def Start(self):
        self.view.showOsoba()
    def Get(self, inView):
        self.view.getOsoba()
        # print(self.view.ModelOsoba.imie)
        inView.ModelOsoba = self.view.ModelOsoba
        inView.showOsoba()
    def Stop(self):
        pass
    def GetFromKeyboard(self, inView):
        self.view.getOsoba()
        inView.ModelOsoba = self.view.ModelOsoba
        inView.showOsoba()

class ViewFile():
    def __init__(self, inModelOSoba):
        self.ModelOsoba = inModelOSoba 
    def showOsoba(self):
        inFile = open("plik.txt", mode="w")
        inFile.write("Wyświetlona osoba: " + "\n")
        inFile.write("******************"+ "\n")
        inFile.write("Imię: " + self.ModelOsoba.imie  + "\n")
        inFile.write("Nazwisko: " + self.ModelOsoba.nazwisko+ "\n")
        inFile.write("Wiek: " + str(self.ModelOsoba.wiek)+ "\n")
        inFile.write("******************"+ "\n")
        inFile.close()



cntrl = MainController(None, ViewConsole(None))
cntrl.Init()
# cntrl.Start()
# cntrl.Get(ViewFile(None))
# cntrl.Get(ViewConsole(None))
cntrl.Get(ViewDataBase(None))
# cntrl.Get(ViewDataBase(None))
# cntrl.Get(ViewFile(None))
# cntrl.GetFromKeyboard(ViewDataBase(None))

# md = ModelOsoba("Aldona", "Blada", 45)
# v = ViewConsole(md)
# v.showOsoba()




# query1 = myCol.find({"imie" : "Hans"})
# if query1.count()>0:
#     for x in query1:
#         print(x)
# else: 
#     print("Brak wynikow")

# s="{'wiek' : 45}"
# def extractWiek(param):
#         param= param + " "
#         t= param.split(sep=":")[1]
#         r = t.split(sep="}")[0]
#         return float(r)

# query2 = myCol.find({}, {"_id" : 0, "wiek": 1})
# if query2.count()>0:
#     s = 0 
#     for x in query2:
#         s = s + extractWiek(str(x))
# else: 
#     print("Brak wynikow") 



# print(extractWiek("{'wiek': 45 }"))
# print("Średnia: " + str(s/query2.count()))