#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.data) + " - "
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.data) + " - "
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += str(start.data) + " - "
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type == 'preorder':
            print(self.preorder_print(self.root, ''))
        elif traversal_type == 'inorder':
            print(self.inorder_print(self.root, ''))
        elif traversal_type == 'postorder':
            print(self.postorder_print(self.root, ''))
        else:
            print("Traversal type: " + str(traversal_type) + " not defined")
            return

#           5
#       10      20
#   30    40  50    60

tree = BinaryTree(5)
tree.root.left = Node(10)
tree.root.right = Node(20)
tree.root.left.left = Node(30)
tree.root.left.right = Node(40)
tree.root.right.left = Node(50)
tree.root.right.right = Node(60)

tree.print_tree('preorder')
tree.print_tree('inorder')
tree.print_tree('postorder')