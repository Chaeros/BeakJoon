# https://www.acmicpc.net/problem/9663
# 9663번 N-Qeen , Gold4, 백트래킹
# 2023년 6월 27일

import sys
n=int(sys.stdin.readline())

col=[0]*(n+1)

def promising(pos):
    k=1
    fix=True
    while k<pos and fix:
        if col[k]==col[pos] or abs(col[k]-col[pos])==pos-k:
            fix=False
        k+=1
    return fix

cnt=0
def backTracking(pos):
    global cnt
    if pos==n:
        cnt+=1
        return
    else:
        for i in range(n):
            col[pos] =i
            if promising(pos):
                backTracking(pos+1)

backTracking(0)
print(cnt)