import pandas as pd

df = pd.read_excel('arquivo.xlsx')

df = df.drop_duplicates(subset=['Coluna com duplicatas'], keep='first', ignore_index=True)

df.to_excel('arquivo_sem_duplicatas.xlsx', index=False)
