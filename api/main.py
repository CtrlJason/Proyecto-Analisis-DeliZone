from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

# Importaciones del proyecto
from etl.etl import etl_proceso
from ml.ml import model_arbol
from viz.viz import dataviz

app = FastAPI

# Define los endpoints

@app.get("/")
async def home():
    return "Bienvenido a la API ETL"


@app.get("/run_etl")
async def run_etl():
# Función que ejecuta el proceso de ETL
    etl_result = etl_proceso()
    return JSONResponse(content={"message": "ETL completado"}, media_type="application/json")


# Graficos
@app.get("/dataviz")
async def dataviz():
# Carga los datos y genera un gráfico
data = carga_datos()
grafico = generar_grafico(data)
# Almacena el gráfico en una carpeta aparte
with open("graficos/" + "gráfico.png", "wb") as f:
    f.write(grafico)
    return JSONResponse(content={"message": "Grafico generado"}, media_type="application/json")
    
@app.get("/dataviz")
async def dataviz():
# Carga los datos y genera un gráfico
data = carga_datos()
grafico = generar_grafico(data)
# Almacena el gráfico en una carpeta aparte
with open("graficos/" + "gráfico.png", "wb") as f:
    f.write(grafico)
    return JSONResponse(content={"message": "Grafico generado"}, media_type="application/json")

@app.get("/ml/arboles")
async def ml_arboles():
    # Llama a la función que ejecuta el modelo de árboles
    ml_result = model_arbol()
    return JSONResponse(content={"message": "Modelo de árboles completado"}, media_type="application/json")

# Función principal que llama a las funciones de ETL y ML

def main():
    etl_proceso()
    # Llama a la función que ejecuta el modelo de árboles
    model_arbol()
    # Llama a la función que ejecuta el modelo de Bayes
    model_baye()

if __name__ == '__main__':
    uvicorn.run('api:app', host="127.0.0.1", port=8000, reload=True)