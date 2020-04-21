import numpy as np 
#ZAD 1
a=np.arange(start=2, stop=41, step=2)
print(a)

#ZAD 2 

a = np.array([0.5, 1.3, 2.7])
b = a.astype('int64')
print(a.dtype)
print(a)
print(b.dtype)
print(b)

#ZAD3

def foo(n):
    a=np.arange(start=1,stop=(n*n)+1,step=1)
    print(a)
foo(4)

#ZAD4

def generuj(x, y):
    return np.logspace(1,y,y,base = x)
print(generuj(2,4)

#ZAD5
def diagonalna(n):
    a = np.array([i for i in range(n,0,-1)])
    mat_diag = np.diag([a for a in range(n,0,-1)])
    print( mat_diag)

diagonalna(5)

#ZAD6

words = ['olsztyn','warszawa','krakow','poznan','gdansk','gdynia']
s =[[],[],[],[],[],[]]
for i in range(0,6,1):
    s[i] = np.array(list(words[i]))
    s[i] = np.fromiter(words[i], dtype='U1')
    print(s[i])

#ZAD7

def przekatna(n):
    przekatna=[]
    for i in range(n):
        przekatna.append(2)            
    A = np.diag(przekatna) 
    for a in range(0,n):
        for b in range(0,n):
            for c in range(1,n+1):
                if(a==b+c or b==a+c):  
                    A[a,b]=2*(c+1)    
    return A                
        
print(przekatna(8))

#ZAD8

def ciecie(tab,kierunek):
    if kierunek == 1:
        if len(tab)%2==0:
            print(tab[:len(tab)//2])
            print(tab[2:len(tab)])
    if kierunek == 2:
        if len(tab[0])%2==0:
            pionowa = np.array([[x[0:len(tab) // 2] for x in tab], [x[len(tab) // 2: len(tab)] for x in tab]])
            print(pionowa[0],"\n", pionowa[1])
a = np.array([[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]])
print(ciecie(a,2))

#ZAD 9

def fibbonacci(n):
    result = [1,1]
    for i in range(n-2):
        result.append(result[i] + result[(i + 1)])
    a = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    i = 0
    k = 0
    l = 0
    while i < n:
        if l==5:
            k+=1
            l=0
        a[k][l] = result[i]
        i+=1
        l+=1
        
    return a
print(fibbonacci(10))


