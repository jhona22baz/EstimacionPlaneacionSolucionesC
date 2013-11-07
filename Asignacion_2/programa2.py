#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
 Program Assignment:  programa2.py                                                         
 Name:  Jhonatan Bazaldúa Oliva
 Date:  02 Oct 2013
 Description: A LOC program 
'''
'''
Class declarations:                                                                                            
        
functions: 
    +count_loc
'''
#BASE 0
def count_loc(lines):
    '''
    Function that count coude lines
    '''
    #Declaracion de variables#
    nb_lines  = 0#cuenta el numero de lineas#
    numclass = 0#cuenta las clases#
    function = 0#cuenta las funciones#
    modificada = 0#cuenta las lineas modificadas#
    reusada = 0#cuenta las lineas reusadas#
    eliminada = 0#cuenta lineas eliminadas#
    base = 0#cuenta lineas base#
    agregada = 0#cuenta lineas agregadas#

    docstring = False#docstring es la documentacion del codigo por defecto en python en este caso no se contara#
    for line in lines:
        line = line.strip()

        if line == "" \
           or line.endswith("#") \
           or docstring\
           and not (line.startswith('"""')\
           or line.startswith("'''"))\
           or (line.startswith("'''")\
           and line.endswith("'''")\
           and len(line) >3)  \
           or (line.startswith('"""')\
           and line.endswith('"""') and len(line) >3) :
            continue
        # this is either a starting or ending docstring #
        elif line.startswith('"""') or line.startswith("'''"):
            docstring = not docstring
            continue
        elif "#BASE" in line:
            base = line[5:10]            
        elif "class" in line:
            numclass+=1
            if "REUSE" in line:
                reusada +=1
            else:
                nb_lines+=1            
        elif "def" in line:
            function+=1
            if "REUSE" in line:
                reusada +=1
            else:
                nb_lines+=1                        
        elif "MODIFIED" in line:
            modificada+=1
            nb_lines+=1
        elif "REUSE" in line:
            reusada +=1
        elif "DELETED" in line:
            eliminada +=1        
        else:
            nb_lines += 1
    if int(base) == 0:
        eliminada = 0
        agregada = nb_lines
    elif base > nb_lines:
        eliminada = int(base) - nb_lines
    elif base < nb_lines:
        agregada = int(base) - nb_lines    
    else :
        agregada = 0
        eliminada = 0        
    total = nb_lines + reusada
    #print "----------------------------------------------------------------------------------------"#
    print "%d clases |%d funciones|%d modificadas|%d reusadas|%d base|%d eliminadas|%d agregadas"%(numclass , function , modificada, reusada, int(base), eliminada, agregada)
    #print "----------------------------------------------------------------------------------------"#
    return total

#archi=open('/home/jhonatan/Documentos/PSP/Asignacion_2/estandar_codigo_programa1.py','r')#
#archi=open('/home/jhonatan/prueba.py','r')#
nombre = raw_input('\tNombre de el archivo: ')
archi=open(nombre,'r')

linea=archi.readlines()
print "%d Totales"%(count_loc(linea))#here I call to the main function
