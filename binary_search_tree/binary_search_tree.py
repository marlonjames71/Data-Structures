# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

    # Insert the given value into the tree
    def insert(self, newValue):
        if newValue < self.value:
            if self.left:
                self.left.insert(newValue)
            else:
                self.left = BinarySearchTree(newValue)
        else:
            if self.right:
                self.right.insert(newValue)
            else:
                self.right = BinarySearchTree(newValue)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        # TODO: Ask why code below didn't pass tests
        # if target < self.value and self.left is not None:
        #     return self.contains(target)
        # elif target > self.value and self.right is not None:
        #     return self.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        myStack = Stack()
        myStack.push(node)
        
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        myQueue = Queue()
        myQueue.enqueue(node)
        while myQueue.size > 0:
            node = myQueue.dequeue()
            print(node.value)
            if node.left:
                myQueue.enqueue(node.left)
            if node.right:
                myQueue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        myStack = Stack()
        myStack.push(node)
        while myStack.size > 0:
            mrNode = myStack.pop()
            print(mrNode)
            if mrNode.left:
                myStack.push(mrNode.left)
            if mrNode.right:
                myStack.push(mrNode.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
