#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Activity import Activity
from WeatherTranslation import WeatherTranslation
from Pgc import Pgc
from Area import Area
from City import City
from Tag import Tag


def main():
    collection_old = 'activities'
    collection_new = 'activity'

    address_old = '192.168.37.128'
    port_old = 27017

    address_new = '192.168.6.254'
    port_new = 37017

    # City.convert_city(address_old, port_old, address_new, port_new)
    Tag.convert_tag(address_old, port_old, address_new, port_new)

    Area.insert_area(address_old, port_old, address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()
