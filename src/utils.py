import pandas as pd
import io

def exportar_csv(df):
    #Esta funcio se encarga de devolver el archivo csv con los nuevos datos editados
    return df.to_csv(index=False).encode('utf-8')
    
   
def exportar_excel(df):
    #Esta funcion se encarga de devolver el archivo excel utilizando xlsxwriter 
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        
    excel = buffer.getvalue()
    return excel
                    
