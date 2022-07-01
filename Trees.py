### Trees ###

#Recorridos -> Level Order, InOrder (Binarios), PostOrder, Preorder

class BinaryTree():
    def __init__(self):
        self.root = None
    def inOrder(self):
        return self.inOrdert(self.root)
    def inOrdert(self, root):
        order = []
        if root:
            order+=self.inOrdert(root.left)
            order.append(root.key)
            order+=self.inOrdert(root.right)
        return order
    def preOrder(self):
        return self.preOrdert(self.root)
    def preOrdert(self, root):
        order = []
        if root:
            order.append(root.key)
            order+=self.preOrdert(root.left)
            order+=self.preOrdert(root.right)
        return order
    def postOrder(self):
        return self.postOrdert(self.root)
    def postOrdert(self, root):
        order = []
        if root:
            order+=self.postOrdert(root.left)
            order+=self.postOrdert(root.right)
            order.append(root.key)
        return order
    def levelOrder(self):
        r = []
        for i in self.levelOrderT(self.root): r+=i
        return r
    def levelOrderT(self,root):
        r = []
        if root is None:
            return r
        queue = []
        queue.append(root)
        while queue:
            s = len(queue)
            l = []
            while s > 0:
                n = queue.pop(0)
                l.append(n.key)
                s -= 1
                if n.left is not None: queue.append(n.left)
                if n.right is not None: queue.append(n.right)
            r.append(l)
        return r


#ADT -> Árbol de Búsqueda
# Operaciones: Insertar, Eliminar, Buscar por clave (Sin indices,comparaciones)

#BST -> Binary Search tree ->  Árbol de Búsqueda Binaria

class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree(BinaryTree):
    
    def makeEmpty(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    def insert(self,key):
        self.root = self.insert_(key,self.root)
    def insert_(self,key,node):
        if not node: return BSTNode(key)
        elif node.key>key: node.left = self.insert_(key,node.left)
        elif node.key<key: node.right = self.insert_(key,node.right)
        return node
    def contains(self,key):
        return contains_(key,self.root)
    def contains_(self,key,node):
        if not node: return False
        elif node.key<key: return self.contains_(key,node.right)
        elif node.key>key: return self.contains_(key,node.left)
        return True
    def findMin(self):
        if self.isEmpty(): raise Exception('Not Min element in Empty Tree')
        return self.findMin_(self.root).key
    def findMin_(self,node):
        if not node.left: return node
        return self.findMin_(node.left)
    def findMax(self):
        if self.isEmpty(): raise Exception('Not Max element in Empty Tree')
        return self.findMax_(self.root).key
    def findMin_(self,node):
        if not node.right: return node
        return self.findMax_(node.right)
    def remove(self,key):
        if self.isEmpty(): raise Exception('Cannot remove element in Empty list')
        self.root = self.remove_(key,self.root)
    def remove_(self,key,node):
        if not node: return node
        if node.key > key: node.left = self.remove_(key,node.left)
        elif node.key < key: node.right = self.remove_(key,node.right)
        elif node.left and node.right:
            node.key = self.findMin_(node.right).key
            node.right = self.remove_(key,node.right)
        else:
            if node.left: node = node.left
            else: node = node.right
        return node
    def height(self):
        if self.isEmpty(): raise Exception('Not height in Empty Tree')
        return self.height_(self.root)
    def height_(self,node):
        if not node: return -1
        return 1+max(self.height_(node.right),self.height_(node.left))

#BST -> AVL tree ->  Árbol de Búsqueda Binaria Balanceado

class AVLNode(BSTNode):
    def __init__(self,key):
        super().__init__(key)
        self.height = 1

class AVLTree(BinarySearchTree):
    def insert(self,key):
        self.root = self.insert_(self.root,key)
    def insert_(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert_(root.left, key)
        else:
            root.right = self.insert_(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)





