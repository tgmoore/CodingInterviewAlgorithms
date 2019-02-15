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
        
class LinkedList:
    
    def __init__(self, data = "head"):
        self.head = Node(data)
        
    def getNode(self, index):
        retVal = self.head
        for i in range(0, index):
            retVal = retVal.right            
        return retVal
    
    def getData(self, index):
        retVal = self.head
        for i in range(0, index):
            retVal = retVal.right            
        return retVal.getData()
    
    def addNode(self, n):
        tail = self.head
        while tail.right:
            tail = tail.right
        else:
            n.left = tail
            tail.right = n
            
    def deleteNode(self, index):
        retVal = self.head
        for i in range(0, index):
            retVal = retVal.right
        if retVal.right is not None:
            retVal.right.left = retVal.left
        retVal.left.right = retVal.right