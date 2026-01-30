import pandas as pd
import matplotlib.pyplot as plt

from src.config.database_models import engine
from src.pipelines.processing import ProcessingData
from src.functions.common_func import processing_column_money

def insight_data_quality():
    data = ProcessingData()
    df_orders = pd.read_sql('orders_fact', engine)
    df_orders_dirty = data.df_fact_dirty

    df_sum_dirty = df_orders_dirty.agg({
            'valor': ['sum']
    })
    df_sum_clean = df_orders.agg({
        'price' : ['sum']
    })

    labels = ['Faturamento Sujo','Faturamento Limpo']
    values = [df_sum_dirty['valor']['sum'], df_sum_clean['price']['sum']]
    plt.bar(labels, values)
    plt.title('Custo da Sujeira')
    plt.show()

if __name__ == '__main__':
    insight_data_quality()