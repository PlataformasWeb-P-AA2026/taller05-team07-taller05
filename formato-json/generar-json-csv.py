import pandas as pd
import json

"""
Script para generar un JSON a partir de un CSV, siguiendo la estructura requerida por CouchDB.
"""

def generar_json_csv():
    lista_jugadores = []

    # --- PROCESAR CSV (SUDAMÉRICA) ---
    print("Procesando CSV...")
    df_sudamerica = pd.read_csv('../data/fuente_csv_sudamerica.csv')
    # str.capitalize() convierte la primera letra de cada palabra a mayúscula, el resto a minúscula
    df_sudamerica.columns = df_sudamerica.columns.str.capitalize()
    # Convertimos el DataFrame directamente a una lista de diccionarios
    jugadores_csv = df_sudamerica.to_dict(orient='records')
    lista_jugadores.extend(jugadores_csv)

    # --- ESTRUCTURA REQUERIDA POR COUCHDB ---
    # CouchDB necesita el formato { "docs": [ ... ] }
    resultado_couch = {
        "docs": lista_jugadores
    }

    # --- GUARDAR ARCHIVO ---
    with open('csv_data.json', 'w', encoding='utf-8') as f:
        json.dump(resultado_couch, f, ensure_ascii=False, indent=4)

    print(f"Éxito: Se han procesado {len(lista_jugadores)} registros.")

if __name__ == "__main__":
    generar_json_csv()