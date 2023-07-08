# https://www.acmicpc.net/problem/1365
# 꼬인 전깃줄 Gold2
# 2023년 7월 8일
import bisect
import sys

input = sys.stdin.readline

n=int(input())

arr=list(map(int,input().split()))
result=[arr[0]]

for i in range(1,n):
    if result[-1]<arr[i]:
        result.append(arr[i])
    else:
        result[bisect.bisect_left(result,arr[i])]=arr[i]

print(n-len(result))