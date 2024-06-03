
from queue import Queue as Cola 
import random 

#ejercicio 13 
def generar_n_al_azar(cantidad:int, desde:int,hasta:int)->Cola[int]:
    c:Cola[int]=Cola()
    elementos:int=0
    while elementos<cantidad:
        c.put(random.randint(desde,hasta))
        elementos=elementos+1
    return c

def generar_n_al_azar2(cant,desde,hasta):
    c=Cola()
    for i in range(cant):
         c.put(random.randint(desde,hasta))
    return(c)

def imprimir_cola(c:Cola[int]):
    lista_aux=[]
    while not c.empty():
        lista_aux.append(c.get())
    print(lista_aux)
    for i in range(lista_aux):
        c.put(lista_aux[i])

#ejercicio 19 
def separar_palabras(lineas:str)->list[str]:

def contar_longitud_palabras(linea:str)->list[int]:
    longitudes:list[int]=[]
    i:int=0
    longitud:int=0
    while linea[i] != " ":




def agrupar_por_longitud(nombre_archivo:str)->dict:
    diccionario={}
    f=open(nombre_archivo)
    archivo=f.readlines()
    longitudes:list[list[int]]=[]
    for i in range(archivo):
        x=contar_longitud_palabras(archivo[i])
        longitudes.append(x)
    for elemento in longitudes:
        for j in elemento:
            repeticiones= contar_repetidos(j, longitudes)
            diccionario[j]=repeticiones
    return diccionario 



def agrupar_por_longitud2(archivo):
    f=open(archivo)
    longitudes:dict[int,int]={}
    for linea in f.readlines():
        for palabra in linea.split():
            if len(palabra) in longitudes.keys():
                longitudes[len(palabra)]+=1
            else:
                longitudes[len(palabra)]=1
    f.close()
    return(longitudes)

            

