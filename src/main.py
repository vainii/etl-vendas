from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    df = extract_data('../data/vendas_raw.csv')
    df = transform_data(df)
    load_data(df, '../data/vendas_tratado.csv')

    print("Pipeline executado com sucesso!")

if __name__ == "__main__":
    run_pipeline()