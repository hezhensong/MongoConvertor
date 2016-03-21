#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Label import Label
from City import City
from Area import Area
from Tag import Tag


def main():
    address_old = '192.168.37.128'
    port_old = 27017

    address_new = '192.168.37.128'
    port_new = 27017

    # 城市表 依赖新导入的Label表，需保证City前导入Label
    print("convert city data")
    City.convert_city(address_old, port_old, address_new, port_new)

    Label.convert_label(address_old, port_old, address_new, port_new)

    Tag.convert_tag(address_old, port_old, address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()
