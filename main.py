from config.database_models import Base, engine

# criação da database
Base.metadata.create_all(bind=engine)