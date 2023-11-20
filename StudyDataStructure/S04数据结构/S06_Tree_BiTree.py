'''
二叉树：所有节点的度为2的树
'''
from collections import *

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

root = e
e.left = a
e.right = g
a.right = c
c.left = b
c.right = d
g.right = f

# 先序遍历
def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.left)
        pre_order(root.right)

# 中序遍历
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=',')
        in_order(root.right)

def in_order_not_rec(root):
    stack =[]
    p = root
    while p or not stack:
        if p:
            pass


# 后序遍历
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=',')

# 层序遍历
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

pre_order(root)
print('\n---')
in_order(root)
print('\n---')
post_order(root)
print('\n---')
level_order(root)
