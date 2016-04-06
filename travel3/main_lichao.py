#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from Restaurant import Restaurant

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    address_old = 'localhost'
    port_old = 27017

    address_new = 'localhost'
    port_new = 27017

    print('convert restaurants to restaurant.')
    Restaurant.convert_restaurant(address_old, port_old, address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()
