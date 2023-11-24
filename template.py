import os
from pathlib import Path
import logging

root_logger= logging.getLogger()
root_logger.setLevel(logging.DEBUG) # or whatever
handler = logging.FileHandler('test.log', 'w', 'utf-8') # or whatever
handler.setFormatter(logging.Formatter('%(asctime)s %(messages)s')) # or whatever
root_logger.addHandler(handler)

project_name = "CNN_Classifier_Chicken_Disease"

list_of_files = [".github/workflows/.gitkeep",
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/components/__init__.py",
                 f"src/{project_name}/utils/__init__.py",
                 f"src/{project_name}/config/__init.py",
                 f"src/{project_name}/config/configuration.py",
                 f"src/{project_name}/pipeline/__init__.py",
                 f"src/{project_name}/entity/__init__.py",
                 f"src/{project_name}/constants/__init__.py",
                 "config/config.yaml",
                 "dvc.yaml",
                 "params.yaml",
                 "requirements.txt",
                 "setup.py",
                 "research/trials.ipynb"]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for File:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")