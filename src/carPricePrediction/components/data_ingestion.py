################################################
# Imports Modules
################################################

import os
import opendatasets as od
from pathlib import Path
from carPricePrediction.utils.common import get_size
from carPricePrediction import logger
from carPricePrediction.config.configuration import DataIngestionConfig



##################################################
# Class Data Ingestion
# ################################################

class DataIngestion:
    def __init__(
            self,
            config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            os.chdir(self.config.root_dir)
            od.download(self.config.source_URL)
            logger.info(f'Data is donwload! =======================>')
            os.chdir('../../')
        else:
            logger.info(f"File already exist of size: {get_size(Path(self.confg.local_data_file))}")
