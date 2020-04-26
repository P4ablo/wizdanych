import numpy as np 
#ZAD 1
a = np.array( [20,30,40] )
b = np.array( [10,20,30] )
print(a*b)
#ZAD 2
A = np.array([[3,4,5], [1,2,3], [4,5,6]])
B = np.array([[-2, 5,1,5], [7, 0, 2,1], [-1, 0,5,3],[8,3,0,1]])
print(A.min(axis=1))
print(B.min(axis=1))
#ZAD 3
a = np.array( [20,30,40] )
b = np.array( [10,20,30] )
print(np.dot(a,b))
#ZAD 4
a=np.array([2,3,4])
b=np.array([1.2,4.7,2.1])
print(a*b)

#ZAD 5
C = np.array([[2,8,6],[10,1,3]])
a=np.sin(C)
print(a)

#ZAD 6
D = np.array([[1,5,2],[98,45,0]])
b=np.cos(D)
print(b)

#ZAD 7
C = np.array([[2,8,6],[10,1,3]])
a=np.sin(C)
D = np.array([[1,5,2],[98,45,0]])
b=np.cos(D)
print(a+b)

#ZAD 8
a=np.arange(9).reshape(3,3)
for b in a:
    print(b)

#ZAD 9
b = np.arange(9).reshape(3,3)
for a in b.flat:
   print(a)

#ZAD 10
a=np.arange(81).reshape(9,9)
print(a)
print(a.shape)
b=a.reshape(3,27)
print(b)
print(b.shape)
c=b.reshape(27,3)
print(c)
print(c.shape)
d=b.T
print(d)
print(d.shape)
#Możemy zmieniać kształt macierzy tylko wtedy,gdy iloczyn kolumn i wierszy będzie taki sam np. 9*9=81 i 3*27=81

#ZAD 11
a=np.arange(12)
print(a)
b=a.reshape(3,4)
c=b.ravel()
print(c)
d=a.reshape(4,3)
print(d.ravel())
e=a.reshape(2,6)
print(e.ravel())




