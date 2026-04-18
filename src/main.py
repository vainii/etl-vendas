from pathlib import Path
from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    project_root = Path(__file__).resolve().parent.parent

    input_path = project_root / 'data' / 'vendas_raw.csv'
    output_path = project_root / 'data' / 'vendas_tratado.csv'

    df = extract_data(input_path)
    df = transform_data(df)
    load_data(df, output_path)

if __name__ == "__main__":
    run_pipeline()