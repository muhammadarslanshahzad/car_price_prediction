#############################################################
#       Import Modules
############################################################

from carPricePrediction.config.configuration import ConfigurationManager
from carPricePrediction.components.data_ingestion import DataIngestion
from carPricePrediction import logger

STAGE_NAME = 'DATA INGESTION STAGE'

#############################################################
#  Data Ingestion Pipeline
# ###########################################################

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        data_ingestion.download_file()



if __name__ == '__main__':
    try: 
        logger.info(f'=============>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<=====================')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'===================>>>>>>>>>>>>>>> Stage {STAGE_NAME} <<<<<<<<<<<<<<<<<<<<========================== \n\n xxx=========================================================================xxx')
    
    except Exception as e:
        logger.exception(e)
        raise e