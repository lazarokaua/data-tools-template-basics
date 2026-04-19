from pathlib import Path
import pandas as pd
import streamlit as st

def load_data(file_path):
    # TODO: ler arquivo (csv, txt, etc)
    pass

def process_data(df):
    # TODO: aplicar filtros / groupby / contagens e retorne um df
    return df

def main():
    data_path = Path("data/seu_arquivo.csv")

    if not data_path.exists():
        print("Coloque o arquivo dentro da pasta /data")
        return

    df = load_data(data_path)
    result = process_data(df)

    st.dataframe(result)

if __name__ == "__main__":
    main()
