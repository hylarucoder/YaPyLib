import json
import os
import shutil
import sys
import importlib
import itertools
import traceback
import datetime

import yaml


def register_error_handlers():
    pass


def register_logger():
    pass


def create_app(config=None):
    config = config or {}

    config_path = os.environ.get("YAPYLIB_SETTINGS", None)
    if config_path:
        with open(config_path, "rt") as f:
            yml_config = (yaml.load(f))
        config = {**yml_config, **config}
    config.update(config)
    register_error_handlers()
    register_logger()
    pass
