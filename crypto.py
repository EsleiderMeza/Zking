#algoritmo de dispersión (Hashing)
#hash es como el ADN de los datos, el algoritmo lo procesa y genera una cadena única y fija.
def generar_hash_basico(text):
    resultado = 0
    for indice, caracter in enumerate(text):
        chart = ord(caracter) * 31 ** indice#Esta función convierte cualquier letra o símbolo en su número equivalente en código ASCII
        resultado +=chart 
    return resultado % 1000000007

#En ciberseguridad hay una propiedad crucial en el hashing llamada Efecto Avalancha. 
#Significa que si cambias un solo bit o carácter de la entrada, 
#el hash resultante debería cambiar de forma drástica e irreconocible.

