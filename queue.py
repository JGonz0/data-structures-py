#!/usr/bin/env python3

class UniqueQueue:

    def __init__(self):
        self.queue = []
        self._set = set()
    
    def add(self,data):
        if data in self._set:
            print("Data already in the queue")
            return
        self.queue.insert(0,data)
        self._set.add(data)
    
    def remove(self):
        if self.queue == []:
            print("Nothing to remove")
            return
        return self.queue.pop()
    
    def queue_size(self):
        leng = 0
        for _ in self.queue:
            leng +=1
        return leng
    
    def graphic_print(self):
        for i in range(len(self.queue)):
            if i == 0:
                print("[ Last Item ]")
            print("-> %s" %self.queue[i])
            if i == len(self.queue) - 1:
                print("[ First Item ]")
        return

class Queue:

    def __init__(self):
        self.queue = []
    
    def add(self,data):
        self.queue.append(data)
        return
    
    def remove(self):
        if self.queue == []:
            print("Nothing to remove")
            return
        return self.queue.pop()
    
    def queue_size(self):
        leng = 0
        for _ in self.queue:
            leng +=1
        return leng
    
    def graphic_print(self):
        for i in range(len(self.queue)):
            if i == 0:
                print("[ Last Item ]")
            print("-> %s" %self.queue[i])
            if i == len(self.queue) - 1:
                print("[ First Item ]")
        return


if __name__ == '__main__':

    Uqueue = UniqueQueue()
    Uqueue.add(5)
    Uqueue.add(8)
    Uqueue.add(12)
    Uqueue.add(15)
    Uqueue.remove()
    Uqueue.graphic_print()
