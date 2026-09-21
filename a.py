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

L=list