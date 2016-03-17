#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Label import Label


def main():
    address_old = '192.168.37.128'
    port_old = 27017

    address_new = '192.168.37.128'
    port_new = 27017

    print("convert label data")
    Label.convert_label(address_old, port_old, address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()
