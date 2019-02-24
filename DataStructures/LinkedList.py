# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:49:59 2019

@author: tgmoore
"""

class Node:
    
    def __init__(self, data=""):
        self.left = None
        self.right = None
        self.data = data
        
    def getData(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def setLeft(self, l):
        self.left = l
        
    def setRight(self, r):
        self.right = r
        
class LinkedList:
    
    def __init__(self, data = "head"):
        self.head = Node(data)
        
    def search(self, data):
        curr = self.head
        while curr and curr.getData() is not data:
            curr = curr.getRight();
        else:
            if curr:
                return curr
        return None            
        
    def getNode(self, index):
        retVal = self.head
        for i in range(0, index):
            retVal = retVal.getRight()            
        return retVal
    
    def getData(self, index):
        retVal = self.head
        for i in range(0, index):
            retVal = retVal.getRight()            
        return retVal.getData()
    
    def addNode(self, data):
        n = Node(data)
        tail = self.head
        while tail.getRight():
            tail = tail.getRight()
        else:
            n.setLeft(tail)
            tail.setRight(n)
            
    def deleteData(self, data):
        curr = self.head
        if curr.getData() is data:
            self.head = self.head.getRight()
        else:
            curr = curr.getRight()
            while curr:
                if curr.getData() is data:
                    if curr.getRight() is not None:
                        curr.getRight().setLeft(curr.getLeft())
                    curr.getLeft.setRight(curr.getRight())
            
    def deleteNode(self, index):
        retVal = self.head
        for i in range(0, index):
            retVal = retVal.getRight()
        if retVal.getRight() is not None:
            retVal.getRight.setLeft(retVal.getLeft())
        retVal.getLeft().setRight(retVal.getRight())
        
