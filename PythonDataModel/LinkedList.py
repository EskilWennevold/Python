from hashlib import new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self):
        return f'The variable {self.data} , {self.next}'

class LinkedList:
    def __init__(self):
        self.head = Node('Genesis  Block')
    
    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self):
        return f'The variable {self.head}'
    
    def __add__(self, list):
        if self.head.next == None:
            self.head.next = list.head
        else:
            node = self.head.next
            while node !=  None:
                node = node.next
            node.next = list.head