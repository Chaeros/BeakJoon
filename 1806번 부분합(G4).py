# https://www.acmicpc.net/problem/1806
# 2023년 06월 23일

import sys

n,s=map(int,sys.stdin.readline().split())

array=list(map(int,sys.stdin.readline().split()))

cnt=0
start=0
end=0
total=0
minimum=int(1e9)
while end!=n:
    if array[end]>=s:
        minimum=1
        break
    if total<s:
        total+=array[end]
        end+=1
        cnt+=1
    else:
        total-=array[start]
        start+=1
        cnt-=1
    if total>=s and cnt<minimum:
        minimum=cnt
    if end==n:
        if minimum==int(1e9):
            minimum=0
            break
        while total>s:
            total -= array[start]
            start += 1
            cnt -= 1
            if total >= s and cnt < minimum:
                minimum = cnt
print(minimum)

# for i in range(n):
#     while total<s:
#         total += array[end]
#         end += 1
#         cnt += 1
#     while total>=s:
#         total -= array[start]
#         start += 1
#         cnt -= 1


# while end!=n:
#     if array[end]>=s:
#         minimum=1
#         break
#     if total<s:
#         total+=array[end]
#         end+=1
#         cnt+=1
#     else:
#         total-=array[start]
#         start+=1
#         cnt-=1
#     if total>=s and cnt<minimum:
#         minimum=cnt
#     if end==n and minimum==int(1e9):
#         minimum=0
# print(minimum)