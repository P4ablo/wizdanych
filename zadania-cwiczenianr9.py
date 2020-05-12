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

#ZAD 4

df = pd.read_csv("iris.data", sep=",", names=[
                 "sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])
l= df[['sepal length in cm','sepal width in cm','class']]

x1 = l[l['class']=='Iris-setosa']['sepal length in cm']
x2 = l[l['class']=='Iris-versicolor']['sepal length in cm']
x3 = l[l['class']=='Iris-virginica']['sepal length in cm']

y = l[l['class']=='Iris-setosa']['sepal width in cm']

plt.scatter(x1,y, c='r')
plt.scatter(x2,y, c='b')
plt.scatter(x3,y, c='g')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()

#ZAD 5

df = pd.read_csv('zamowienia.csv',sep=";")
grupa = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
wykres = grupa.plot.bar()
wykres.legend()
wykres.set_ylabel('Zamowienia')
wykres.set_xlabel('Sprzedawca')
plt.title('Ilosc zamowien na sprzedawce')
plt.show()
