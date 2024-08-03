from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>{STAGE_NAME} started <<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f" >>> stage {STAGE_NAME} completed <<<")
    except Exception as e:
        logger.exception(e)
        raise e