import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Obtener la ruta absoluta del directorio 'static'
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../static")
    # Construir la ruta completa al archivo 'index.html'
    index_path = os.path.join(static_dir, "index.html")
    # Abrir y leer el contenido del archivo 'index.html'
    with open(index_path) as f:
        html_content = f.read()
    # Devolver el contenido HTML como respuesta
    return HTMLResponse(content=html_content)
