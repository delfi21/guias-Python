
import random
import numpy as np #preguntar el warning 
#problema1 :: 
# 1.1 pertenece

def pertenece(x: list[int], y: int) -> bool:
    i = 0
    lo_encontre : bool = False 
    while not lo_encontre and i < len(x):
        if y == x[i]:
            lo_encontre = True
        i += 1
#1.2
def divide_a_todos(s:list[int], e:int) -> bool:
    res:bool=True 
    i:int=0
    while res and i< len(s):
        if s[i]%e != 0:
            res=False 
        i=i+1
    return res


#1.3 :: suma de elemenos de una lista 
def suma_total(x: list[int]):
    suma: int = 0
    i: int =0
    while i < len(x):
       suma= suma+x[i]
       i =i+1
    return suma
        

def suma_total2(x: list[int]):
    suma: int = 0 
    for i in x:
        suma += i
    return suma  #revisar lista vacia 

#1.4 ordenados 
def ordenados(s:list[int])->bool: 
    res:bool=True 
    i:int=0
    while res and i<len(s)-1: #si es vacia len= 0 y esto es falso no?
        if s[i] > s[i+1]:
            res=False
        i=i+1 
    return res 

#1.5
def mayor_a_siete(s:list[str])->bool:
    res:bool=False
    i:int=0
    while not res and i<len(s):
        if len(s[i]) > 7:
            res=True 
        i=i+1
    return res 

#1.6
def se_lee_igual(palabra:str)->bool:
    if palabra==palabra[::-1]:
        res=True 
    else: 
        res=False
    return res #preguntar si vale 


#problema 1.7 :: fortaleza_contraseña 
def tiene_mayuscula(x:str) -> bool:
    es_mayuscula: bool =False  
    for i in x:
        if i>='A' and i<='Z' and not es_mayuscula: 
            es_mayuscula=True
    return es_mayuscula

def tiene_minuscula(x:str) -> bool:
    es_minuscula: bool =False  
    for i in x:
        if i>='a' and i<='z' and not es_minuscula: 
            es_minuscula=True
    return es_minuscula
def tiene_numero(x:str) -> bool:
    es_numero: bool = False 
    for i in x: 
        if i>= "0" and i<= "9" and not es_numero:
            es_numero=True
    return es_numero 
def fortaleza_contraseña(x:str) -> str: 
    if len(x) > 8 and tiene_mayuscula(x) and tiene_minuscula(x) and tiene_numero(x):
        res="verde"
    elif len(x)<5:
        res="rojo"
    else:
        res="amarillo" 
    return res 
#ejercicio 1.8 
def saldo_actual(historial:list[tuple:(str,int)]): #revisar especificacion del tipo
    monedero:list[int]=[]
    for i in historial:
        if i[1] == "I":
            monedero.append(i[2])
        if i[1]== "R":
            monedero.append(-1*i[2])
        return sum(monedero) 
    
#1.9
def pertenece2(x: list[str], y: str) -> bool:
    i = 0
    lo_encontre : bool = False 
    while not lo_encontre and i < len(x):
        if y == x[i]:
            lo_encontre = True
        i += 1
    return lo_encontre 

def al_menos_tres(palabra:str):
    vocales:list[str]=["a","e","i","o","u"]
    vocales_palabra:list[str]=[]
    i=0
    while i<len(palabra) and len(vocales_palabra)<3:
        if pertenece2(vocales, palabra[i]) == True:
            vocales_palabra.append(palabra[i])
        i=i+1
    if len(vocales_palabra) == 3:
        res=True
    else:
        res=False
    return res    

#EJERCICIO 2
#2.1
def pares_por_cero(s:list[int])->None:
    for i in range(len(s)):
        if i%2==0:
            s[i]=0
#2.2
def pares_por_cero2(s:list[int])->list[int]:
    res=s.copy() #que pasaba si igualaba directamente?
    for i in range(len(res)):
        if i%2==0:
            res[i]=0
    return res 

#2.3
def sin_vocales(palabra:str)->str:
    vocales:list[str]=["a","e","i","o","u"]
    palabra_nueva:str=""
    for i in palabra:
        if pertenece2(vocales,i)== False:
            palabra_nueva= palabra_nueva + i 
    return palabra_nueva #preguntar porque me im

#2.4 remplaza las vocales por un guion
def remplaza_vocales(palabra:str)->str: 
    vocales:list[int]=["a", "e","i","o","u"]
    res:str= ""
    for i in palabra: 
        if pertenece2(vocales, i) == True:
            res= res + "-"
        else:
            res=res+i
    return(res)
            
  #2.5
def dar_vuelta_str(palabra:str)->str:
    return palabra[::-1] #como lo hagp sin esto?
    
#2.6
def pertenece3(palabra:str, letra:str)->bool:
    pertenece:bool=False 
    i:int=0
    while not pertenece and i<len(palabra):
        if palabra[i] == letra:
            pertenece=True 
        i=i+1
    return pertenece

def eliminar_repetidos(palabra:str)->str:
    res:str=""
    for i in palabra:
        if not pertenece3(res,i):
            res=res+i 
    return res 


#Ejercicio 3
def aprobado(notas:list[int])->int:
    menor_a_4:bool= False 
    i:int=0
    promedio=sum(notas)/len(notas)
    while not menor_a_4 and i<len(notas):
        if notas[i]<4:
            menor_a_4=True 
        i=i+1
    if menor_a_4:
        if promedio<4:
            res:int=3
    else:
        if promedio>=4 and promedio<7:
            res:int=2
        elif promedio >=7:
            res:int=1
    return res 

# Ejercicio 4
#4.1
def lista_nombres()->list[str]:
    lista_nombres:list[str] = []
    sigo_pidiendo: bool = True 
    while sigo_pidiendo:
        nombre=input("Ingrese nombre:\n")
        if nombre == "listo":
            sigo_pidiendo= False 
        else:
            lista_nombres.append(nombre)
    return(lista_nombres)
#4.2
def historial_monedero() -> list[tuple]:
    historial_monedero:list[int] = []
    continuar_operacion:bool = True 
    while continuar_operacion:
        operacion=input("seleccione la operacion a realizar:\n")
        if operacion == "C":
            monto_a_cargar:int=int(input("ingrese el monto a cargar:\n"))
            historial_monedero.append(("C", monto_a_cargar))
        elif operacion == "D":
              monto_a_descontar:int=int(input("ingrese el monto a descontar:\n"))
              historial_monedero.append(("D", monto_a_descontar))
        elif operacion == "X":
            continuar_operacion= False 
    return historial_monedero 

#4.3
def siete_y_medio()-> list[int]: 
    historial_cartas:list[int] = []
    puntos:list[int] = []
    seguir_jugando= True 
    while seguir_jugando:
        carta: int = random.choice([1,2,3,4,5,6,7,10,11,12])
        historial_cartas.append(carta)
        if carta <= 7:
            puntos.append(carta)
        else:
            puntos.append(0.5)
        if sum(puntos) >= 7.5:
            print("¡Perdiste!")
            seguir_jugando=False 
        else:
            print(carta)
            dar_otra_carta= input("¿queres sacar otra carta?:\n") 
            if dar_otra_carta == "no":
                seguir_jugando = False 
                print(f"Ganaste {sum(puntos)}")
                
    return historial_cartas 

#Ejercicio 5

#ejercicio 5.2 
def pertenece_a_cada_uno_version_2(x:list[list[int]], n: int, res:list[bool]): 
    res.clear()
    for i in range(len(x)) :
        res.append (pertenece(x[i],n))
#la version 1 cambia un toque el requiere y seria correcto si devuelve una lista con true false en las posiciones de x y en posiciones mayores, cualquier cosa.
#el dos contempla al 1, por eso no lo programo a parte, pero el 1 no contemplas al 2.

#5.3
def es_matriz(x:list[list[int]])-> bool:
    res:bool=True 
    if len(x)>0 and len(x[0])>0:
        for i in range(len(x)-1):
            if len(x[i]) != len(x[i+1]):
                res=False 
    else: 
        res=False 
    return res 

def filas_ordenadas(matriz:list[list[int]])-> bool:
    estan_ordenadas:bool=True 
    i=0
    while estan_ordenadas and i< len(matriz):
        if not ordenados(matriz[i]):
            estan_ordenadas=False 
        i=i+1
    return estan_ordenadas

#Ejercicio 5 
def multiplicar_matrices(matriz1:list[list[int]], matriz2:list[list[int]])->list[list[int]]: #requiere lo necesario para q valga el producto de matrices
    matriz1=np.array(matriz1)
    matriz2=np.array(matriz2)
    res=matriz1.copy()
    for i in range(len(res)):
        for j in range(len(res)):
            res[i,j]=sum((matriz1[i,:])*matriz2[:,j])
    return res


def potencia_matriz(dimension:int, potencia:int)-> list[list[int]]:
    matriz=np.random.random((dimension,dimension))
    paso:int=1
    res=matriz.copy()
    while paso<potencia:
        res=multiplicar_matrices(res,matriz)
        paso=paso+1
    return res #preguntar debugguer 



    
            
  






