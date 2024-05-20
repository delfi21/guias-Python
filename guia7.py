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

print(suma_total([1,1]))

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

#ejercicio 5.2 
def pertenece_a_cada_uno_version_2(x:list[list[int]], n: int, res:list[bool]): 
    res.clear()
    for i in range(len(x)) :
        res.append (pertenece(x[i],n))



