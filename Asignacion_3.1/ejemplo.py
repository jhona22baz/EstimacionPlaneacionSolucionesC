nombre = raw_input('\tNombre de el archivo: ')
        
archi=open(nombre,'r')
completo=archi.readlines()
lista = []

for line in completo:
    lista.append(line.split())

#print linea
print lista
