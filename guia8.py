#ejercicio 1
#1.1
def contar_lineas(nombre_archivo: str)->int:
    f=open(nombre_archivo)
    print(len(f.readlines()))
    f.close()
    return 

#ejercicio 2
#queremos que crear un archivo de texto tal q las lineas q solo tienen comentarios no esten 

def es_comentario(linea_archivo:str)->bool:
    res=False 
    i = 0 
    while i< len(linea_archivo) and linea_archivo[i]!= " ":
        if linea_archivo[i] == "#":
            res=True
    return res 
            




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
    
    #holis










