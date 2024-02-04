import json

# 3rd party dependencies
import tensorflow as tf

# package dependencies
from deepface.commons.logger import Logger
from deepface import __version__

logger = Logger(module="commons.package_utils")


def get_tf_major_version() -> int:
    """
    Find tensorflow's major version
    Returns
        major_version (int)
    """
    return int(tf.__version__.split(".", maxsplit=1)[0])


def find_package_version() -> str:
    """
    Find the currenct package version
    Returns:
        version (str)
    """
    version_info = "N/A"
    try:
        version_info = __version__
    except Exception as err:  # pylint: disable=broad-except, unused-variable
        logger.error(f"Exception while getting deepface version: {str(err)}")
    return version_info
