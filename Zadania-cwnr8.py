import numpy as np
import pandas as pd
import xlrd
import openpyxl

#ZAD 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
print(df)

#ZAD 2 a
print(df[df['Liczba'] > 1000])
#ZAD 2 b
print(df[df['Imie'] == 'PAWEŁ'])
#ZAD 2 c
print(df.agg({'Liczba':['sum']}))
#ZAD 2 d
print(df[df['Rok'] < 2006].agg({'Liczba': ['sum']}))
#ZAD 2 e
print(df[df['Plec'] == 'M'].agg({'Liczba': ['sum']}))
print(df[df['Plec'] == 'K'].agg({'Liczba': ['sum']}))
#ZAD 2 f
dfdrugi = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(dfdrugi, start=1):
    print(f"{index} {group[0]}")
    print(f"{group[1].iloc[0]['Imie']}", end=' ')
    print(f"{group[1].iloc[0]['Liczba']}")
#ZAD 2 g
print(df.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']})
        .sort_values(('Liczba', 'sum'), ascending=False).iloc[[0, 1]])


#ZAD 3
df = pd.read_csv('zamowienia.csv',sep=";")
#ZAD 3 a
print(df["Sprzedawca"].unique())
#ZAD 3 b
print(df.sort_values(by="Utarg").tail(5))
#ZAD 3 c
print(df.groupby(["Sprzedawca"]).agg({"idZamowienia": ['count']}))
#ZAD 3 d
print(df.groupby(["Kraj"]).agg({"idZamowienia": ['count']}))
#ZAD 3 e
suma=(df[((df.Kraj == "Polska") & (df.DataZamowienia>"2004-12-31") & (df.DataZamowienia<"2006-01-01"))].agg({"idZamowienia": ['count']}))
print(suma)
#ZAD 3 f
sredni=(df[((df.DataZamowienia>"2003-12-31") & (df.DataZamowienia<"2005-01-01"))].agg({"Utarg": ['average']}))
print(sredni)
#ZAD 3 g
plik = open("Zamowienia_2015.csv","w+")
plik.write(str(suma))
plik.close()
plik2 = open("Zamowienia_2014.csv","w+")
plik2.write(str(sredni))
plik2.close()
