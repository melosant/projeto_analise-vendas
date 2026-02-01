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
    df_order_clean = df_order[['id_order', 'price', 'date_purchase', 'id_store']]
    df_order_dirty = data.df_fact_dirty
    df_order_dirty_fat = df_order_dirty[['id_venda', 'valor', 'data', 'loja_id']]

    df_order_dirty_fat['data'] = pd.to_datetime(df_order_dirty_fat['data'], format='mixed', errors='coerce').dt.year

    return df_order_dirty_fat, df_order_clean



#     # concatenando e fazendo agreagações
#     df_concat = pd.concat([df_order_dirty_fat, df_order_clean], axis=1)
#     df_concat_stats = df_concat.agg({
#     'id_venda': ['count'],
#     'id_order': ['count'],
#     'valor': ['sum'],
#     'price': ['sum']
# })

#     # soma para tirar os nulls
#     df_final = df_concat_stats.sum().to_frame().T

#     df_final.columns = ['orders_dirty', 'orders_clean', 'sum_dirty', 'sum_clean']
#     df_final['diff_counts'] = df_final['orders_dirty'] - df_final['orders_clean']
    
#     # stack para transformar as colunas em linhas
#     df_stack = df_final.stack().reset_index()
#     df_stack.columns = ['index', 'Tipo', 'Valores']
#     df_stack.drop('index', axis=1, inplace=True)

#     return df_stack

if __name__ == '__main__':
    df = insight_dirty_cost()