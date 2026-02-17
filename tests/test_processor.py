import pandas as pd
import pytest
import sys
import os

# Agregamos la ruta del proyecto para poder importar 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.processor import gestionar_nulos, estandarizar_texto, limpiar_nombres_columnas

# --- Tests para gestionar_nulos ---

def test_gestionar_nulos_eliminar():
    """
    Test 1: Verifica que se eliminan las filas con nulos.
    """
    # ARRANGE (Preparar): Creamos un DF sucio
    data = {
        'nombre': ['Ana', 'Luis', None], 
        'edad': [25, None, 30]
    }
    df_sucio = pd.DataFrame(data)
    
    # ACT (Actuar): Ejecutamos la función con estrategia 'eliminar'
    df_limpio = gestionar_nulos(df_sucio, estrategia='eliminar')
    
    # ASSERT (Verificar): 
    # Esperamos que solo quede la fila de 'Ana' (que no tiene nulos)
    # La longitud debería ser 1
    assert len(df_limpio) == 1
    assert df_limpio.iloc[0]['nombre'] == 'Ana'

def test_gestionar_nulos_rellenar_constante():
    """
    Test 2: Verifica que se rellenan nulos con un valor constante.
    """
    # ARRANGE
    data = {'ventas': [100, None, 200]}
    df_sucio = pd.DataFrame(data)
    
    # ACT: Rellenamos con 0
    df_limpio = gestionar_nulos(df_sucio, estrategia='rellenar_constante', valor_relleno=0)
    
    # ASSERT: El valor nulo ahora debería ser 0
    assert df_limpio.iloc[1]['ventas'] == 0
    # Verificamos que no haya ningún nulo restante en todo el DF
    assert df_limpio.isnull().sum().sum() == 0

# --- Tests para estandarizar_texto ---

def test_estandarizar_texto_mayusculas_y_tildes():
    """
    Test 3: Verifica limpieza de espacios, tildes y formato.
    """
    # ARRANGE
    data = {'ciudad': ['  méxico  ', 'NUEVA YORK', '  bogotá  ']}
    df_sucio = pd.DataFrame(data)
    
    # ACT: Queremos mayúsculas y quitar tildes
    df_limpio = estandarizar_texto(df_sucio, formato='mayusculas', quitar_tildes=True)
    
    # ASSERT
    # '  méxico  ' -> strip() -> 'méxico' -> upper() -> 'MÉXICO' -> unidecode -> 'MEXICO'
    assert df_limpio.iloc[0]['ciudad'] == 'MEXICO'
    # Verificamos que no haya espacios al inicio/final
    assert df_limpio.iloc[1]['ciudad'] == 'NUEVA YORK'

def test_estandarizar_texto_automatico():
    """
    Test 4: Si no paso columnas, debe detectar y limpiar las categóricas automáticamente.
    """
    # ARRANGE
    data = {
        'id': [1, 2], 
        'nombre': ['juan', 'pedro'] # Categórica
    }
    df = pd.DataFrame(data)
    
    # ACT: No especificamos columnas, debería limpiar solo 'nombre'
    df_limpio = estandarizar_texto(df, formato='titulo')
    
    # ASSERT: 'juan' debería ser 'Juan'
    assert df_limpio.iloc[0]['nombre'] == 'Juan'
    # 'id' no debería cambiar (es numérico)
    assert df_limpio.iloc[0]['id'] == 1

# --- Tests para limpiar_nombres_columnas ---

def test_limpiar_nombres_columnas():
    """
    Test 5: Nombres de columnas a minúsculas, sin espacios ni tildes.
    """
    # ARRANGE
    df = pd.DataFrame(columns=['Nombre Cliente', '  Edad  ', 'Ciudad_Origen'])
    
    # ACT
    df_limpio = limpiar_nombres_columnas(df)
    
    # ASSERT
    # 'Nombre Cliente' -> 'nombre_cliente'
    assert 'nombre_cliente' in df_limpio.columns
    # '  Edad  ' -> 'edad'
    assert 'edad' in df_limpio.columns
    # Verificamos que las viejas columnas sucias ya no existen
    assert 'Nombre Cliente' not in df_limpio.columns