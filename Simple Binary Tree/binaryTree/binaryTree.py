# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 21:21:12 2017

@author: 1
"""
class Node:
    def __init__(self, value):
        self.left=None
        self.right=None
        self.value=value
        
        
    def __str__(self):        
        return str(self.value)
        
        
class Tree:
    def __init__(self):
        self.root=None
        self.size=0
        
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def __call_(self,value):
        self.add(value)
        print('Value '+str(value)+' was added')

        
    def GetRoot(self):
        return self.root
    
    def add(self,value):
      if self.root is None:
          self.root=Node(value)
          self.size=1
      else: 
          self._add(value,self.root)
          print('Value '+str(value)+' was added')
      
      
    def _add(self, value, node):
        
        if (value<node.value):
            if (node.left is not None):
                self._add(value,node.left)
            else:
                node.left=Node(value)
                self.size+=1
            
        if (value>node.value):
            if (node.right is not None):
                self._add(value,node.right)
            else:
                node.right=Node(value)
                self.size+=1
            
    def find(self,value,node):
        if (value==node.value):    
            return node
        elif (value<node.value and node.left is not None):
            self.find(value,node.left)
        elif (value>node.value and node.rigth is not None):
            self.find(value,node.right)
        
    def DeleteTree(self):
        self.root=None
        self.size=0
        
    def PrintTree(self):
        if (self.root!=None):
            self._PrintTree(self.root)
            
            
    def _PrintTree(self,node):            
        if (node is not None):
            self._PrintTree(node.left)
            print(str(node.value)+" ")
            self._PrintTree(node.right)
 
#simple example
tr=Tree()
tr.add(7)
tr.add(12)    
tr.add(1)    
tr.add(10)    
tr.add(4)    
tr.add(2)
tr.add(0)
tr.add(15)
tr.add(16)
tr.add(14)

tr.PrintTree()     
print('Length of Tree='+str(len(tr)) )              

