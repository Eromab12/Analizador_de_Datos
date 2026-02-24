import pandas as pd
import unidecode

def filtros_aplicados(df, columna, valor):
    #Filtra el dataframe basado en una selección.
    if valor == "Todos":
        return df
    return df[df[columna] == valor]

def identificar_tipo_columna(df, columna):
    #Identifica el tipo de columna para determinar qué filtro mostrar.
    if pd.api.types.is_numeric_dtype(df[columna]):
        return "numerico"
    elif pd.api.types.is_datetime64_any_dtype(df[columna]):
        return "fecha"
    else:
        return "categorico"

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
        raise ArchivoSinDatos("El archivo esta vacio, Sube uno que si tenga datos")
    tiene_numeros = any(pd.api.types.is_numeric_dtype(df[col]) for col in df.columns)


    if not tiene_numeros:
        raise ColumnaNumericaNoEncontrada("No hay datos numericos")
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

def gestionar_nulos(df, estrategia='eliminar', columnas=None, valor_relleno=None):
    """
    Gestiona valores nulos en el DataFrame.
    Versión corregida y simplificada.
    """
    df_limpio = df.copy()
    
    # 1. Definir qué columnas vamos a procesar
    if columnas:
        # Si el usuario pasa columnas, verificamos que existan
        cols_procesar = [col for col in columnas if col in df_limpio.columns]
    else:
        # Si no pasa columnas, tomamos TODAS las columnas del DataFrame
        cols_procesar = df_limpio.columns.tolist()
    
    # 2. Estrategia ELIMINAR
    # Dropna funciona mejor pasando directamente la lista de columnas
    if estrategia == 'eliminar':
        df_limpio = df_limpio.dropna(subset=cols_procesar)
        return df_limpio
    
    # 3. Otras Estrategias (Rellenar)
    # Iteramos solo sobre las columnas que vamos a procesar
    for col in cols_procesar:
        # Verificamos que la columna tenga nulos antes de procesar (optimización)
        if df_limpio[col].isnull().sum() == 0:
            continue
            
        tipo = identificar_tipo_columna(df_limpio, col)
        
        if estrategia == 'rellenar_media':
            if tipo == 'numerico':
                media = df_limpio[col].mean()
                df_limpio[col] = df_limpio[col].fillna(media)
                
        elif estrategia == 'rellenar_moda':
            moda = df_limpio[col].mode()
            if not moda.empty:
                df_limpio[col] = df_limpio[col].fillna(moda[0])
                
        elif estrategia == 'rellenar_constante':
            if valor_relleno is not None:
                df_limpio[col] = df_limpio[col].fillna(valor_relleno)
                
    return df_limpio

def estandarizar_texto(df, columnas=None, formato = 'titulo', quitar_tildes = True):
    #Funcion que se encarga de estandarizar columnas de texto: espacion, tildes y Mayusculas

    df_std = df.copy()

    if columnas is None:
        columnas = [col for col in df_std.columns if identificar_tipo_columna(df_std, col) == 'categorico']
    
    for col in columnas:
        if col in df_std.columns:
            df_std[col] = df_std[col].astype(str).str.strip()

            if quitar_tildes:
                df_std[col] = df_std[col].apply(lambda x: unidecode.unidecode(x))
            
            if formato == 'titulo':
                df_std[col] = df_std[col].str.title()
            elif formato == 'mayusculas':
                df_std[col] = df_std[col].str.upper()
            elif formato == 'minusculas':
                df_std[col] = df_std[col].str.lower()

            df_std[col] = df_std[col].replace('nan', pd.NA)
    return df_std

def limpiar_nombres_columnas(df):
    #Funcion que se encarga de limpiar los nombres de las columnas
    
    df.columns = [unidecode.unidecode(str(col).strip().lower().replace(' ', '_')) for col in df.columns]
    return df

def eliminar_duplicados(df):
 
 # Retorna el DataFrame limpio y la cantidad de filas eliminadas.
    n_duplicados = df.duplicated().sum()
    if n_duplicados > 0:
        df_limpio = df.drop_duplicates().reset_index(drop=True)
        return df_limpio, n_duplicados
    return df, 0

def generar_resumen_estadistico(df):
    
    #Genera un resumen estadístico de las columnas numéricas.
    #Incluye conteo, media, desviación estándar, min, max y cuartiles.
    

    return df.describe().T # Transponemos para mejor lectura en espacios verticales
