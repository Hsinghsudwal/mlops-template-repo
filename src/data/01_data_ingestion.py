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

    def load_and_save(self, url, filename):
        """This method is used to read the data from aws s3 storage and save to local drive.

        Returns
        --------
        None
        """

        try:
            # getting data url from params.yaml file
            url = params['data_location']['notebook_data']

            #url = inital_url + url.split('/')[-2]
            logging.info("reading csv to dataset")
            # Reading the csv file
            data = pd.read_csv(url)

            main_data_folder = params['data_location']['main_data_folder']
            raw_data_folder = params['data_location']['raw_data_folder']

            #raw_data_path = os.path.join("artifacts/data", "raw.csv")

            # Creating a Data folder to save the loaded data
            Utility().create_folder(main_data_folder)
            Utility().create_folder(os.path.join(main_data_folder, raw_data_folder))

            # Saving the loaded data to the Data folder
            data.to_csv(os.path.join(main_data_folder, raw_data_folder, str(
                filename)), index=False, sep=',')
            logging.info("save to folder path for raw data")

        except Exception as e:
            logging.error(e)
            raise e


if __name__ == "__main__":

    data_url = params['data_location']['notebook_data']

    md = MakeDataset()
    logging.info('Loading of data started.')

    raw_data_filename = params['data_location']['raw_data_filename']
    md.load_and_save(data_url, raw_data_filename)
    logging.info(
        'Data loading completed and data saved to the directory artificats/raw')
