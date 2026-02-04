import pandas as pd

from src.config.database_models import engine
from src.pipelines.processing import ProcessingData


def insight_dirty_cost():
    '''
    gera um df concatenado contendo informações de total de pedidos e de faturamento antes e pós tratamento.
    '''
    data = ProcessingData()

    # importação e seleção das colunas
    df_order = pd.read_sql('orders_fact' , engine)
    df_order_clean = df_order[['id_order', 'price', 'date_purchase', 'id_store', 'id_product']]
    df_order_dirty = data.df_fact_dirty
    df_order_dirty_fat = df_order_dirty[['id_venda', 'valor', 'data', 'loja_id']]

    df_order_dirty_fat['data'] = pd.to_datetime(df_order_dirty_fat['data'], format='mixed', errors='coerce').dt.year

    return df_order_dirty_fat, df_order_clean