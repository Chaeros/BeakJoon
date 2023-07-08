# https://www.acmicpc.net/problem/1991
# 1991번 트리 순회 Silver1
# 2023년 6월 23일
import sys

class Node:
    def __init__(self,data,left_node,right_node):
        self.data=data
        self.left_node=left_node
        self.right_node=right_node

nodes={}
def pre_order(node):
    print(node.data,end='')
    if node.left_node!=None:
        pre_order(nodes[node.left_node])
    if node.right_node!=None:
        pre_order(nodes[node.right_node])

def in_order(node):
    if node.left_node!=None:
        in_order(nodes[node.left_node])
    print(node.data,end='')
    if node.right_node!=None:
        in_order(nodes[node.right_node])

def post_order(node):
    if node.left_node != None:
        post_order(nodes[node.left_node])
    if node.right_node != None:
        post_order(nodes[node.right_node])
    print(node.data,end='')

n=int(sys.stdin.readline())
for i in range(n):
    data,left_node,right_node=sys.stdin.readline().split()
    if left_node==".":
        left_node=None
    if right_node==".":
        right_node=None
    nodes[data]=Node(data,left_node,right_node)

pre_order(nodes['A'])
print()
in_order(nodes['A'])
print()
post_order(nodes['A'])