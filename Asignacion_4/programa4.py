#!/usr/bin/python#
#-*- encoding: utf-8 -*-#
import math
class Node: #REUSE
    """
    Node have dato and next. have a __init__ and __str__ functions for init the method and acept 
    all data. and recive a varible named dato that will bi add to the list 
    """
    def __init__(self, dato):#REUSE
        self.dato = dato#REUSE
        self.next = None      #REUSE          
    def __str__(self):#REUSE
        return str(self.dato)#REUSE

class  doublyLinkedList:   #REUSE
    '''
    doublyLinkedList
    recive: 
    funtions:
        +addToFinish
        +AddToInit
        +Delete
        +printList
    '''
    def __init__(self):        #REUSE
        self.head = None       #REUSE
        self.Tail = None        #REUSE
    def addToFinish(self,dato):  #REUSE
        """
        Function to add to the Finish
        """
        nodo_nuevo = Node(dato) #REUSE
        if self.head == None:  #REUSE
            self.head = nodo_nuevo #REUSE
        if self.Tail != None:  #REUSE
            self.Tail.next = nodo_nuevo #REUSE
        self.Tail = nodo_nuevo#REUSE
    def AddToInit(self, dato):#REUSE
        """
        Function to add to the init
        """
        nodo_nuevo = Node(dato)#REUSE
        if self.head == None: #REUSE
            self.head = nodo_nuevo  #REUSE      
        if self.Tail != None: #REUSE
            nodo_nuevo.next = self.head #REUSE
            self.head =  nodo_nuevo #REUSE
    def Delete(self,dataToDelete):#REUSE
        """
        Function to delete data 
        """
        node = self.head#REUSE
        prev = node#REUSE
        if self.head.dato == dataToDelete: #REUSE
            self.head == self.head.next#REUSE
        else: #REUSE
            while node != None:#REUSE
                if node.dato == dataToDelete:#REUSE
                    prev.next = node.next#REUSE
                prev = node#REUSE
                node = node.next#REUSE
    def printList(self):#REUSE
        """
        Function to print List 
        """
        node = self.head#REUSE
        while node != None:#REUSE
            print node.dato#REUSE
            node = node.next    #REUSE

class Statistics():
    """
    Statistics is a clase that I will use for create all funtions abaut math
    """         
    def XYavg(self,numerador,large):#REUSE
        """
        return divition
        """
        return numerador/large#REUSE

    def lenForItem(self, everyItems):       #8
    	'''
    	function for obtaind number for item
    	'''
    	nodo = DLList.head
    	resultList = doublyLinkedList()
    	algo = []
    	while nodo!=None:    		    		
    		algo.append(float(nodo.dato[0])/float(nodo.dato[1]))
    		nodo = nodo.next    		    	
    	return algo

    def natureLogForItem(self,items):       #5
    	'''
    	return all nature logarithm in the list
    	'''
    	anser = []
    	for item in items:
    		anser.append(math.log(item))
    	return anser
    def Variance(self,values,avarage):      #7
    	'''
    	this function will return the variance for numbers list
    	'''
    	auxiliarList = []#this variable going to help me to obtain the variance
    	variableVarianza = 0.0
    	for x in values:
    		auxiliarList.append(math.pow((x-avarage),2))
    	variableVarianza = math.fsum(auxiliarList)/(len(auxiliarList)-1)
    	return variableVarianza
    def rangesOfLog(self,avg,stDv):         #7
    	'''
    	recive the avarage and standart deviation
    	the function will return all natural logarithm verySmall, small, medium, large and very large
    	'''
    	lnVS = avg -2*stDv
    	lnS = avg - stDv
    	lnM = avg 
    	lnL = avg + stDv
    	lnVL = avg + 2*stDv
    	return lnVS, lnS ,lnM,lnL,lnVL
    def OriginalForm(self,lnVS, lnS ,lnM,lnL,lnVL):  #7
        '''
        OriginalForm print all the parametres necesaries for the final program result
        '''
    	Vs = math.exp(lnVS)
    	S = math.exp(lnS)
    	M = math.exp(lnM)
    	L = math.exp(lnL)
    	VL = math.exp(lnVL)
    	print 'VS = ',Vs,' S = ',S,' M = ',M,' L = ',L,' VL =',VL

'''
Main program
'''
Estadistica = Statistics()                              #32
DLList = doublyLinkedList()
num = 0
arrayOfLenOfItems = []#array of Len of items
arrayOfLogLn = []#array of natural logs
ELn = 0.0 #varialbe for total of sumatori of ln
averageOfLog = 0.0
valueofVariance = 0.0
valueOfStandartDeviation = 0.0
VarOfLnVS = 0.0
VarOfLnS = 0.0
VarOfLnM = 0.0
VarOfLnL = 0.0
VarOfLnVL = 0.0
print '--------------------------PSP homework 4---------------------------'
nombre = nombre = raw_input('\tNombre de el archivo: ')#optain the file name
archi=open(nombre,'r')#open the file
complete = archi.readlines()#read all file and asign in the string named complete
for line in complete:
	DLList.addToFinish(line.split()) #add numbers to the list
	num+=1#count how many lines are?
arrayOfLenOfItems = Estadistica.lenForItem(DLList) #step 1
arrayOfLogLn = Estadistica.natureLogForItem(arrayOfLenOfItems)#step 2
ELn = math.fsum(arrayOfLogLn)#step2
averageOfLog = Estadistica.XYavg(ELn,len(arrayOfLogLn))#step3
valueofVariance = Estadistica.Variance(arrayOfLogLn,averageOfLog)#step4
valueOfStandartDeviation = math.sqrt(valueofVariance)#step5
VarOfLnVS,VarOfLnS,VarOfLnM,VarOfLnL,VarOfLnVL =  Estadistica.rangesOfLog(averageOfLog,valueOfStandartDeviation)#step6
print "\n\n____________________________________________________________________________________________________"
Estadistica.OriginalForm(VarOfLnVS,VarOfLnS,VarOfLnM,VarOfLnL,VarOfLnVL)
print "____________________________________________________________________________________________________\n\n"