def buscar_patron(linea, patron):
    return patron.lower() in linea.lower()

"""
Solo como un tip de optimización en Python: 
cuando una condición if ya devuelve un booleano (True o False), 
puedes simplificar toda la función retornando directamente la condición. 
Quedaría así de elegante:
"""
