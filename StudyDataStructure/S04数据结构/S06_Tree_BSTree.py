'''
二叉搜索树：在二叉树的基础上，每个根节点的左节点比根节点小，右节点比根节点大
'''
import random

class BiTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self, nums=None):
        self.root = None
        if nums: # 非递归插入
            for num in nums:
                self.insert_no_rec(num)
        # if nums: # 递归插入
        #     for num in nums:
        #         self.insert(self.root, num)

    # 递归插入
    def insert(self, node, val):
        if not self.root: # node为空说明没有树，则创建树
            node = BiTree(val)
        elif val < node.data:
            node.left = self.insert(node.left, val)
            node.left.parent = node
        elif val > node.data:
            node.right = self.insert(node.right, val)
            node.right.parent = node
        return node

    # 非递归插入
    def insert_no_rec(self, val):# 非递归版本
        p = self.root
        if not p: # 空树时的处理
            self.root = BiTree(val)
            return
        while p:
            if val < p.data:
                if p.left: # 存在左子树,则继续遍历左子树
                    p = p.left
                else:  # 左子树不存在
                    p.left = BiTree(val)
                    p.left.parent = p
                    return
            elif val > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = BiTree(val)
                    p.right.parent = p
                    return
            else:
                return

    # 查找
    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.right, val)
        elif node.data > val:
            return self.query(node.left, val)
        else:
            return node

    # 非递归查找
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.right
            elif p.data > val:
                p = p.left
            else:
                return p
        return None

    # 删除
    def __remove_node_1(self, node):
        # 情况1， node是叶子节点
        if not node.parent: # 是否为根节点
            self.root = None
        if node == node.parent.left: # 如果节点为左节点
            node.parent.left = None
        else :
            node.parent.right = None

    def __remove_node_21(self, node):
        # 情况2：node只有一个左孩子
        if not node.parent: #判断是否为根节点
            self.root = node.left
            node.left.parent = None
        elif node == node.parent.left: # node为父节点的左孩子
            node.parent.left = node.left
            node.left.parent = node.parent
        else: # node为父节点的右孩子
            node.parent.right = node.left
            node.left.parent = node.parent

    def __remove_node_22(self, node):
        # 只有一个右孩子
        if not node.parent:
            self.root = node.right
            node.right.parent = None
        elif node == node.parent.left:
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent

    def delete(self, val):
        if self.root: # 不是空树
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.left and not node.right:# 情况1
                self.__remove_node_1(node)
            elif not node.right: # 情况2.1
                self.__remove_node_21(node)
            elif not node.left: # 情况2.2
                self.__remove_node_22(node)
            else: # 情况3 有左右孩子
                '''
                有左右孩子的时候，删除node需要重新构建树
                将右子树的最小节点替换node
                '''
                min_node = node.right
                # 在右子树中找min取代node，或左子树中找max取代
                while min_node.left:
                    min_node = min_node.left
                node.data = min_node.data
                # 删除min_node
                if min_node.right:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


    # 先序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.left)
            self.pre_order(root.right)

    # 中序遍历
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data, end=',')
            self.in_order(root.right)

    # 后序遍历
    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=',')

print('插入')
nums = list(range(0, 20, 2))
random.shuffle(nums)
print(f'原数组:{nums}')
tree = BST(nums)
print('先序遍历:')
tree.pre_order(tree.root)
print('\n中序遍历:')
tree.in_order(tree.root)
print('\n后序遍历:')
tree.post_order(tree.root)
print('\n查询')
print(tree.query_no_rec(4).data)
print(tree.query(tree.root, 4).data)
tree.query(tree.root, 5)
# print('删除')
# tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
# tree.in_order(tree.root)
# print('')
# tree.delete(4)
# tree.in_order(tree.root)