def processing_column_money(df):
    df = (df.str.replace('R$ ', '')
            .str.replace(',', '.')
            .str.strip())
    return df