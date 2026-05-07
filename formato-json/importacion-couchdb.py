"""
Script para importar el JSON unificado a CouchDB usando la API REST.
"""
import requests
import json
from config import user, password, host, port, database

url = f"http://{user}:{password}@{host}:{port}/{database}/_bulk_docs"
with open('./data/mundial_2026.json', 'rb') as f:
    data = json.load(f)

response = requests.post(url, json=data, headers={'Content-Type': 'application/json; charset=utf-8'})
print(response.status_code)