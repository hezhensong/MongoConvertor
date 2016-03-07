#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from City import City


def main():
    address_old = 'localhost'
    port_old = 27017
    address_new = '192.168.1.113'
    port_new = 27017

    City.convert_city(address_old, port_old, address_new, port_new)


if __name__ == "__main__":
    main()
