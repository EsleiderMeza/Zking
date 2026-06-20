import ollama


def analizar_con_ia(linea_sospechosa):
    respuesta = ollama.chat(model='gemma4:e4b', messages=[
        {
            'role': 'user',
            'content': (
                f"Analiza esta línea de código: '{linea_sospechosa}'. "
                "Responde EN ESPAÑOL, de forma ultra corta, usando exactamente este formato de 2 líneas:\n"
                "RIESGO: (qué pasa aquí en 10 palabras)\n"
                "SOLUCIÓN: (cómo arreglarlo en 10 palabras)\n"
                "Sé directo, no saludes ni agregues nada más."
            )
        }
    ])
    
    return respuesta['message']['content']
