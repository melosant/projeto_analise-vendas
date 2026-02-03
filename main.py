from src.config.database_models import Base, engine
from src.pipelines.processing import ProcessingData

# criação da database
Base.metadata.create_all(bind=engine)

# transform e load nas tabelas
load = ProcessingData()
load.processing_dfs()