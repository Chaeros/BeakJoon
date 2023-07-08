n=int(input())

array=list(map(int,input().split()))

sum=0

prefixSum=[0] * n

prefixSum[0]=array[0]
for i in range(1,n):
    prefixSum[i]=prefixSum[i-1]+array[i]

sum=0
for i in range(n-1):
    sum+=array[i]*(prefixSum[n-1]-prefixSum[i])

print(sum%1000000007)