# https://www.acmicpc.net/problem/9934
# 9934번 완전 이진 트리(Silver1)

import sys

k=int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split()))

layer=[[] for _ in range(k+1)]
for n in range(k,0,-1):
    i=0
    while 2**(k-n)+i*(2**(k-n+1))<2**k:
        layer[n].append(array[2**(k-n)+i*(2**(k-n+1))-1])
        i+=1

for i in range(1,k+1):
    for value in layer[i]:
        print(value,end=' ')
    print()