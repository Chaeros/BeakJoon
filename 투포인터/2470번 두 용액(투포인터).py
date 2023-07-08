# https://www.acmicpc.net/problem/2470
# 두 용액 / Gold5
# 2023년 7월 5일
import sys

input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
arr.sort()

start=0
end=N-1
min=int(1e10)
result1=arr[0]
result2=arr[N-1]

while(start<end):
    sum=arr[start]+arr[end]

    if abs(sum)<min:
        min=abs(sum)
        result1=arr[start]
        result2=arr[end]
        if sum==0:
            break

    if sum<0:
        start+=1
    else:
        end-=1

print(result1,result2)
