import pandas as pd

def padronizar_colunas(df):
  df = df.rename(columns={
    'show_id': 'id',
    'type':'tipo',
    'title':'titulo',
    'director':'diretor',
    'cast':'elenco',
    'country':'pais',
    'date_added':'adicionado_em',
    'release_year':'lancado_em',
    'rating':'classificacao',
    'duration':'duracao',
    'listed_in':'genero'
})
  return df

def preencher_nulos(df):
  df['diretor'] = df['diretor'].fillna('Não informado')
  df['elenco'] = df['elenco'].fillna('Não informado')
  df['pais'] = df['pais'].fillna('Não informado')
  return df

def limpar_strings(df):
  df['adicionado_em'] = df['adicionado_em'].str.strip()
  return df

def tratar_datas(df):
  df['adicionado_em'] = pd.to_datetime(df['adicionado_em'], format='%B %d, %Y', errors='coerce')
  df['lancado_em'] = pd.to_datetime(df['lancado_em'], format='%Y').dt.year
  return df

def transform(df):
  #pre_transform = df.isnull().sum().sum()

  df = df.drop(columns=['description'])

  df = padronizar_colunas(df)
  df = preencher_nulos(df)

  df = limpar_strings(df)
  df = tratar_datas(df)
  #pos_transform = df.isnull().sum().sum()
  return df