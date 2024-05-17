import pandas as pd
import numpy as np
from logger import logging
import os
from utility_file import Utility
# import aws

Utility().create_folder('Logs')
params = Utility().read_params()

#main_log_folderpath = params['logging_folder_paths']['main_log_foldername']
#make_data_path = params['logging_folder_paths']['data_loading']


class MakeDataset:

    def __init__(self) -> None:
        pass

    def load_and_save(self):

        try:
            # getting data url from params.yaml file
            url = params['data_location']['notebook_data']

        except Exception as e:
            logging.error(e)
            raise e


if __name__ == "__main__":

    md = MakeDataset()
    md.load_and_save()

