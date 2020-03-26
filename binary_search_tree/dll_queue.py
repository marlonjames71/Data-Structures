import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.size = 0
        self.linkedList = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        return self.linkedList.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.linkedList.remove_from_head()
        else:
            return None
            
    def len(self):
        return self.size