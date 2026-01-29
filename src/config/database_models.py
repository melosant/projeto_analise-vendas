# import libs
from sqlalchemy import create_engine, Column, Integer, Date, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# criação engine, início de sessão e declaração de base
engine = create_engine('sqlite:///data/database.db')
Session = sessionmaker()
session = Session()
Base = declarative_base()

# criação das tabelas
class Orders_Facts(Base):
    __tablename__ = 'orders_fact'

    id_order = Column('id_order', Integer, primary_key=True)
    id_product = Column('id_product', String)
    id_store = Column('id_store', String)
    category = Column('category', String)
    price = Column('price', Float)
    date_purchase = Column('date_purchase', Date)
    qtd = Column('quantity', Integer)

    def __init__(self, id_order, id_product, id_store, category, price, date_purchase, qtd):
        self.id_order = id_order 
        self.id_product = id_product 
        self.id_store = id_store 
        self.category = category 
        self.price = price 
        self.date_purchase = date_purchase 
        self.qtd = qtd 

class Products_Dim(Base):
    __tablename__ = 'products_dim'

    id_product = Column('id_product', String, primary_key=True)
    category = Column('category', String)
    price = Column('price', Float)

    def __init__(self, id_product, category, price):
        self.id_product = id_product
        self.category = category 
        self.price = price 

class Stores_Dim(Base):
    __tablename__ = 'stores_dim'

    id_store = Column('id_store', String, primary_key=True)
    city = Column('city', String)

    def __init__(self, id_store, city):
        self.id_store = id_store
        self.city = city