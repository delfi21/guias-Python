
import random
#problema2 :: suma de elemenos de una lista 
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
    return suma 



#problema1 :: pertenece

def pertenece(x: list[int], y: int) -> bool:
    i = 0
    lo_encontre : bool = False 
    while not lo_encontre and i < len(x):
        if y == x[i]:
            lo_encontre = True
        i += 1
    return lo_encontre

#problema 7 :: fortaleza_contraseña 
def tiene_mayuscula(x:str) -> bool:
    es_mayuscula: bool =False  
    for i in x:
        if i>='A' and i<='Z' and not es_mayuscula: 
            es_mayuscula=True
    return es_mayuscula3

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

#ejercicio 5.2 
def pertenece_a_cada_uno_version_2(x:list[list[int]], n: int, res:list[bool]): 
    res.clear()
    for i in range(len(x)) :
        res.append (pertenece(x[i],n))

# Ejercicio 4
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

print(siete_y_medio())




