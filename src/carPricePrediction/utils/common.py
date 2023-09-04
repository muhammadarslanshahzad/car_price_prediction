##################################################################
#   Files for the Commong Utility Functions used in whole Project
######################################################################
import os
import yaml
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from carPricePrediction import logger

###############################################
# Read Yaml Fiels
# #############################################
@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    '''
        read yaml file and returning it
        Args : 
            path_to_yaml(str) path like input
        
        Raises:
            Value Error if the file is empty
            e: empty File
        
        Returns: 
        Config Box: ConfigBox type
     '''
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("f ===============>>> Yaml file: {path_to_yaml} loaded Successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("xxxxxxxxxxxx>>> Yaml file is empty.")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''
        creating list of directories

        Args: 
            path to directories (list): list of path of directories,
            ignore_log (bool, optional): ignore if multiple dires is to be created. Defaults to false .        
    '''

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"==================>>> created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    '''
        save json data

        Args: 
            path(Path): path to json file
        
        Returns:
            str: size in KB
    '''

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    