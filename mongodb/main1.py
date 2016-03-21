#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Activity import Activity


def main():
    collection_old = 'activities'
    collection_new = 'activity'

    address_old = '192.168.37.128'
    port_old = 27017

    address_new = '192.168.6.254'
    port_new = 37017

    print("convert activity data")
    Activity.convert_activity(address_old, port_old, address_new, port_new,
                              collection_old, collection_new, Activity.params_map)

    print("OK")


if __name__ == "__main__":
    main()
