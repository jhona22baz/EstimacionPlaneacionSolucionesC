#!/usr/bin/python
# -*- encoding: utf-8 -*-
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
    def medium(self,listX_Y):
        """
        Function to return dictionario with all summations
        """
        nodo = listX_Y.head                
        sumax = 0.0
        sumay = 0.0
        sumaxy = 0.0
        sumax2 = 0.0
        sumay2 = 0.0
        retorno = []
        while nodo != None:            
            sumax = float(nodo.dato[0]) + sumax
            sumay = float(nodo.dato[1]) + sumay
            sumax2 = (float(nodo.dato[0]) * float(nodo.dato[0])) + sumax2
            sumay2 = (float(nodo.dato[1]) * float(nodo.dato[1])) + sumay2
            sumaxy = (float(nodo.dato[0]) * float(nodo.dato[1])) + sumaxy
            nodo = nodo.next   
        retorno = [sumax,sumay,sumax2,sumay2,sumaxy]
        return retorno

    def XYavg(self,numerador,large):
        """
        return divition
        """
        return numerador/large

    def B1(self,Exiyi,num,xavg,yavg,Ex2):
        """
        return B1
        """        
        arriba = (Exiyi)-(num*xavg*yavg)
        abajo = (Ex2) - (num * (xavg*xavg))
        res = arriba/abajo        
        return res 

    def rxy(self,num,Exiyi,Ex,Ey,Ex2,Ey2):
        """
        return rxy
        """
        arriba = num*(Exiyi)-(Ex*Ey)
        mitad1abajo =(num*(Ex2)-(math.pow(Ex,2)))
        mitad2abajo =(num*(Ey2)-(math.pow(Ey,2)))
        abajo = math.sqrt( mitad1abajo * mitad2abajo)        
        return arriba/abajo        
    def B0(self,yavg,b1,xavg):
        """
        return B0
        """
        b0 = (yavg - (b1*xavg))
        return b0

    def yk(self,b0,b1,xk):
        """
        return yk
        """
        return (b0+b1*xk)
"""
Principal part of the program
"""
Estadistica = Statistics()#clase of statistics
DLList = doublyLinkedList()#clase of the list
resultados = []#results of summaations
resultadosFinales = []#Final results
num = 0
print '-------------------------PSP Tarea 3------------------------------------------------'
nombre = raw_input('\tNombre de el archivo: ')
archi=open(nombre,'r')
xk = raw_input('ingresa el valor de proxy estimado ')

completo=archi.readlines()#read file

for line in completo:
    DLList.addToFinish(line.split())#add numbers to the list
    num +=1#lenght of the list

resultados.append(Estadistica.medium(DLList)) #recibe todas las sumatorias [Ex,Ey,Ex2,Ey2,Exy]
resultados.append(Estadistica.XYavg(resultados[0][0],num))#recibe xavg
resultados.append(Estadistica.XYavg(resultados[0][1],num))#recibe yavg
"""
aqui ya tengo todos los datos requeridos para B1 en la siguiente forma
[[Ex,Ey,Ex2,Ey2,Exy]xavg,yavg]
[[0 ,1 ,  2,  3,  4], 1 , 2  ]
"""                             
resultados.append(Estadistica.B1(resultados[0][4],num,resultados[1],resultados[2],resultados[0][2]))#recibe B1
resultados.append(Estadistica.rxy(num,resultados[0][4],resultados[0][0],resultados[0][1],resultados[0][2],resultados[0][3]))#recibo rxy
resultados.append(math.pow (resultados[4],2))#recibo r2
"""
aqui ya tengo todos los datos requeridos para B0 en la siguiente forma
[[Ex,Ey,Ex2,Ey2,Exy]xavg,yavg,B1,rxy,r2]
[[0 ,1 ,  2,  3,  4], 1 , 2  , 3, 4 ,5 ]
"""
resultados.append(Estadistica.B0(resultados[2],resultados[3],resultados[1]))#regresa B0
resultados.append(Estadistica.yk(resultados[6],resultados[3],float(xk)))#regresa yk
"""
aqui ya tengo todos los datos requeridos para B0 en la siguiente forma
[[Ex,Ey,Ex2,Ey2,Exy]xavg,yavg,B1,rxy,r2,B0,yk]
[[0 ,1 ,  2,  3,  4], 1 , 2  , 3, 4 ,5 ,6 , 7]
"""
print "\n\n____________________________________________________________________________________________________"
print '|B0 '+str(resultados[6])+ '| B1 ' +str(resultados[3])+ ' | rxy ' +str(resultados[4])+' | r2 '+str(resultados[5])+' | yk '+str(resultados[7])+' |' 
print "____________________________________________________________________________________________________\n\n"
#DLList.printList()#