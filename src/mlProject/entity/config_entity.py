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