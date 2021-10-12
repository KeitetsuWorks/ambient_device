#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
## @file        ambient_device.py
## @brief       Script to send BME280 data to Ambient
## @author      Keitetsu
## @date        2021/10/12
## @copyright   Copyright (c) 2021 Keitetsu
## @par         License
##              This software is released under the MIT License.
##

import json
import ambient

import smbus2
import bme280
import time


def post_BME280Data_to_Ambient(data):
    with open('ambient.json', 'r') as f:
        dict_configs = json.load(f)

    str_channelId = dict_configs['ambient']['channelId']
    str_writeKey = dict_configs['ambient']['writeKey']
    am = ambient.Ambient(str_channelId, str_writeKey)

    dict_data = {
        "created": time.strftime("%Y-%m-%d %H:%M:%S"),
        "d1": data.temperature,
        "d2": data.humidity,
        "d3": data.pressure
    }

    print("begin request")
    r = am.send(dict_data)
    print("response status code: %d" % (r.status_code))
    if r.status_code == 200:
        print("response text: %s" % (r.text))
        ret_val = True
    else:
        ret_val = False
    print("end request")

    return ret_val


if __name__ == '__main__':
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)

    calibration_params = bme280.load_calibration_params(bus, address)

    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, address, calibration_params)

    for i in range(0, 5):
        result = post_BME280Data_to_Ambient(data)
        if result == True:
            break
        time.sleep(2)

