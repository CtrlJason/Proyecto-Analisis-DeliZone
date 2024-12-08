import matplotlib.pyplot as plt
import pandas as pd
import os

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, '..', 'data', 'datos_trabajados', 'publicaciones.csv')
data = pd.read_csv(data_path)
tipo_publicacion_alcance = data.groupby("Tipo de publicación")["Alcance"].mean()

def generar_grafico_alcance():
    print("Iniciando proceso VIZ de las publicaciones...")
    
    # Alcance por Tipo de Publicación
    tipo_publicacion_alcance = data.groupby("Tipo de publicación")["Alcance"].mean()
    plt.figure(figsize=(8, 5))
    tipo_publicacion_alcance.sort_values().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Promedio de Alcance por Tipo de Publicación")
    plt.xlabel("Tipo de Publicación")
    plt.ylabel("Promedio de Alcance")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def generar_grafico_impresiones():
    # Crear el gráfico de dispersión Impresiones y Me gusta
    plt.figure(figsize=(8, 5))
    plt.scatter(data["Impresiones"], data["Me gusta"], color='orange', alpha=0.7)
    plt.title("Relación entre Impresiones y Me gusta")
    plt.xlabel("Impresiones")
    plt.ylabel("Me gusta")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

def generar_grafico_interacciones():
    interacciones = data[["Me gusta", "Veces que se guardó", "Veces que se compartió"]].sum()
    # Crearmos el grafico Interacciones totales
    plt.figure(figsize=(10, 6))
    interacciones.plot(kind="bar", color=["#6A5ACD", "#6495ED", "#FFA07A"], edgecolor="black")
    plt.title("Interacciones Totales")
    plt.ylabel("Cantidad Total")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()