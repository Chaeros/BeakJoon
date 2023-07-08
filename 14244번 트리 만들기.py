# https://www.acmicpc.net/problem/14244
# 14244번 트리만들기(S4)
# 2023년 6월 23일

import sys
n,m=map(int,sys.stdin.readline().split())

print(0,1)
for i in range(1,n-m+1):
    print(i,i+1)
if m!=2:
    for i in range(n-m+2,n):
        print(n-m,i)
