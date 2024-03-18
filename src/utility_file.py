import yaml
import os
import dill
import pickle


class Utility:

    def __init__(self, params_path='params.yaml') -> None:
        self.params_path = params_path

    def create_folder(self, folder_name):
        """This method is used to create folders that are required.

        Returns
        --------
        None
        """

        try:
            # Creating a directory if it does not exist already
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

        except Exception as e:
            raise e
        
    def save_model(file_path, obj):
        """save model to the path folder with name """
        try:
            dir_path = os.path.dirname(file_path)

            os.makedirs(dir_path, exist_ok=True)

            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)

        except Exception as e:
            raise e
        
    def load_model(file_path):
        """this will load the model from save path 
        return : model name
        """
        try:
            with open(file_path, "rb") as file_obj:
             return pickle.load(file_obj)

        except Exception as e:
            raise e

    def read_params(self):
        """This method is used to read the parameters yaml file.

        Parameters: 
        
        config_path: Path to the parameters yaml file

        Returns: the yaml file object.
        """

        try:
            # Reading params yaml file
            with open(self.params_path, 'r') as params_file:
                params = yaml.safe_load(params_file)

        except Exception as e:
            raise e

        else:
            return params