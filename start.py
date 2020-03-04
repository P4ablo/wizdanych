#print("Hello world!")

a = 5
#print(type(a))

imie = "Ala"
imie = """Ala
ma kota
Filemona"""
#print(imie)

#def funkcje():
#   """ docstring """
#    pass

#imie = 6.3
#print(imie)
#print(type(imie)

#liczba = str(5)
#liczba = int("5")
#liczba = int("5.5")

imie="ala"
#print(imie.capitalize())
imie=imie.capitalize()
#print(imie)

#print(imie[0])
#print("ala".capitalize().count("A"))

#print(imie+imie)

#print(5+imie) blad
#-------------------------------------------------------------------

#FORMATOWANIE WYJSCIA

#print("Ala ma 5 lat")
#print(imie+"ma"+str(5)+"lat")
#print("{} ma {} lat".format(imie,5))
#print("{0} ma {1} lat".format(imie,5))
wiek = 5
#print(f"{imie} ma {wiek} lat")
#---------------------------------------------------------------------

##LISTY

lista = []
lista = [1, 3, 4, "Ala", 4.5, imie]
lista = [1, 3, 4, "Ala", 4.5, imie, [1, 2]]
lista[0]
#print(lista[5][1]) ---->lista dwupoziomowa

lista.append(3)
lista[0] = 10

lista2 = lista + lista
#print(lista2)
#--------------------------------------------------------------------

#SLOWNIK

slownik = {}
slownik = {"imie": "Marek", 
"wiek":35}
#print(slownik)

slownik["imie"] #----------->wybieranie rzeczy ze slownika
#print(slownik.items())
#---------------------------------------------------------------------

#IMPORT

#from math import *
#import math as m ------->better option

 
