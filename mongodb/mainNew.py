#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Area import Area


# 插入新增数据，这部分数据不需要从老库导入
def main():
    address_old = '192.168.37.128'
    port_old = 27017

    address_new = '192.168.37.128'
    port_new = 27017

    Area.insert_area(address_old, port_old, address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()
