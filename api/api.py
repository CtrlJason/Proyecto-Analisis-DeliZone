from fastapi import FastAPI # Request
from fastapi.responses import JSONResponse
# from fastapi.staticfiles import StaticFiles

# Importaciones del proyecto
from etl.etl_proceso import etl_proceso
from viz.visualizaciones import generar_grafico
from ml.arboles import modelo_arbol
from ml.bayes import modelo_bayes

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Bienvenido al API de DeliZone"}

@app.get("/run_etl")
async def run_etl():
    resultado_etl = etl_proceso()
    return JSONResponse(content={"message": "ETL completado", "result": resultado_etl})

@app.get("/run_dataviz")
async def dataviz():
    grafico = generar_grafico()
    # with open("graficos/grafico.png", "wb") as f:
    #     f.write(grafico)
    return JSONResponse(content={"message": "Gráfico generado"})

@app.get("/ml/arboles")
async def ml_arboles():
    ml_result = modelo_arbol()
    return JSONResponse(content={"message": "Modelo de árboles ejecutado", "result": ml_result})

@app.get("/ml/bayes")
async def ml_bayes():
    ml_result = modelo_bayes()
    return JSONResponse(content={"message": "Modelo de Bayes ejecutado", "result": ml_result})