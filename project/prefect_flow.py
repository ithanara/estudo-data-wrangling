from prefect import flow, task, get_run_logger
from pipeline import extract, load
from transform import transform
from config import INPUT_PATH, OUTPUT_PATH
import os


@task
def extract_task():
    logger = get_run_logger()
    logger.info("Iniciando extração...")

    df = extract(INPUT_PATH)

    logger.info(f"Arquivo carregado com sucesso. Linhas: {len(df)}")
    return df

@task
def transform_task(df):
    logger = get_run_logger()
    nulos_inicio = df.isna().sum().sum()
    total_campos = df.size

    logger.info(f"Iniciando transformação... Nulos: {nulos_inicio}")

    df = transform(df)

    nulos_final = df.isna().sum().sum()
    logger.info(f"Transformação concluída! Nulos: {nulos_final}")

    #Alerta muitos nulos:
    percentual_nulos = (nulos_final / total_campos) * 100
    if percentual_nulos > 10:
        logger.warning(
            f"Alto volume de valores nulos: {percentual_nulos:.2f}% do dataset."
        )
    return df

@task
def load_task(df):
    logger = get_run_logger()
    logger.info(f'Salvando dataframe em {OUTPUT_PATH}...')

    load(df, OUTPUT_PATH)

    if os.path.exists(OUTPUT_PATH):
        logger.warning("Arquivo de saída já existe e será sobrescrito.")

    logger.info(f"Arquivo salvo com sucesso!")
    

@flow(name='estudo-prefect')
def pipeline_flow():
    df = extract_task()
    df = transform_task(df)
    load_task(df)

if __name__ == "__main__":
    pipeline_flow()
