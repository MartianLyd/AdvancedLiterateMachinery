# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         settings.py
# Author:       liyd
# Version:      Python 3.8.16
# Created:      2023/11/03 15:20
# Description:  项目配置模块
# -------------------------------------------------------------------------------
# !/usr/bin/env python

import os
import configparser
import platform
from pathlib import Path


sys = platform.system()

# settings.py Path
cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path, 'config.ini')
conf = configparser.ConfigParser()
conf.read(config_path, encoding="utf-8-sig")

# -------------------------------- Log Configuration --------------------------
"""
project_path = Path.cwd().parent
log_path = Path(project_path, "logs")
"""
# D:/workspace/
ROOT_PATH = cur_path.replace('config', '').replace('\\', '/')

# ----------------------------- Application Configuration ---------------------
APPLICATIONS_PORT = conf.get('DOCUMENT_VGT', 'APPLICATIONS_PORT')
