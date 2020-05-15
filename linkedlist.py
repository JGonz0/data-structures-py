#!/usr/bin/env python3

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_node(self):
        return self.data
    
    def set_node(self,data):
        self.data = data
        return
    
    def get_next(self):
        return self.next
    
    def set_next(self, node):
        self.next = node
        return
    
class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def add(self,data):
        new_node = LinkedNode(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        return
    
    def node_add(self,node):
        if type(node) is type(LinkedNode(1)):
            if self.head is None:
                self.head = node
                return
            
            current_node = self.head
            while True:
                if current_node.next is None:
                    current_node.next = node
                    return
                current_node = current_node.next
        else:
            print("Operacion invalida")
    
    def display(self):
        current_node = self.head
        while current_node is not None:
            print("%d -> " % current_node.data, end='')
            current_node = current_node.next
        print("None")
        return
    
    def len(self):
        current_node = self.head
        leng = 0
        while True:
            if current_node is None:
                return leng
            current_node = current_node.next
            leng += 1
    
    def insertion(self,data,idx):
        if idx > self.len():
            print("Indice fuera de limites")
            return
        
        new_node = LinkedNode(data)
        if idx == 0:
            aux_node = self.head
            self.head = new_node
            self.head.next = aux_node
            return
        
        current_node = self.head
        current_idx = 0
        while True:
            if current_idx == idx - 1:
                aux_node = current_node.next
                current_node.next = new_node
                new_node.next = aux_node
                return
            current_node = current_node.next
            current_idx += 1
    
    def remover(self,idx):
        if idx > self.len() - 1:
            print("Indice fuera de limites")
            return
        
        if idx == 0:
            self.head = self.head.next
            return
        
        current_node = self.head
        current_idx = 0
        while True:
            if current_idx == idx-1:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            current_idx += 1

if __name__ == '__main__':
    
    link = LinkedList()
    n1 = LinkedNode(5)
    n2 = LinkedNode(49)
    n3 = LinkedNode(30)

    n1.next = n2
    n2.next = n3

    n3.set_next(LinkedNode(20))

    link.node_add(n1)
    link.display()