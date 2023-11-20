'''
自平衡二叉搜索树
性质：1、根的左右子树的高度差的绝对值不大于1
2、根的左右子树都是二叉树

AVL插入：左旋、右旋、右旋-左旋

bf:平衡参数，下沉为-1，平衡为0，上升为1
'''
from S06_Tree_BSTree import BiTree, BST
class AVLNode(BiTree):
    def __init__(self, data):
        BiTree.__init__(self, data)
        self.bf = 0 # 高度差

class AVLTree(BST):
    def __init__(self, nums=None):
        BST.__init__(self, nums) # 沿用父类BST的初始化方法

    def rotate_left(self, p, c): # 左旋
        s2 = c.left
        p.right = s2
        if s2:
            s2.parent = p
        c.left = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.right
        p.left = s2
        if s2:
            s2.parent = p
        c.right = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c): # 先右旋再左旋
        g = c.left

        s3 = g.right
        c.left = s3
        if s3:
            s3.parent = c
        g.right = c
        c.parent = g

        s2 = g.left
        p.right = s2
        if s2:
            s2.parent = p
        g.left = p
        p.parent = g

        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def rotate_left_right(self, p, c): # 先左旋再右旋
        g = c.right

        s2 = g.left
        c.right = s2
        if s2:
            s2.parent = c
        g.left = c
        c.parent = g

        s3 = g.right
        p.left = s3
        if s3:
            s3.parent = p
        g.right = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def insert_no_rec(self, val):
        # 1、和BST一样，插入
        p = self.root
        if not p:  # 空树时的处理
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.left:  # 存在左子树,则继续遍历左子树
                    p = p.left
                else:  # 左子树不存在
                    p.left = AVLNode(val)
                    p.left.parent = p
                    node = p.left # node存储插入节点
                    break

            elif val > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = AVLNode(val)
                    p.right.parent = p
                    node = p.right
                    break

            else: # val == p.adata
                return

        # 2、 更新
        while node.parent:
            if node.parent.left == node: #传递从左子树来，左子树更陈了
                # 更新node.parent的bf
                if node.parent.bf < 0: # 原来node.parent.bf == -1 ，更新后为2
                    # 看node哪边沉
                    g = node.parent.parent # 为了连接旋转之后的子树
                    x = node.parent # 旋转前的子树的根
                    if node.bf > 0: # 左边沉
                        n = self.rotate_left_right(node.parent, node)
                    else: #右边沉
                        n = self.rotate_right(node.parent, node)
                    # 把n和g连起来
                elif node.parent.bf > 0: # 原来等于1，现在等于0
                    node.parent.bf = 0
                    break
                else: # 原来等于0，现在-1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else: # 传递从右子树来，右子树更沉了
                if node.parent.bf > 0: # 原本等于1， 现在2
                    # 旋转，看哪边沉
                    g = node.parent.parent
                    x = node.parent  # 旋转前的子树的根
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                    # 记得连起来 n g
                elif node.parent.bf < 0: # 原来-1， 现在0
                    node.parent.bf = 0
                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 连接旋转后的子树
            n.parent = g
            if g :
                if x == g.left:
                    g.left = n
                else:
                    g.right = n
                break
            else:
                self.root = n
                break

tree = AVLTree([9, 8, 7, 6, 5, 4, 3, 2, 1])
tree.pre_order(tree.root)
print('')
tree.in_order(tree.root)
