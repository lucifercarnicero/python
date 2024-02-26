import pandas as pd

def resumen_cotizaciones(fichero):
    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])

# Print the result to the console
print(resumen_cotizaciones('./cotizacion.csv'))
