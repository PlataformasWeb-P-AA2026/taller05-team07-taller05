import pdfplumber
import json

"""
Script para generar un JSON a partir de un PDF, siguiendo la estructura requerida por CouchDB.
"""

def generar_json_pdf():
    lista_jugadores = []
    
    # Declaramos la variable del header fuera del ciclo para mantenerla entre páginas
    headers_pdf = None 

    # --- PROCESAR PDF (NORTEAMÉRICA / ASIA) ---
    print("Procesando PDF...")
    with pdfplumber.open('../data/fuente_pdf_norteamerica_asia.pdf') as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            
            if table:
                # 1. Validamos si es la primera vez que leemos la tabla
                if headers_pdf is None:
                    headers_pdf = table[0]  # Guardamos la cabecera
                    filas_datos = table[1:] # Los datos empiezan en la fila 1
                else:
                    # En las siguientes páginas, toda la tabla son datos
                    filas_datos = table 
                
                # 2. Iteramos sobre las filas de datos correctamente
                for row in filas_datos:
                    # Creamos diccionario filtrando valores Nulos
                    if row[0]: # Si la primera celda no está vacía
                        
                        # zip() para combinar los headers con los valores de la fila
                        jugador = {key: value for key, value in zip(headers_pdf, row)}
                        
                        lista_jugadores.append(jugador)

    # --- 4. ESTRUCTURA REQUERIDA POR COUCHDB ---
    # CouchDB necesita el formato { "docs": [ ... ] }
    resultado_couch = {
        "docs": lista_jugadores
    }

    # --- 5. GUARDAR ARCHIVO ---
    with open('./data/pdf_data.json', 'w', encoding='utf-8') as f:
        json.dump(resultado_couch, f, ensure_ascii=False, indent=4)
    
    print(f"Éxito: Se han procesado {len(lista_jugadores)} registros.")

if __name__ == "__main__":
    generar_json_pdf()