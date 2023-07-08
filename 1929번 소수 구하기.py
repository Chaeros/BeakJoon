import math

m,n=map(int,input().split())

array=[1]*(n+1)
array[1]=0

for i in range(2,int(math.sqrt(n))+1):
    j=2
    while i*j<=n:
        array[i*j]=0
        j+=1

for i in range(m,n+1):
    if array[i]==1:
        print(i)