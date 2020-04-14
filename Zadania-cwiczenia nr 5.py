#ZAD 1
class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        return self.rodzaj

class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla_kogo,rodzaj,dlugosc,szerokosc):
        Material.__init__(self,rodzaj,dlugosc,szerokosc)
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo
    def wyswietl_dane(self):
        return self.rozmiar, self.kolor, self.dla_kogo,self.rodzaj,self.dlugosc,self.szerokosc
        

class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra,rozmiar,kolor,dla_kogo,dlugosc,szerokosc):
        Ubrania.__init__(self, rozmiar,kolor,dla_kogo,"Sweter",dlugosc,szerokosc)
        self.rodzaj_swetra=rodzaj_swetra
    def wyswietl_dane(self):
        return self.rodzaj_swetra

ub = Ubrania("M","czerwony","damski","koszula","60","50")
print(ub.wyswietl_dane())
print(ub.wyswietl_nazwe())
sw = Sweter("rozsuwany","L","czarny","męski","65","55")
print(sw.wyswietl_dane())
print(sw.wyswietl_nazwe())
#ZAD 2
class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
       
    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
        
    def __add__(self,bok):
        wynik = self.x+bok.x
        return "Nowy bok kwadratu:{}".format(wynik)
kw = Kwadrat(2)
kw2=Kwadrat(4)
kw3= kw+kw2
print(kw3)

#ZAD 3
class Ksztalt:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalt):

    def __init__(self, x):
        self.x =x
        self.y=x
    def __lt__(self,drugi):
        return self.x < drugi.x

    def __le__(self, drugi):
        return self.x<=drugi.x
    
    def __gt__(self,drugi):
        return self.x>drugi.x

    def __ge__(self, drugi):
        return self.x>=drugi.x
        
kw = Kwadrat(4)
kw2 = Kwadrat(7)
print(kw<=kw2)
print(kw>kw2)
print(kw>=kw2)
if kw<kw2:
    print("Zgadza się")
else:
    print("Nieprawda")


#ZAD 4
class Point:
    counter = []

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(8,2)
p2 = Point(9,7)
print(p1.counter)
p2.update(4)
print(p2.counter)
print(p1.counter)
for i in range(5):
    p1.update(i)
print(p1.counter)
print(p2.counter)

#ZAD 5
class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(isinstance("adrian", Menadzer))
print(isinstance("jozek",Pracownik))

print(issubclass(Menadzer,Pracownik))



print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())

#ZAD 6
class Wspak:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

wspak = Wspak("emilia")
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())

print("\n")

wspak2=Wspak("dom")
print(wspak2.__next__())
print(wspak2.__next__())
print(wspak2.__next__())
print("\n")

for i in Wspak("kwarantanna"):
    print(i)


#ZAD 7
class Parzyste:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration
        if self.index % 2 == 0:
            value = self.data[self.index]
            self.index += 2
            print(value)
moj_iter = Parzyste([1,3,6,2,9,18])
for element in moj_iter:
    element

#ZAD 8
class Samogloska:
    
    def __init__(self,data):
        self.data=data
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration
        if self.data[self.index] in ("a","e","i","o","u","y"):
            print(self.data[self.index])
        self.index+=1


s=Samogloska("samochod")
s.__next__()
s.__next__()
s.__next__()
s.__next__()
s.__next__()
s.__next__()
s.__next__()
s.__next__()
s.__next__()
s.__next__()
s.__next__()

print("\n\n")

s2=Samogloska("warszawa")

for i in s2:
    i
#ZAD 9
def samogloska(data):
    for i in data:
         if i in ("a","e","i","o","u","y"):
             yield i


s = samogloska("komputer")
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
#ZAD 10
import itertools

liczby = [1,2,3,4,5,6,7,8,9,10]

wynik = itertools.combinations(liczby,3)

for item in wynik:
    print(item)
#ZAD 11
def gen_fib():
    a,b = 1,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b
g = gen_fib()
fibo = [next(g) for _ in range(10)] 
print(fibo)
#ZAD 12
import itertools

miesiace = ["Styczen","Luty","Marzec","Kwiecien","Maj","Czerwiec","Lipiec","Sierpien","Wrzesien","Pazdziernik","Listopad","Grudzien"]

daily_data = list(itertools.zip_longest(range(1,13), miesiace))

print(daily_data)
