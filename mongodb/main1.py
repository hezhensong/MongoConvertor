#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Activity import Activity
from WeatherTranslation import WeatherTranslation


def main():
    collection_old = 'activities'
    collection_new = 'activity'

    address_old = '192.168.37.128'
    port_old = 27017

    address_new = '192.168.6.254'
    port_new = 37017

    Pgc.convert_pgc(address_old, port_old, address_new, port_new, collection_old, collection_new, params_map)

    print("OK")


if __name__ == "__main__":
    main()
