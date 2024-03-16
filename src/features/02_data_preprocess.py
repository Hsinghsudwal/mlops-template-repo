from dataclasses import dataclass
import pandas as pd
import numpy as np
from logger import logging
import os
import joblib
from utility_file import Utility
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler,LabelEncoder

params = Utility().read_params()
Utility().create_folder('models')

class Preprocessor:
  def __init__(self) -> None:
      pass
    
  def preprocess_data(self,DATA_PATH):
    try:
        logging.info('reading data to perform preprocess')
        df = pd.read_csv(DATA_PATH)
        # numerical: imputer
        # categorical: onehotencoder
        # target: labelencoder
        # pipeline
        # save preprocess data as file
        return ('Preprocess data complete')


    except Exception as e:
        logging.error(e)
        raise e



if __name__ == "__main__":
    DATA_PATH = os.path.abspath('file_path')
    
    preprocess_data(DATA_PATH)
    print("processed.csv", DATA_PATH)
