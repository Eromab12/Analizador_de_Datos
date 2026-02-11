import plotly.express as px

def renderizador_graficos(df, eje_x, eje_y, tipo_grafico):
    #Carga el archivo subido

    if tipo_grafico == "Barras":
        fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_x} por {eje_y}")
    elif tipo_grafico == "Lineas":
        fig = px.line(df, x=eje_x, y=eje_y, title=f"Tendencia de {eje_y}")
    else:
        fig = px.scatter(df, x=eje_x, y=eje_y, title=f"Relacion {eje_x} vs {eje_y}")
    return fig