import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = self

        while current is not None:
            if value < current.value:
                if current.left == None:
                    current.left = BinarySearchTree(value)
                    return
                else:
                    current = current.left
            else: 
                if current.right == None:
                    current.right = BinarySearchTree(value)
                    return
                else:
                    current = current.right
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self

        while current.value != target:
            if target < current.value:
                if current.left == None:                    
                    return False
                else:
                    current = current.left
            else: 
                if current.right == None:
                    return False
                else:
                    current = current.right
        return True

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right != None:
            current = current.right
        return current.value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if node.left:
            self.left.in_order_print(node.left)
        
        print(node.value)
        
        if node.right:
            self.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = []
        q.append(node)

        while len(q) > 0:
            current = q.pop(0)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) > 0:
            current = stack.pop(-1)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            print(current.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        
        if node.left:
            self.left.pre_order_dft(node.left)
        
        if node.right:
            self.right.pre_order_dft(node.right)

    # # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.left.post_order_dft(node.left)
        
        if node.right:
            self.right.post_order_dft(node.right)
        
        print(node.value)
