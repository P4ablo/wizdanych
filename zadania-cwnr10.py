import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#ZAD 1

x= range(1,21)
y= [1/y for y in x]
plt.plot(x,y, label='f(x)=1/x')
plt.axis([1, len(x), 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(0,21,1))
plt.yticks(np.arange(0,1.1,0.1))
plt.legend()

plt.show()

#ZAD 2

x= range(1,21)
y= [1/y for y in x]
plt.plot(x,y,'g:>',label='f(x)=1/x')
plt.axis([1, len(x), 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(0,21,2.5))
plt.title('Wykres funkcji')
plt.legend()

plt.show()

#ZAD 3

x= np.arange(0,30.1,0.1)
ys= np.sin(x)
yc= np.cos(x)

plt.plot(x,ys,label='sin(x)')
plt.plot(x,yc,label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#ZAD 4

x= np.arange(0,30.1,0.1)
ys= 2+ np.sin(x)
ys2= np.sin(-x)

plt.plot(x,ys,label='sin(x)')
plt.plot(x,ys2,label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sinusa')
plt.legend(loc=6)
plt.show()
#ZAD 5

from sklearn import datasets

iris = datasets.load_iris()
plt.scatter(iris.data[:,0], iris.data[:,1], c=iris.target, s=abs(iris.data[:,0]-iris.data[:,1]))
plt.show()

#ZAD 6

import xlrd
import openpyxl

df= pd.read_excel(pd.ExcelFile("zadanie6/imiona.xlsx"),"Arkusz1")
p=df.groupby(['Plec']).agg({"Liczba":["sum"]})
p2=df.groupby(['Rok']).agg({"Liczba":["sum"]})
ch=df[df["Plec"]=='M'].groupby(['Rok']).sum()
dz=df[df["Plec"]=='K'].groupby(['Rok']).sum()

plt.subplot(1,3,1)
plt.bar(['K','M'],[p.values[0][0],p.values[1][0]],color=['blue','cyan'])
plt.ylabel('Ilość urodzeń')
plt.xlabel('Płeć')
plt.subplot(1,3,2)
plt.plot(df.Rok.unique(),[ch.values[y][0] for y in range(len(ch.values))],"r", label="M")
plt.plot(df.Rok.unique(),[dz.values[y][0] for y in range(len(dz.values))],"g", label="K")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.legend()
plt.subplot(1,3,3)
plt.bar(df.Rok.unique(),[p2.values[y][0] for y in range(len(p2.values))],color="pink")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.show()

#ZAD 7

import xlrd
import openpyxl

df= pd.read_excel(pd.ExcelFile("zadanie7/imiona.xlsx"),"Arkusz1")
ch=df[df["Plec"]=='M'].groupby(['Rok']).sum()
dz=df[df["Plec"]=='K'].groupby(['Rok']).sum()

plt.bar(df.Rok.unique(),[ch.values[y][0] for y in range(len(ch.values))],color="red", label="M")
plt.bar(df.Rok.unique(),[dz.values[y][0] for y in range(len(dz.values))],color="green", label="K",  bottom=[ch.values[y][0] for y in range(len(ch.values))])
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.legend(loc='best')
plt.show()

#ZAD 8

def kostka(n):
    return [(np.random.randint(6)+1)+(np.random.randint(6)+1) for x in range(n)]

lista=kostka(50)
print(lista)
plt.hist(lista, bins=10, facecolor="red", alpha=0.75)
plt.xlabel('Wartości')
plt.ylabel('Rzuty')
plt.grid(True)
plt.show()

#ZAD 9

df= pd.read_csv("zadanie9/zamowienia.csv",header=0,delimiter=";")
p=df.groupby(['Sprzedawca']).agg({"idZamowienia":['count']})
sprzedawcy=p.index.values
zamowienia=[p.values[y][0] for y in range(len(p.values))]
Explode=[0 for i in range(len(p.index.values))]
Explode[5]=0.1

def prepare_label(pct, zam):
    absolute = int(np.ceil(pct / 100. * np.sum(zam)))
    return "{:.1f}% \n({}/{})".format(pct, absolute, sum(zamowienia))

wedges, texts, autotexts = plt.pie(zamowienia, explode=Explode, shadow=True, labels=sprzedawcy,
                                   autopct=lambda pct: prepare_label(pct, zamowienia), textprops=dict(color="black"))
plt.setp(autotexts, size=8, weight="bold", rotation=-45)
plt.legend(title='Sprzedawcy')
plt.show()

#ZAD 10

x= np.arange(0,30.1,0.1)
ys= np.sin(x)
yc= np.cos(x)

fig, ax = plt.subplots()
ax.plot(x,ys,label='sin(x)')
ax.plot(x,yc,label='cos(x)')
ax.annotate('sin(x)=0',
            xy=(0, 0), xycoords='data',
            xytext=(0,-1), textcoords='data',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()

fig, ax = plt.subplots()
x= range(1,21)
y= [1/y for y in x]
line, =ax.plot(x,y, label='f(2)=1/x')
ax.axis([1, len(x), 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(0,21,1))
plt.yticks(np.arange(0,1.1,0.1))
ax.annotate('f(2)=0.5',
            xy=(2, 0.5), xycoords='data',
            xytext=(5,0.8), textcoords='data',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='left', verticalalignment='bottom')
plt.legend()
plt.show()