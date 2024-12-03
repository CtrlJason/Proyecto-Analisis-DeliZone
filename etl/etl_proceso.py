import pandas as pd
import os

def etl_proceso():
    # Extraccion de los datos
    print("Iniciando proceso ETL de las publicaciones...")
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, '..', 'data', 'publicaciones.csv')
    df_origin = pd.read_csv(data_path)
    df = df_origin.copy()

    # Mostramos los datos de las publicaciones
    df
    
    # Tipos de dato por columna
    df.info()
    
    # Eliminacion de columnas que no necesitamos
    COLUMNS_TO_DROP = [
    'Identificador de la cuenta',
    'Nombre de usuario de la cuenta',
    'Nombre de la cuenta', 'Duración (segundos)',
    'Comentario sobre los datos',
    'Comentarios',
    'Enlace permanente',
    'Fecha',
    ]
    df = df.drop(COLUMNS_TO_DROP, axis=1)
    df
    
    # Separacion de Hashtags de la descripción
    # Mostramos una de las descripciones para obtener la informacion completa
    df.iloc[0]['Descripción']
    
    # Ahora obtenemos unicamente los numerales de todas las descripciones
    df['Descripción'].str.findall('#')
    # se visualizaran todos los # que esten en la descripción
    
    # Ahora obtenemos los Hashtags completos
    df['Descripción'].str.findall(r'#\w+') # findall nos sirve para buscar partes de un string en especifico
    
    # Ahora creamos separamos los hastag de la descripcion
    df['Hashtags'] = df['Descripción'].str.findall(r'#\w+')
    df
    return {"status": "ETL completado"}