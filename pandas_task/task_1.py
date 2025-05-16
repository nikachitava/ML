import pandas as pd

df = pd.read_excel('./folders/it_2022.xlsx')

df['საგანი'] = df['საგანი'].str.replace(r'\s*\{.*?\}\s*ქართული', '', regex=True)

filtered_df = df[df['ჯამი'].str.extract(r'\((\d+)\)').astype(float)[0] > 10]

with pd.ExcelWriter('./folders/it_2022.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    filtered_df.to_excel(writer, sheet_name='moreten', index=False)
