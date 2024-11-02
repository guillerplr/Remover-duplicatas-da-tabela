import pandas as pd

df = pd.read_excel('frente.xlsx')

df = df.drop_duplicates(subset=['ID da conta'], keep='first', ignore_index=True)

df.to_excel('frente_sem_duplicatas.xlsx', index=False)