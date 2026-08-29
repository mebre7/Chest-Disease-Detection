from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main():
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>> Stage \'{STAGE_NAME}\' is started. <<<<<<<<<<<<<<<")
        DataIngestionTrainingPipeline().main()
        logger.info(f">>>>>>>>>>>>>>> Stage \'{STAGE_NAME}\'is completed. <<<<<<<<<<<<<<<\n\n x=================x")
    except Exception as e:
        logger.exception(e)
        raise e