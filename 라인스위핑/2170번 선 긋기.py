# https://www.acmicpc.net/problem/2170
# 선 긋기 (Gold5)
# 2023년 7월 2일
import sys

input=sys.stdin.readline

n=int(input())

line=[]
for i in range(n):
    a,b=map(int,input().split())
    line.append((a,b))

line.sort()

start=line[0][0]
end=line[0][1]
sum=0

for i in line:
    if end<i[0]:
        sum+=end-start
        start=i[0]
        end=i[1]
    else:
        if end<i[1]:
            end=i[1]
sum+=end-start

print(sum)
