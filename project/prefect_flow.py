from prefect import flow, task, get_run_logger
from pipeline import extract, load
from transform import transform
from config import INPUT_PATH, OUTPUT_PATH

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
    logger.info("Iniciando transformação...")
    df = transform(df)
    logger.info(f"Transformação concluída!")
    return df

@task
def load_task(df):
    logger = get_run_logger()
    logger.info(f'Salvando dataframe...')
    load(df, OUTPUT_PATH)
    logger.info(f"Arquivo salvo com sucesso!")

@flow(name='estudo-prefect')
def pipeline_flow():
    df = extract_task()
    df = transform_task(df)
    load_task(df)

if __name__ == "__main__":
    pipeline_flow()
