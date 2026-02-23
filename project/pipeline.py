import pandas as pd
from transform import transform
from config import INPUT_PATH, OUTPUT_PATH

def extract(csv):
    df = pd.read_csv(csv)
    return df

def load(df, output):
    df.to_csv(output, index=False)

def main():
    df = extract(INPUT_PATH)
    df = transform(df)
    load(df, OUTPUT_PATH)
    return df

#Roda apenas quando é executado a partir do pipeline.py:
if __name__ == "__main__":
    main()