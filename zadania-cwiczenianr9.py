import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ZAD 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

x = df.groupby(["Rok"]).agg({"Liczba": ['count']})
wykres = x.plot()
wykres.set_ylabel('Rok')
wykres.set_xlabel('Liczba')
wykres.legend()
plt.title('Liczba urodzonych dzieci w danym roku')
plt.show()

# ZAD 2

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
l = df.groupby(['Plec']).agg({"Liczba": ['sum']})
wykres = l.plot.bar()
wykres.legend()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Płeć')
plt.title('Suma urodzonych dzieci w latach 2000-2017 z podziałem na płeć')
plt.show()

# ZAD 3 

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
x = (df[((df.Rok >= 2013) & (df.Rok <= 2017))].groupby(['Plec']).agg({'Liczba': ['sum']}))
wykres = x.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title("Suma urodzonych dzieci w latach 2013-2017 z podziałem na płeć")
plt.show()

#ZAD 4-----> Mam problem z tym plikiem, nie ma tam jakby kolumn, z ktorych moge korzystac

#irys=pd.read_csv('iris .data',delimiter=',')
#x=irys['versicolor']
#y=irys['virginica']
#colors = np.random.rand(150)
#plt.scatter(x,y,c=colors)
#plt.show()

#ZAD 5

df = pd.read_csv('zamowienia.csv',sep=";")
grupa = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
wykres = grupa.plot.bar()
wykres.legend()
wykres.set_ylabel('Zamowienia')
wykres.set_xlabel('Sprzedawca')
plt.title('Ilosc zamowien na sprzedawce')
plt.show()

