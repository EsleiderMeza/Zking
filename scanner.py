import os

def listar_archivos(ruta_carpeta):
    archivos_validos = [] # Aquí guardaremos solo los archivos que pasen el filtro
    
    # os.listdir nos da solo los nombres sueltos (ej. "secreto.txt")
    for nombre in os.listdir(ruta_carpeta):
        # Creamos la ruta completa (ej. "./secreto.txt")
        ruta_completa = os.path.join(ruta_carpeta, nombre)
        
        # Filtro 1: ¿Es realmente un archivo? 
        # Filtro 2: ¿Termina en .txt o .py o .log?
        if os.path.isfile(ruta_completa) and (nombre.endswith('.txt') or nombre.endswith('.py') or nombre.endswith('.log')):
            archivos_validos.append(ruta_completa) # Lo sumamos a la lista
            
    return archivos_validos # Devolvemos la lista limpia al programa principal



if __name__ == "__main__":
    print("Probando el escáner filtrado en la carpeta actual:")
    resultado = listar_archivos(".")
    print(resultado)
