import pandas as pd
import logging
from transform import transform
from config import INPUT_PATH, OUTPUT_PATH, LOG_PATH 

#Remove caso já tenha sido criado algum logger
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(level=logging.INFO, 
                    filename=LOG_PATH, 
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s' )

def extract(csv):
    logging.info(f'Extração do arquivo {csv} iniciada.')
    try:
        df = pd.read_csv(csv)
        logging.info(f"Arquivo carregado com sucesso. Linhas: {len(df)}")
        return df
    except Exception as e:
        logging.error(f'Algo deu errado: {e}')
        raise

def load(df, output):
    logging.info(f'Salvando do dataframe em {output}')
    try:
        df.to_csv(output, index=False)
        logging.info(f"Arquivo salvo com sucesso!")
    
    except Exception as e:
        logging.error(f'Algo deu errado: {e}')
        raise

def main():
    df = extract(INPUT_PATH)
    df = transform(df)
    load(df, OUTPUT_PATH)
    return df

#Roda apenas quando é executado a partir do pipeline.py:
if __name__ == "__main__":
    main()