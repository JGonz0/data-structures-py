#!/usr/bin/env python3

class DLinkedNode:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def get_node(self):
        return self.data
    
    def set_node(self,data):
        self.data = data
        return

    def get_next(self):
        return self.next
    
    def set_next(self,node):
        node.prev = self
        self.next = node
        return
    
    def get_prev(self):
        return self.prev
    
    def set_prev(self,node):
        node.next = self
        self.prev = node
        return

class DLinkedList:

    def __init__(self,head=None):
        self.head = head
    
    def add(self,data):
        new_node = DLinkedNode(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        new_node.prev = current_node
        current_node.next = new_node
        return
    
    def node_add(self,node):
        if type(node) is type(DLinkedNode(1)):
            if self.head is None:
                self.head = node
                return
            
            current_node = self.head
            while True:
                if current_node.next is None:
                    node.prev = current_node
                    current_node.next = node
                    return
                current_node = current_node.next
        else:
            print("Invalid action")

    def len(self):
        current_node = self.head
        leng = 0
        while current_node is not None:
            leng += 1
            current_node = current_node.next
        return leng

    def remover(self,idx):
        if idx > self.len() - 1:
            print("Index out of bounds")
            return

        if idx == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        current_node = self.head
        current_idx = 0

        while True:
            if current_idx == idx:
                if idx == self.len() -1:
                    current_node = current_node.prev
                    current_node.next = None
                    return
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                return
            current_idx += 1
            current_node = current_node.next

    def insertion(self,idx,data):
        if idx > self.len():
            print("Index out of bounds")
            return
        
        new_node = DLinkedNode(data)
        current_node = self.head
        current_idx = 0

        if idx == 0:
            aux_node = self.head
            self.head = new_node
            self.head.next = aux_node
            aux_node.prev = self.head
            return

        while True:
            if current_idx == idx - 1:
                aux_node = current_node.next
                current_node.next = new_node
                new_node.prev = current_node
                new_node.next = aux_node
                if aux_node is None:
                    return
                aux_node.prev = new_node
                return
            current_idx += 1
            current_node = current_node.next 

    def display(self):
        if self.head is not None:
            print("None <-> ", end='')
        current_node = self.head
        while current_node is not None:
            print("%s <-> " % current_node.data, end='')
            current_node = current_node.next
        print("None")
        return
    

if __name__ == '__main__':

    DLink = DLinkedList()
    n1 = DLinkedNode(10)
    n2 = DLinkedNode(20)
    n3 = DLinkedNode(30)

    n1.set_next(n2)
    n2.set_next(n3)

    DLink.node_add(n1)
    DLink.insertion(1,35)
    DLink.display()
