# https://www.acmicpc.net/problem/17266
# 알고리즘 : 라인 스위핑

import sys

input=sys.stdin.readline

N=int(input())
M=int(input())

pos=list(map(int,input().split()))

start=0
end=pos[0]
distance=end-start
pos.pop(0)

for i in pos:
    start=end
    end=i

    if (end-start)%2==1:
        if distance<int((end-start)/2)+1:
            distance=int((end-start)/2)+1
    else:
        if distance<int((end-start)/2):
            distance=int((end-start)/2)


if distance<N-end:
    distance=N-end

print(distance)