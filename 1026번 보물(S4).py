n=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
C=B
C.sort(reverse=True)

sum=0
for i in range(n):
    sum+=A[i]*C[i]

print(sum)