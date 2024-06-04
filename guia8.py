#ejercicio1
#1.1
def contar_lineas(nombre_archivo: str)->int:
    f=open(nombre_archivo)
    n=len(f.readlines())
    f.close()
    return n


#1.2
def frase_a_lista(frase:int)->list[str]:
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
def promedio_estudiante (nombre_archivo:str, LU:str)->float:
    
    
    
    

        
    
    


        
    

            
            
    

