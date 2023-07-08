#https://www.acmicpc.net/problem/10025

n,k=map(int,input().split())
position=[0]
inputArray=[0 for i in range(4000001)]

sum=0
ans=0
for i in range(n):
    g,x=map(int,input().split())
    position.append(x)
    inputArray[x]=g

k=2*k+1
for i in range(max(position)+1):
    if i>=k:
        sum-=inputArray[i-k]
    sum+=inputArray[i]
    ans=max(sum,ans)

print(ans)
