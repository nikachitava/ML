import pandas as pd


df = pd.read_excel('./folders/it_2022.xlsx', sheet_name='moreten')


filtered_df = df[df['F'].str.extract(r'(\d+\.?\d*)%').astype(float)[0] > 10]


with pd.ExcelWriter('./folders/it_2022.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    filtered_df.to_excel(writer, sheet_name='Fgrade', index=False)
