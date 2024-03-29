#!/usr/bin/env python3

class UniqueStack:

    def __init__(self):
        self.stack = []
        self._set = set()
    
    def push(self,data):
        if data not in self._set:
            self.stack.append(data)
            self._set.add(data)
            return
        print("Error: Duplicated data in the stack")
        return
    
    def pop(self):
        if self.stack == []:
            print("Stack is empty")
            return
        return self.stack.pop()

    def graphic_print(self):
        rev_stack = self.stack[::-1]
        for i in range(len(rev_stack)):
            if i == 0:
                print("[ Last Item ]")
            print("-> %s" %rev_stack[i])
            if i == len(rev_stack) - 1:
                print("[ First Item ]")
        return

    def peek(self):
        return self.stack[-1]

    def show(self):
        print(self.stack)
        return
    
    def stack_size(self):
        leng = 0
        for _ in self.stack:
            leng += 1
        return leng

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)
        return
    
    def pop(self):
        if self.stack == []:
            print("Stack is empty")
            return
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def graphic_print(self):
        rev_stack = self.stack[::-1]
        for i in range(len(rev_stack)):
            if i == 0:
                print("[ Last Item ]")
            print("-> %s" %rev_stack[i])
            if i == len(rev_stack) - 1:
                print("[ First Item ]")
        return
    
    def show(self):
        print(self.stack)
        return
    
    def replicate(self, times):
        if times < 0:
            print("Invalid number of times")
            return
        dup = self.pop()
        for _ in range(times):
            self.push(dup)
        return
    
    def stack_size(self):
        leng = 0
        for _ in self.stack:
            leng += 1
        return leng

if __name__ == '__main__':

    UVstack = UniqueStack()
    UVstack.push(10)
    UVstack.push('Foo')
    UVstack.push('30.45')
    UVstack.pop()
    UVstack.graphic_print()

    print("\n")

    Astack = Stack()
    Astack.push(5)
    Astack.push(5)
    Astack.push(7)
    Astack.replicate(3)
    Astack.graphic_print()

