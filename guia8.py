#ARCHIVOS
#ejercicio1
#1.1
def contar_lineas(nombre_archivo: str)->int:
    f=open(nombre_archivo)
    n=len(f.readlines())
    f.close()
    return n


#1.2
def frase_a_lista(frase:str)->list[str]:
    palabra:str=""
    res:list[str]=[]
    for caracter in frase:
        if caracter != " ":
            palabra+=caracter 
        if caracter == " " or caracter==frase[len(frase)-1]:
            res.append(palabra)
            palabra=""
    return res 
def pertenece(palabra:str, lista:list[str])->bool:
    pertenece:bool=False
    i=0
    while not pertenece and i<len(lista):
        if lista[i]==palabra or lista[i]==palabra+"\n":
            pertenece=True
        i+=1
    return pertenece 

def existe_palabra(palabra:str, nombre_archivo:str)->bool:
    f=open(nombre_archivo)
    archivo=f.readlines()
    palabras:list[str]=[]
    for frase in archivo:
        palabras.append(frase_a_lista(frase))
    f.close()
    return pertenece(palabra,palabras) #probar 

#1.3
def cantidad_de_apariciones(palabra:str, nombre_archivo:str)->int:
    f=open(nombre_archivo)
    archivo=f.readlines()
    print(archivo)
    palabras:list[str]=[]
    palabras2:list[str]=[]
    res:int=0
    for frase in archivo:
        palabras.append(frase_a_lista(frase))
    for i in palabras:
        for j in i:
            palabras2.append(j)
    print(palabras2)
    for elem in palabras2:
        if elem == palabra or elem==palabra+"\n":
            res += 1
    return res 

#Ejecicio 2
def es_comentario(linea_archivo:str)->bool:
    esComentario:bool=False 
    for i in range(len(linea_archivo)):
        if linea_archivo[i] != " ":
            break 
    if linea_archivo[i]== "#":
        esComentario=True
    return esComentario #como lo hago sin el break?


def clonar_sin_comentarios(nombre_de_archivo:str):
    f=open(nombre_de_archivo)
    res:list[str]=[]
    for i in (f.readlines()):
        if es_comentario(i)==False:
            res.append(i)
    f.close()
    nombre_clonado="clonado_"+ nombre_de_archivo
    f_out=open(nombre_clonado, "w") #si no existe, lo crea, y si existe y pusiste w, pisa lo q habia ahi. La funcio "a ", te permite escribir pero lo appendea al final
    f_out.writelines(res)
    f_out.close 

#ejercicio3
def invertir_lineas(nombre_archivo:str):
    f=open(nombre_archivo)
    archivo=f.readlines()
    reverso=archivo[::-1]
    f.close()
    f_out=open("reverso.txt","w")
    f_out.writelines(reverso)
    f_out.close()

#ejercicio4
def agregar_frase_al_final(nombre_archivo:str, frase:str):
    f=open(nombre_archivo, "a")
    f.writelines(frase)
    f.close()
    
#ejercicio5
def agregar_frase_al_principio(nombre_archivo:str, frase:str):
    f=open(nombre_archivo)
    archivo=f.readlines()
    res=[frase+"\n"]+archivo
    f.close()
    f=open(nombre_archivo, "w")
    f.writelines(res)
    f.close()
    
#ejercicio6
#preguntar 

#ejercicio7
def sacarEspacio(palabra:str)->str: #saca el salto de linea en realidad 
    res:str=""
    for i in palabra:
        if i != "\n":
            res+=i
    return res 


def encontrarIndice(lista:int, elemento:int)->int:
    for i in range(len(lista)):
        if lista[i] == elemento:
            res=i
    return res 

def frase_a_lista_csv(frase:str)->list[str]:
    palabra:str=""
    res:list[str]=[]
    for caracter in frase:
        if caracter != ",":
            palabra+=caracter 
        if caracter == "," or caracter==frase[len(frase)-1]:
            res.append(palabra)
            palabra=""
    return res  

def sacarRepetidos(lista:list)->list:
    res:list=[]
    for i in lista:
        if i not in res:
            res.append(i)
    return res 
            
        

def columnas_de_datos(nombre_archivo:str)->list[list[str]]: #me devuelve una lista con los numeros de libreta como primer elemento y las notas como segundo 
    f=open(nombre_archivo)
    archivo=f.readlines()
    archivo_matriz:list[list[str]]=[] #hacer esta lista no es necesario pero me di cuenta despues y como anda igual no lo cambie 
    f.close()
    for i in archivo:
        elemento:list[str]=[i]
        archivo_matriz.append(elemento)
    archivo_matriz_copia=archivo_matriz.copy()
    for i in range(len(archivo_matriz_copia)):
        if (archivo_matriz_copia[i])==["\n"]:
            h=encontrarIndice(archivo_matriz, archivo_matriz_copia[i])
            archivo_matriz.pop(h)
    numeroDeLibreta:list[str]=[]
    nota:list[str]=[]
    for j in archivo_matriz:
        palabras=frase_a_lista_csv(j[0])
        numeroDeLibreta.append(palabras[0])
        nota.append(palabras[3])
    numeroDeLibreta.pop(0)
    nota.pop(0)
    return [numeroDeLibreta, nota]

def promedioEstudiante(nombre_archivo:str, lu:str)->float:
    data:list[str]=columnas_de_datos(nombre_archivo)
    notas:list[int]=[]
    for i in range(len(data[0])):
        if data[0][i] == lu:
            notas.append(float(data[1][i]))
        if i == lu+"\n":
            notas.append(float(sacarEspacio(data[1][i]))) #esto esta de mas tambien pero lo mismo, me di cuenta despues porque primero hice otra cosa
    promedio:float=sum(notas)/len(notas)
    return promedio 


def calcular_promedio_por_estudiante(nombre_archivo:str, nombre_archivo_promedios:str):
    f=open(nombre_archivo_promedios, "w")
    data:list[str]=columnas_de_datos(nombre_archivo)
    res:list[str]=["LU,Promedio\n"]
    for i in data[0]:
        promedio=promedioEstudiante(nombre_archivo, i)
        res.append(f"{i,promedio}\n")
    res=sacarRepetidos(res)
    f.writelines(res)

#probablemnete la hice larguisima pero anda asi q no me importa mucho jajajja
        
    
#PILAS
    
#Ejercicio8
from queue import LifoQueue as Pila
import random 

def generar_n_al_azar(cantidad:int, desde:int, hasta:int)->Pila[int]:
    p= Pila()
    i=0
    while i < cantidad:
        p.put(random.randint(desde,hasta))
        i=i+1
    return p 

def imprimir_pila(p:Pila): #defino una funcion para poder ver las pilas 
    res:list=[]
    while not p.empty():
        res.append(p.get())
    res=res[::-1]
    print(res)
    for i in range(len(res)):
        p.put(res[i])

#ejercicio 9 
def cant_elementos(p:Pila)->int:
    res:list=[]
    while not p.empty():
        res.append(p.get())
    res=res[::-1]
    for i in range(len(res)):
        p.put(res[i])
    return len(res)

#ejercicio10
def maximo(lista:list[int])->int:
    mayor=lista[0]
    for i in range(len(lista)):
        if mayor<lista[i]:
            mayor=lista[i]
    return mayor

                
def buscarMaximo(p:Pila[int])->int:
    res:list=[]
    while not p.empty():
        res.append(p.get())
    res=res[::-1]
    max=maximo(res)
    for i in range(len(res)):
        p.put(res[i])
    return max 

#ejercicio 11
#lo veo despues porque me da fiaca 

#ejercicio 12
#same

#COLAS 
#ejercicio 13 
from queue import Queue as Cola 

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
    print(len(lista_aux))
    for i in range(len(lista_aux)):
        c.put(lista_aux[i])
        
#ejercicio 14
def cant_elementos(c:Cola)->int:
     lista_aux=[]
     while not c.empty():
        lista_aux.append(c.get())
     res=len(lista_aux)
     for i in range(lista_aux):
        c.put(lista_aux[i])
     return res 
 
#ejercicio 15 #asumo q es igual a la de la pila 

#ejercicio 16
def armar_secuencia_de_bingo()->Cola[int]:
    c=Cola()
    for i in range(0,100):
        c.put(random.randint(0,99))
    return c 

def carton_bingo()->list[int]:
    res:list[int]=[]
    while len(res) < 12:
        res.append(random.randint(0,99))
    return res 

def encontrarIndice(lista:int, elemento:int)->int:
    for i in range(len(lista)):
        if lista[i] == elemento:
            res=i
    return res 

    
    

def jugar_carton_bingo()->int: 
    carton:list[int]=carton_bingo()
    copia_carton=carton.copy()
    bolillero:Cola[int]=armar_secuencia_de_bingo()
    bolillero_aux:list[int]=[]
    while not bolillero.empty():
        bolillero_aux.append(bolillero.get())
    print("se ejecuto")
    for i in bolillero_aux:
        bolillero.put(i)
    print("se ejecuto")
    while copia_carton != []:
        bolilla:int=bolillero.get()
        if bolilla in copia_carton:
            print(bolilla)
            copia_carton.remove(bolilla)
            print(carton)
            print(copia_carton)#se cuelga aca y no se porque. Funciona hasta que qudan 4 elementos en copia carton 
    print("se ejecuto") # lo hice con remove pero en realidad hay q hacerlo con buscar indice y pop (pero queria ver si era eso lo q me lo colgaba) 
    res:list[int]=[]
    while not bolillero.empty():
        res.append(bolillero.get())
    print("se ejecuto")
    cant_jugadas:int=len(res)
    bolillero.empty()
    for i in bolillero_aux:
        bolillero.put(i)
    return 100- cant_jugadas #esto se puede hacer mas facil con un contador 


#ejercicio 17 
def n_pacientes_urgentes(cola:Cola[(int,str,str)])->int:
    aux:list[tuple:[int,str,str]]=[]#preguntar
    pacientesPrioridad:int=0 #para que use una cola?
    while not cola.empty():
        aux.append(cola.get())
    for i in aux:
        if i[0]==1 or i[0]==2 or i[0]==3:
            pacientesPrioridad +=1
    for i in aux:
        cola.put(i)
    return pacientesPrioridad

#ejercicio 18
def atencion_a_clientes(c:Cola[(str, int, bool, bool)])->Cola[(str, int, bool, bool)]:
    lista_restaurar:list=[]
    res:Cola=Cola()
    prioridad:list=[]
    preferencial:list=[]
    pobre:list=[] #jeje 
    while not c.empty():
        lista_restaurar.append(c.get())
    for i in lista_restaurar:
        c.put(i)
    for i in lista_restaurar:
        if i[3]:
            prioridad.append(i)
        elif i[2]:
            preferencial.append(i) #se me pone 2 veces esto revisar #lo veo mañana
        else:
            pobre.append(i)
    for i in prioridad:
        res.put(i)
    for i in preferencial:
        res.put(preferencial)
    for i in pobre:
        res.put(i)
    return res  #revisar 

#Diccionarios 
#ejercicio 19


def agrupar_por_longitud(nombre_archivo:str)->dict:
    diccionario:dict={} #preguntar 
    f=open(nombre_archivo)
    archivo=f.readlines()
    palabras:list[str]=[]
    for i in archivo:
        x:list[str]=frase_a_lista(i) #me devuelve una lista con las palabras de la frase 
        for j in x:
            palabras.append(j) #desarmo las listas 
    palabras_copia=palabras.copy()
    for i in range(len(palabras_copia)): #saco los caracteres que son saltos de linea 
        if palabras_copia[i] == "\n":
            h=encontrarIndice(palabras, palabras_copia[i])
            palabras.pop(h)
    print(palabras)
    for i in palabras:
        if len(i) in diccionario.keys(): #cuenta los saltos de linea al final de la palbras, no se si eso deberia sacarlo 
            diccionario[(len(i))]+=1
        else:
            diccionario[(len(i))]=1
    return diccionario  

#ejercicio 20
def calcular_promedio_estudiantes2(nombre_archivo:str)->dict:
    data:list[str]=columnas_de_datos(nombre_archivo)
    res:list=[]
    diccionario:dict={}
    for i in data[0]:
        promedio=promedioEstudiante(nombre_archivo, i)
        res.append((i,promedio))
    res=sacarRepetidos(res)
    for i in res:
        diccionario[i[0]]=i[1]
    return diccionario
    
#ejercicio21
def mayor(x:list[int])->int:
    mayor=x[0]
    for i in x:
        if mayor<i:
                mayor=i 
    return mayor 

def palabra_mas_frecuente(nombre_archivo:str)->str:
    repeticiones:dict={}
    f=open(nombre_archivo)
    archivo=f.readlines()
    archivo2:list[list[str]]=[]
    palabras:list[str]=[]
    for i in archivo:
        x=frase_a_lista(i)
        archivo2.append(x)
    for j in archivo2: 
            for i in j:
                i=sacarEspacio(i)
                palabras.append(i)
    palabras_copia=palabras.copy()
    for i in range(len(palabras_copia)):
        if palabras_copia[i]=="":
            h=encontrarIndice(palabras, palabras_copia[i])
            palabras.pop(h)
    apariciones:int=0
    i=0
    while i < len(palabras):
        palabra=palabras[i]
        for j in palabras:
            if palabra == j:
                apariciones+=1
        if palabra not in repeticiones.keys():
            repeticiones[palabra]=apariciones
        apariciones=0
        i+=1
    x=list(repeticiones.keys())
    mayor=x[0]
    for j in range(len((x))):
        if repeticiones[mayor]< repeticiones[x[j]]:
            mayor=x[j]
    return mayor
    
#ejercicio 22 
historiales:dict={}
def visitar_sitio(historiales:dict, usuario:str, sitio:str):
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        historiales[usuario]=Pila()
        historiales[usuario].put(sitio)



def navegar_atras(historiales:dict[str,Pila[str]], usuario:str): #esto no anda con un historial vacio 
    historial:Pila[str]=historiales[usuario]
    historial_aux:list[str]=[]
    while not historial.empty():
        historial_aux.append(historial.get())
    historial_aux=historial_aux[::-1]
    for i in historial_aux:
        historial.put(i) #podria hacer una distincion aca con la lista vacia que se yo, paja 
    sitio_anterior:str=historial_aux[len(historial_aux)-2]
    historial.put(sitio_anterior)

#ejercicio23
inventario:dict[str, dict[str, dict[str,int]]]={}
def agregar_producto(invetario:dict[str,dict[str, int]], nombre:str, precio:int, cant:int): #el porducto a agregar no esta en inventario
    inventario[nombre]={"precio":precio, "cantidad":cant}

def actualizar_stock(invetario:dict[str,dict[str, int]], nombre:str, cant:int):
    producto:dict=inventario[nombre]
    producto["cantidad"]=cant


def actualizar_stock(invetario:dict[str,dict[str, int]], nombre:str, precio:int): #los precios deberian ser floats pero bueno 
    producto:dict=inventario[nombre]
    producto["precio"]=precio

def calcular_valor_inventario(invetario:dict[str,dict[str, int]])->float:
    valores:list[int]=[]
    for clave in inventario.keys():
        producto:dict=inventario[clave]
        valor_total:int=producto["precio"]*producto["cantidad"]
        valores.append(valor_total)
    #print(valores)
    return sum(valores)


        
    
    


    
        



        
    
    
        
    

        
            
        
    
    
    
    
    




        
    
    
        

    


        

        
            
    
    
    
    

    
            
            

    
        
            
    
            
        
            
            
        
    
    
        
    


    
    
    
    

        
    
    


        
    

            
            
    

