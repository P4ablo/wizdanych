#ZAD 1
plik=open("dane.txt","w+")

lista=[]
for x in range(100):
    if x%4==0:
        lista+=[x]

plik.write(str(lista))
plik.close()
#ZAD 2
plik=open("dane.txt")
liczby = plik.readline()
print(liczby)
#ZAD 3 
with open("zad3.txt", "w") as plik:
    plik.write("Pawel Dabek")
with opne("zad3.txt","r") as plik:
    for linia in plik:
        print(linia,end="")

#ZAD 4 
class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyswietl_produkt(self):
        return self.nazwa_produktu,self.ilosc,self.jednostka_miary,self.cena_jed
    def ile_kosztuje(self):
        return str(self.ilosc*self.cena_jed) + "zl."
    def ile_produktow(self):
        return str(self.ilosc), self.jednostka_miary
    
zakupy = NaZakupy("mleko",2,"szt.",3)
print(zakupy.wyswietl_produkt())
print(zakupy.ile_kosztuje())
print(zakupy.ile_produktow())
 #ZAD 5
class Ciagarytmetcyzny():
    def pobierz_parametry(self):
        self.a1=input()
        self.r=input()
        self.x=input()
        self.tab=[]
        for y in range(int(self.a1),int(self.r)*int(self.x),int(self.r)):
            self.tab.append(y)
        
    def policz_sume(self):
        suma=0
        for y in self.tab:
            suma+=y
        print("Suma elementów ciągu wynosi: {}".format(suma))
    def policz_elementy(self):
        suma=0
        for z in range(len(self.tab)):
            suma+=z
        print("Liczba elementów ciągu wynosi:{}".format(suma))
    def wyswietl_dane(self):
        for elementy in self.tab:
            print(elementy)

ciag = Ciagarytmetcyzny()
ciag.pobierz_parametry()
ciag.policz_sume()
ciag.policz_elementy()
ciag.wyswietl_dane()

    
#ZAD 6
class slowa:
    def __init__ (self, slowo1, slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def czy_palindrom(self):
        if self.slowo1 == self.slowo1[::-1]:
            return "slowo {} jest palindromem".format(self.slowo1)
        return "slowo {} nie jest palindromem".format(self.slowo1)
    def czy_metagramy(self):
        roznica=0
        for i in range(len(self.slowo1)):
            for j in range (len(self.slowo2)):
                if self.slowo1[i]!=self.slowo2[j]:
                    roznica+=1
                i+=1
            if i>=len(self.slowo2):
                break
        if roznica==1:
            return "slowa sa metagramami" 
        return "slowa nie sa metagramami"
    def czy_anagramy(self):
        if(sorted(self.slowo1)==sorted(self.slowo2)):
            print("slowa sa anagramami")
        else:
            print("slowa nie sa anagramami")
s=slowa("kajak","kajak")
print(s.czy_palindrom())
print(s.czy_metagramy())
print(s.czy_anagramy())

      
#ZAD 7 
class Robaczek:
    def __init__(self):
        self.x=0
        self.y=0
        self.krok=1
    def idz_w_gore(self,ile_krokow):
        self.y += ile_krokow * self.krok
        return self.y 
    def idz_w_dol(self,ile_krokow):
        self.y -= ile_krokow * self.krok
        return self.y
    def idz_w_lewo(self,ile_krokow):
        self.x -= ile_krokow * self.krok
        return self.x
    def idz_w_prawo(self,ile_krokow):
        self.x += ile_krokow * self.krok
        return self.x
    def pokaz_gdzie_jestes(self):
        return self.x, self.y
k=Robaczek()
print(k.idz_w_gore(5))
print(k.idz_w_dol(8))
print(k.idz_w_lewo(8))
print(k.idz_w_prawo(8))
print(k.pokaz_gdzie_jestes())

#ZAD 8
class Robaczekv2:
    def __del__(self):
       
        print("bye bye")
    def __init__(self):
        self.x=0
        self.y=0
        self.krok=1
    
    def idz_w_gore(self,ile_krokow):
        self.y += ile_krokow * self.krok
        return self.y 
    def idz_w_dol(self,ile_krokow):
        self.y -= ile_krokow * self.krok
        return self.y
    def idz_w_lewo(self,ile_krokow):
        self.x -= ile_krokow * self.krok
        return self.x
    def idz_w_prawo(self,ile_krokow):
        self.x += ile_krokow * self.krok
        return self.x
    def pokaz_gdzie_jestes(self):
        return self.x, self.y


ruch = Robaczekv2()
del ruch
print(ruch.idz_w_gore(5))
print(ruch.idz_w_dol(8))
print(ruch.idz_w_lewo(8))
print(ruch.idz_w_prawo(8))
print(ruch.pokaz_gdzie_jestes())