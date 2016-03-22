#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Activity import Activity
from WeatherTranslation import WeatherTranslation
from Pgc import Pgc
from Area import Area
from City import City
from Tag import Tag
from Person import Person


def main():
    collection_old = 'activities'
    collection_new = 'activity'

    address_old = '192.168.37.128'
    port_old = 27017

    address_new = '192.168.6.254'
    port_new = 37017

    Person.convert_person(address_old, port_old, address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()
