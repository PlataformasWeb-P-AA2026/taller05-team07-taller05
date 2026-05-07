# Explicación generación formato JSON

Para generar el formato JSON que va a tomar en cuenta todas las fuentes de información de la carpeta *data*
primero generamos un entorno virtual de Python para instalar ahí las librerias necesarias

```
python -m venv .venv
```

Levantamos el entorno virtual y procedemos a instalar las librerías necesarias
```
pip install pandas beautifulsoup4 pdfplumber
```

*   **pandas**: Para el CSV.
*   **beautifulsoup4**: Para el HTML.
*   **pdfplumber**: Para extraer tablas de PDFs.