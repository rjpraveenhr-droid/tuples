T=()
print(T)

T=tuple()
print(T)

T=(30)
print(T,type(T))
T=(30,)
print(T,type(T))


T=(6,1,8,1,2,9,10)
L=[6,1,8,1,2,9,10]
L[2]=100
print(L)

T=(6,1,8,1,2,9,10)
print(sum(T))
print(max(T))
print(min(T))

t=(5,7,4)
a,b,c=t
print(b)

T=a,b,c
print(T)

L=list(T)

L=[]
for X in T:
    L.append(x)
print(L)

T=(3,30,7,2,4,6,9,90,1,60)
print(T[3])
print(T[-3])
print(T[2:7])

T=(3,30,7,(2,4(6,9)90,1)60)

print(T[3][1])
print(T[3][2][1])