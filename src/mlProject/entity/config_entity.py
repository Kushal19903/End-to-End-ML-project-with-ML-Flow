#entity
from dataclasses import dataclass
from pathlib import Path

#dataclass define variables
@dataclass(frozen=True)    #no self needed for this dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path         #return 4 varibles only
    
    

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    
    
#why we are using mlflow code is because of evolution stress because we get losses and accuracy matrix
#we use mlflow to track our experiment
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str