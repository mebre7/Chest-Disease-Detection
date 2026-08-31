from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline 
from cnnClassifier.utils.common import logger

STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>> Stage \'{STAGE_NAME}\' is started. <<<<<<<<<<<<<<<")
        stage1 = DataIngestionPipeline()
        stage1.main()
        logger.info(f">>>>>>>>>>>>>>> Stage \'{STAGE_NAME}\'is completed. <<<<<<<<<<<<<<<\n\n x=================x")
    except Exception as e:
        logger.exception(e)
        raise e