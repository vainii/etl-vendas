import pandas as pd

def transform_data(df):
    # Remover valores nulos
    df = df.dropna()

    # Converter data
    df['data'] = pd.to_datetime(df['data'])

    # Criar coluna de faturamento
    df['faturamento'] = df['preco'] * df['quantidade']

    return df