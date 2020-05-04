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
df = pd.read_csv("zamowienia.csv", sep=";")
print(df)

#ZAD 3 a
print(df["Sprzedawca"].unique())

#ZAD 3 b
 print(df.sort_values(('Utarg'), ascending=False).nth(4))

#ZAD 3 c
print(df.groupby('Sprzedawca')['idZamowienia'].count())

#ZAD 3 d
print(df.groupby('Kraj')['idZamowienia'].count())

#ZAD 3 e
print(df(['Kraj' == 'Polska'] & df['Data zamowienia'] >= '2005-01-01') & df['Data zamowienia'] <= '2006-01-01')['idZamowienia'].count()))

#ZAD 3 f
 print(df[df["Data zamowienia"].str.contains("2004")])

#ZAD 3 g
df[df["Data zamowienia"].str.contains("2004")]
            .to_csv("zamowienia_2004.csv", index=False, sep=";")
df[df["Data zamowienia"].str.contains("2005")]
            .to_csv("zamowienia_2005.csv", index=False, sep=";")
