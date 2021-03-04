#!/usr/bin/env python3

import random

class Node():
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, data: int = None, node: Node = None):
        if (node): self.root = node
        elif (data): self.root = Node(data)
        else: self.root = None

    def inorder_traversal(self, node: Node = 0):
        if (node == 0): node = self.root

        if node.left: self.inorder_traversal(node.left)
        print(node.data, end=" ")
        if (node.right): self.inorder_traversal(node.right)

    def postorder_traversal(self, node: Node = 0):
        if (node == 0): node = self.root

        if (node.left): self.postorder_traversal(node.left)
        if (node.right): self.postorder_traversal(node.right)
        print(node.data, end=" ")

    def height(self, node: Node = 0):
        if (node == 0): node = self.root
        hleft, hright = 0, 0

        if (node.left): hleft = self.height(node.left)
        if (node.right): hright = self.height(node.right)

        if hright > hleft: return hright + 1
        else: return hleft + 1

    def levelorder_traversal(self, node: Node = 0):
        if (node == 0): node = self.root

        queue = []
        queue.append(node)

        while (len(queue)):
            node = queue.pop(0)
            if (node.left): queue.append(node.left)
            if(node.right): queue.append(node.right)
            print(node.data, end=" ")

    def min(self, node: Node = 0):
        if (node == 0): node = self.root
        while (node.left): node = node.left

        return node.data

    def max(self, node: Node = 0):
        if (node == 0): node = self.root
        while (node.right): node = node.right

        return node.data

    def remove(self, data: int, node: Node = 0):
        if (node == 0): node = self.root

        if (node is None): return node
        if (data < node.data): node.left = self.remove(data, node.left)
        elif (data > node.data): node.right = self.remove(data, node.right)
        else:
            if (node.left is None): return node.right
            elif (node.right is None): return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)

        return node

class BinarySearchTree(BinaryTree):
    def add(self, data: int):
        parent = None
        node = self.root

        while (node):
            parent = node

            if (data < node.data): node = node.left
            else: node = node.right

        if (parent is None): self.root = Node(data)
        elif (data < parent.data): parent.left = Node(data)
        else: parent.right = Node(data)

    def search(self, data: int, current: Node = 0):
        if (current == 0): current = self.root
        if (current is None): return current
        if (current.data == data): return BinarySearchTree(node = current)

        if (current.data > data): return self.search(data, current.left)
        return self.search(data, current.right)

def main():
    #  tree = BinaryTree(7)
    #  root = tree.root

    #  root.left = Node(10)
    #  root.right = Node(20)
    #  root.right.left = Node(30)

    #  tree.inorder_traversal()
    #  tree.postorder_traversal()
    #  print(f"height: {tree.height()}")

    #  ------------------------------

    #  random.seed(7)
    #  items = random.sample(range(1, 1000), 10)

    items = [ 7, 3, 20, 2, 5, 30 ]

    search_btree = BinarySearchTree()
    for item in items: search_btree.add(item)
    search_btree.inorder_traversal()

    #  print("[+] SEARCHING", end="\n")

    #  search_items = [ 7, 405, 332, 971 ]

    #  for item in search_items:
        #  res = search_btree.search(item)

        #  if (res is None): print(f"{item}: not found")
        #  else: print(f"[+] {res.root.data}")

    #  ------------------------------

    print("\n[+] LEVELS", end="\n")
    search_btree.levelorder_traversal()

    #  print(f"min: {search_btree.min()}")
    #  print(f"max: {search_btree.max()}")

    print("\n[+] REMOVING", end="\n")
    search_btree.remove(3)
    search_btree.inorder_traversal()
    print("\n[+] LEVELS", end="\n")
    search_btree.levelorder_traversal()
    print(f"\nmin: {search_btree.min()}")

if __name__ == "__main__":
    main()
