from crypto import generar_hash_basico
from analyzer import buscar_patron
from ai_analyzer import analizar_con_ia
from scanner import listar_archivos

VERTIONS = 1.0
NAMETOOL = "ZKING"


def ejecutar_escaneo(ruta_carpeta):
    # CORRECCIÓN 1: Traemos la lista de archivos usando el parámetro de la función
    lista_de_archivos = listar_archivos(ruta_carpeta)
    
    reporte_amenazas = {}
    palabras_clave = ["password", "token", "key", "secret"]

    try:
        with open("reporte_auditoria.txt", "a") as log:
            for archivo_actual in lista_de_archivos:
                print(f"[+] Escaneando archivo: {archivo_actual}")
                log.write(f"--- NUEVO ESCANEO DE ARCHIVO: {archivo_actual} ---\n")
                
                contenido_completo = "" 
                
                with open(archivo_actual, "r") as archivo:
                    for linea in archivo:
                        contenido_completo += linea 
                
                        for patron in palabras_clave:
                            if buscar_patron(linea, patron):
                                if patron in reporte_amenazas:
                                    reporte_amenazas[patron] += 1
                                else:
                                    reporte_amenazas[patron] = 1
                                
                                print(f"[ALERTA] se encontro un patron sospechoso: {linea.strip()}")
                                print("[IA] Analizando vulnerabilidad...")
                                analisis_ia = analizar_con_ia(linea)
                                print(f"Consejo de la IA:\n{analisis_ia}\n" + "-"*20)
                                
                                log.write(f"[ALERTA] se encontro un patron sospechoso: {linea.strip()}\n")
                                log.write(f"Consejo de la IA:\n{analisis_ia}\n" + "-"*20 + "\n")
                                break

                hash_final = generar_hash_basico(contenido_completo)
                print(f"[+] Archivo escaneado: {archivo_actual}")
                print(f"La huella digital HASH es: {hash_final}\n" + "."*30 + "\n")
                
                log.write(f"[+] Archivo escaneado: {archivo_actual}\n")
                log.write(f"La huella digital HASH es: {hash_final}\n" + "."*30 + "\n")
        
            print("\n" + "="*30)
            print("--- REPORTE GLOBAL DE AMENAZAS EN LA CARPETA ---")
            print(reporte_amenazas)
            print("================================")
            
            log.write("\n" + "="*30 + "\n")
            log.write("--- REPORTE GLOBAL DE AMENAZAS EN LA CARPETA ---\n")
            log.write(f"{reporte_amenazas}\n")
            log.write("================================" + "\n")

    # CORRECCIÓN 2: Usamos ruta_carpeta para los mensajes de error
    except FileNotFoundError:
        print(f"\n[ERROR CRÍTICO] La carpeta o archivo '{ruta_carpeta}' no existe. Verifica la ruta.")
    except PermissionError:
        print(f"\n[ERROR CRÍTICO] No tienes permisos para acceder a '{ruta_carpeta}'.")


if __name__ == "__main__":
    print(f"Bienvenido a {NAMETOOL} {VERTIONS}")
    objetivo = input("Ingresa la ruta de tu carpeta a analizar: ")
    print(f"Objetivo fijado en: {objetivo}\n")
    
    ejecutar_escaneo(objetivo)
