import sys

input=sys.stdin.readline

x,y,w,h=map(int,input().split())

list=[x,y,w-x,h-y]

print(min(list))