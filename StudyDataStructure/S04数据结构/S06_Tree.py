'''
    概念：
    深度、高度：树有几层
    度：每个节点有几个子节点
'''

class Node:
    def __init__(self, name, type = 'dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root = Node('/')
        self.now = self.root

    def mkdir(self, name):
        # name 需是已 / 结尾
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != '/':
            name += '/'
        if name == '../':
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError('invalid dir')

tree = FileSystemTree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('usr/')
tree.cd('bin/')
tree.mkdir('Python/')
tree.cd('../')
print(tree.ls())


