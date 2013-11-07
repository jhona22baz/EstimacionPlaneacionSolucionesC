#!/usr/bin/python
'''
 Program Assignment:  programa1.py                                                         
 Name:  Jhonatan Bazaldúa Oliva
 Date:  03 Sep 2013
 Description: Program that Give you an Average and standard Deviation with my own list
'''
'''
Class declarations:                                                                                            
    +Node
    +doublyLinkedList
functions: 
    +Average
    +doublyLinkedList
'''
#BASE 0
import math 

class Node:
    """
    Node have dato and next. have a __init__ and __str__ functions for init the method and acept 
    all data. and recive a varible named dato that will bi add to the list 
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None                
    def __str__(self):
        return str(self.dato)

class  doublyLinkedList:   
    '''
    doublyLinkedList
    recive: 
    funtions:
        +addToFinish
        +AddToInit
        +Delete
        +printList
    '''
    def __init__(self):
    '''
    function to initialize the variables in class doublyLinkedList
    '''
        self.head = None
        self.Tail = None        
    def addToFinish(self,dato):
    '''
    function to add at thefinish of list
    '''  
        nodo_nuevo = Node(dato)
        if self.head == None: 
            self.head = nodo_nuevo
        if self.Tail != None: 
            self.Tail.next = nodo_nuevo
        self.Tail = nodo_nuevo
    def AddToInit(self, dato):
    '''
    function to add at the init of list
    '''  
        nodo_nuevo = Node(dato)
        if self.head == None: 
            self.head = nodo_nuevo        
        if self.Tail != None: 
            nodo_nuevo.next = self.head 
            self.head =  nodo_nuevo 
    def Delete(self,dataToDelete):
    '''
    function to delite any data if exist in the list 
    '''  
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
    '''
    function: print list function
    '''          
        node = self.head
        while node != None:
            print node.dato
            node = node.next    
def Average(DLList):
    '''
    function: return the Average
    '''  
    nodo = DLList.head
    numofElements = 0
    elem = []
    while nodo != None:
        elem.append(nodo.dato)
        nodo = nodo.next   
    return  math.fsum(elem)/len(elem)

def standardDeviation(DLList,medium):
    '''
    function: return standard Deviation
    '''  
    node = DLList.head
    Summation = 0.0 #MODIFICADA
    li = []
    result = 0.0
    val = 0.0
    while node != None:
        node.dato, medium, "dato y media"
        val = math.pow((node.dato - medium),2)
        li.append(val)        
        node = node.next       
    #print li, "valores al cuadrado"#
    summa = math.fsum(li)
    result = math.sqrt((summa/(len(li)-1)))
    return result
#ENDFUNCTION#
DLList = doublyLinkedList()
# DLList.addToFinish(186)#
# DLList.addToFinish(699)#
# DLList.addToFinish(132)#
# DLList.addToFinish(272)#
# DLList.addToFinish(291)#
# DLList.addToFinish(331)#
# DLList.addToFinish(199)#
# DLList.addToFinish(1890)#
# DLList.addToFinish(788)#
# DLList.addToFinish(1601)#
# DLList.addToFinish(15)#
# DLList.addToFinish(69.9)#
# DLList.addToFinish(6.5)#
# DLList.addToFinish(22.4)#
# DLList.addToFinish(28.4)#
# DLList.addToFinish(65.9)#
# DLList.addToFinish(19.4)#
# DLList.addToFinish(198.7)#
# DLList.addToFinish(38.8)#
# DLList.addToFinish(138.2)#
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
media = Average(DLList)#Mando a llamar la media y la guardo en media
print "la media es:"
print media
print "la desviacion estarndar es:"
standar = standardDeviation(DLList,media)
print "-------------"
print standar