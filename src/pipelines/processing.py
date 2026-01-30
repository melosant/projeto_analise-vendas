import pandas as pd

from src.config.database_models import Base, engine
from src.functions.common_func import processing_column_money

class ProcessingData:
    # inicialização dos csv e das tabelas
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.df_orders_dirty = pd.read_csv('data/orders.csv')
        self.df_products_dirty = pd.read_csv('data/products.csv')
        self.df_stores_dirty = pd.read_csv('data/stores.csv')

        # tabela fato sujo
        self.df_join_dirty = pd.merge(self.df_orders_dirty, self.df_products_dirty, on='id_produto', how='left')
        self.df_fact_dirty = pd.merge(self.df_join_dirty, self.df_stores_dirty, left_on='loja_id', right_on='codigo_loja', how='left')
        self.df_fact_dirty['valor'] = processing_column_money(self.df_fact_dirty['valor'])
        self.df_fact_dirty= self.df_fact_dirty.assign(valor = self.df_fact_dirty['valor'].astype('float64'))

    def processing_dfs(self):
        '''
        função de tratamento e validação dos csv
        load nas tabelas
        '''

        # dropando valores nulos das vendas para um dataframe limpo
        df_orders_copy = self.df_orders_dirty.dropna()
        df_products_copy = self.df_products_dirty
        df_stores_clean = self.df_stores_dirty

        # renomear colunas
        df_orders_copy.columns = ['id_order', 'date_purchase', 'id_product', 'id_store', 'qtd']
        df_products_copy.columns = ['id_product', 'category', 'price']
        df_stores_clean.columns = ['id_store', 'city']
        
        # conversão de tipos de colunas e replaces
        df_orders_copy['date_purchase'] = pd.to_datetime(df_orders_copy['date_purchase'], format='mixed', errors='coerce')
        df_orders_clean = df_orders_copy.dropna()
        df_products_copy['price'] = processing_column_money(df_products_copy['price'])
        df_products_clean= df_products_copy.assign(price = df_products_copy['price'].astype('float64'))

        # formando tabela fato
        df_join = pd.merge(df_orders_clean, df_products_clean, on='id_product', how='left')
        df_join_fact = pd.merge(df_join, df_stores_clean, on='id_store', how='left')
        df_tabel_fact = df_join_fact[['id_order', 'id_product', 'id_store', 'category', 'price', 'date_purchase', 'qtd']]

        # load no db
        df_tabel_fact.to_sql('orders_fact', engine, if_exists='replace', index=False)
        df_products_clean.to_sql('products_dim', engine, if_exists='replace', index=False)
        df_stores_clean.to_sql('stores_dim', engine, if_exists='replace', index=False)

if __name__ == '__main__':
    test = ProcessingData()
    test.processing_dfs()