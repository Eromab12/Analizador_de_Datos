import pandas as pd


    
def limpieza_datos(df):
    #Aplica limpieza basica
    #Elimina filas vacias
    df = df.dropna(how="all")
    #Elimina duplicados
    df = df.drop_duplicates()
    return df

def filtros_aplicados(df, columna, valor):
    #Filtra el dataframe basado en una selección.
    if valor == "Todos":
        return df
    return df[df[columna] == valor]

class DataError(Exception):
    """Clase base para otras excepciones"""
    pass
class ArchivoSinDatos(DataError):
    """Se lanza cuando el archivo esta vacio"""
    pass
class ColumnaNumericaNoEncontrada(DataError):
    """Se lanza cuando se intenta graficar pero no hay datos numericos"""
    pass

def validar_df(df):
    if df.empty:
        raise ArchivoSinDatos("El archivo esta vacio ❌, Sube uno que si tenga datos 😅")
    tiene_numeros = any(pd.api.types.is_numeric_dtype(df[col]) for col in df.columns)
    if not tiene_numeros:
        raise ColumnaNumericaNoEncontrada("No hay datos numericos ❌")
    return True

def carga(archivo_subido):
    #Carga el archivo subido y manejo de errores de extension
    try:
        if archivo_subido.name.endswith(".csv"):
            df = pd.read_csv(archivo_subido)
        else:
            df = pd.read_excel(archivo_subido)
        #valida el archivo automaticamente
        validar_df(df)
        return df
    except DataError as de:
        raise de
    except Exception as e:
        raise Exception(f"Error al cargar el archivo: {e}")
