#!/bin/bash -eu

##
## @file        ambient_device.sh
## @brief       Script to send BME280 data to Ambient
## @author      Keitetsu
## @date        2021/10/12
## @copyright   Copyright (c) 2021 Keitetsu
## @par         License
##              This software is released under the MIT License.
##

export ENV_NAME=py36
export VIRTUALENV_PATH=/home/keita/.pyenv/versions/${ENV_NAME}
source ${VIRTUALENV_PATH}/bin/activate
python ambient_device.py
