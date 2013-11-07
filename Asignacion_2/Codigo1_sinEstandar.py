#!/usr/bin/python
import math 
class Node: 
    def __init__(self, dato):
        self.dato = dato
        self.next = None        
    def __str__(self):
        return str(self.dato)    
class  doublyLinkedList:    
    def __init__(self):
        self.head = None
        self.Tail = None    
    def addToFinish(self,dato):  
        nodo_nuevo = Node(dato) #MODIFICADA
        if self.head == None: 
            self.head = nodo_nuevo            
        if self.Tail != None: 
            self.Tail.next = nodo_nuevo                    
        self.Tail = nodo_nuevo
    def AddToInit(self, dato):
        nodo_nuevo = Node(dato)
        if self.head == None: 
            self.head = nodo_nuevo        
        if self.Tail != None: 
            nodo_nuevo.next = self.head 
            self.head =  nodo_nuevo 
    def Delete(self,dataToDelete):
        node = self.head
        prev = node
        if self.head.dato == dataToDelete: 
            self.head == self.head.next
        else: 
            while node != None:
                if node.dato == dataToDelete:
                    prev.next = node.next
                prev = node
                node = node.next    
    def printList(self):
        node = self.head
        while node != None:
            print node.dato
            node = node.next    
def Average(DLList):
    nodo = DLList.head
    numofElements = 0
    elem = []
    while nodo != None:
        elem.append(nodo.dato)
        nodo = nodo.next   
    return  math.fsum(elem)/len(elem)
def standardDeviation(DLList,medium):
    node = DLList.head
    Summation = 0.0
    li = []
    result = 0.0
    val = 0.0
    while node != None:
        node.dato, medium, "dato y media"
        val = math.pow((node.dato - medium),2)
        li.append(val)        
        node = node.next           
    summa = math.fsum(li)
    result = math.sqrt((summa/(len(li)-1)))
    return result
DLList = doublyLinkedList()
DLList.addToFinish(160)
DLList.addToFinish(591)
DLList.addToFinish(114)
DLList.addToFinish(229)
DLList.addToFinish(230)
DLList.addToFinish(270)
DLList.addToFinish(128)
DLList.addToFinish(1657)
DLList.addToFinish(624)
DLList.addToFinish(1503)
print "los datos usados fueron:"
DLList.printList()
media = Average(DLList)
print "la media es:"
print media
print "la desviacion estarndar es:"
standar = standardDeviation(DLList,media)
print "-------------"
print standar