#!/bin/bash
set -x
ls ${DL_PLATFORM_PROJECT_DATA_PATH}/klane-cswin
ls ${DL_PLATFORM_PROJECT_PATH}

ln -sf ${DL_PLATFORM_PROJECT_DATA_PATH}/klane-cswin/data ./data
ln -sf ${DL_PLATFORM_PROJECT_PATH}/klane-cswin/logs ./logs
# ln -sf ${DL_PLATFORM_PROJECT_DATA_PATH}/klane-cswin/configs ./configs

ls ./data
ls ./logs

python validate_gpu_0.py
