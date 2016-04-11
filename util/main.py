#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from ChangeId import ChangeId 

def main():
    address = '123.56.65.17'
    port = 27017

    ChangeId.update_city_id(address, port)


if __name__ == "__main__":
    main()
