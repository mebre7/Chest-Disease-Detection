import base64
import json
import os
from pathlib import Path
from typing import Any

import joblib
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from cnnClassifier import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns its contents as a ConfigBox object.
    Args:
        path_to_yaml (str): Path like input.
    Raises:
        ValueError: If the yaml file is empty.
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox object containing the contents of the yaml file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as ex:
        raise ex

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories given a list of paths.
    Args:
        path_to_directories (list): List of directory paths to be created.
        verbose (bool): If True, logs the creation of each directory.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a dictionary to a JSON file.
    Args:
        path (Path): path to the JSON file.
        data (dict): dictionary to be saved in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file and return its contents as a ConfigBox object.
    Args:
        path (Path): path to the JSON file.
    Returns:
        ConfigBox: ConfigBox object containing the contents of the JSON file.
    """
    with open(path, "r") as f:
        content = json.load(f)

    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save data to a binary file using joblib.
    Args:
        data (Any): data to be saved.
        path (Path): path to the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load data from a binary file using joblib.
    Args:
        path (Path): path to the binary file.
    Returns:
        Any: data loaded from the binary file.
    """

    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())