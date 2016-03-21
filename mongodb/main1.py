#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from WeatherTranslation import WeatherTranslation


def main():
    address_new = '192.168.6.254'
    port_new = 37017

    WeatherTranslation.insert_weather_translation(address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()
