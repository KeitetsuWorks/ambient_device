Script to send BME280 data to Ambient
========


## Description

The Python Script to send BME280 data to Ambient.


## Requirement for Raspberry Pi


### Hardware

* [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
* [Akizuki BME280 I2C or SPI Temperature Humidity Pressure Sensor](http://akizukidenshi.com/catalog/g/gK-09421/)


### Software

* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
* Python 3
* [Python Library: smbus2](https://pypi.org/project/smbus2/)
* [Python Library: RPi.bme280](https://pypi.org/project/RPi.bme280/)
* [AmbientDataInc/ambient-python-lib](https://github.com/AmbientDataInc/ambient-python-lib)


## Usage


### Send Temperature Humidity and Pressure to Ambient

    $ cd ~/ambient_device
    (py36) $ python ambient_device.py


## Example installation in pyenv environment

1. Clone this project

        $ cd ~
        $ git clone https://github.com/KeitetsuWorks/ambient_device.git
        $ cd ambient_device

2. Install dependent libraries

        $ pyenv virtualenv 3.6.6 py36
        (py36) $ pyenv local py36
        (py36) $ pip install smbus2
        (py36) $ pip install RPi.bme280
        (py36) $ pip install git+https://github.com/AmbientDataInc/ambient-python-lib.git

3. Make the configuration file, `ambient.json`

        (py36) $ vi ambient.json

    Please write your channel ID and your write key in JSON format.

        {
            "ambient": {
                "channelId": "your_channel_id",
                "writeKey": "your_write_key"
            }
        }

4. (Optional) Edit cron for periodic execution

        $ crontab -e

    `ambient_device.sh` is shell script to run `ambient_device.py` using pyenv environment from crond.

        2-57/5 * * * * cd ~/ambient_device; ./ambient_device.sh


## License

* MIT
