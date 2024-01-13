import os
from pathlib import Path

list_of_files =  [
    '.github/workflows/.gitkeep',  # if we want to push the empty folder to github
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evalution.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utils/__init__.py'
    'src/utils/utils.py',
    'src/logger/logging.py',
    'src/exception/exception.py',
    'test/unit/__init__.py',
    'test/integration/__init__.py',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',
    'experiment/experiments.ipynb',
    
]
for filename in list_of_files:
    filepath = Path(filename)
    filedir, filename = os.path.split(filepath) # split the path into directory and filename eg src/components/data_ingestion.py -> src/components, data_ingestion.py
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory: {filedir} for file: {filename}")
        
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create empty file