import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.linkedList = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.linkedList.add_to_tail(value)

    def pop(self):
        self.size -= 1
        self.linkedList.remove_from_tail()

    def len(self):
        return self.size
