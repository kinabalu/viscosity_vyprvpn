#!/usr/bin/env python

from string import Template
import os
import shutil

server_locations = [
    ['Los Angeles, CA', 'us1.vpn.giganews.com'],
    ['Washington, DC', 'us2.vpn.giganews.com'],
    ['Austin, TX', 'us3.vpn.giganews.com'],
    ['Miami, FL', 'us4.vpn.giganews.com'],
    ['Toronto', 'ca1.vpn.giganews.com'],
    ['Amsterdam', 'eu1.vpn.giganews.com'],
    ['Stockholm', 'se1.vpn.giganews.com'],
    ['Hong Kong', 'hk1.vpn.giganews.com'],
    ['London', 'uk1.vpn.giganews.com'],
    ['Paris', 'fr1.vpn.giganews.com'],
    ['Frankfurt', 'de1.vpn.giganews.com'],
    ['Copenhagen', 'dk1.vpn.giganews.com'],
    ['Zurich', 'ch1.vpn.giganews.com'],
    ['Moscow', 'ru1.vpn.giganews.com'],
    ['Luxembourg', 'lu1.vpn.giganews.com'],
    ['Bucharest', 'ro1.vpn.giganews.com'],
    ['Singapore', 'sg1.vpn.giganews.com'],
    ['Dublin', 'ie1.vpn.giganews.com'],
    ['Kuala Lumpur', 'my1.vpn.giganews.com'],
    ['Rome', 'it1.vpn.giganews.com'],
    ['Madrid', 'es1.vpn.giganews.com'],
    ['Tokyo', 'jp1.vpn.giganews.com'],
    ['Seoul', 'kr1.vpn.giganews.com'],
    ['Oslo', 'no1.vpn.giganews.com'],
    ['Istanbul', 'tr1.vpn.giganews.com'],
    ['Helsinki', 'fi1.vpn.giganews.com'],
    ['Warsaw', 'pl1.vpn.giganews.com'],
    ['Lisbon', 'pt1.vpn.giganews.com'],
    ['Prague', 'cz1.vpn.giganews.com'],
    ['Vienna', 'at1.vpn.giganews.com'],
    ['Brussels', 'be1.vpn.giganews.com'],
    ['Vilnius', 'lt1.vpn.giganews.com'],
    ['Sydney', 'au1.vpn.giganews.com'],
    ['Melbourne', 'au2.vpn.giganews.com'],
    ['Perth', 'au3.vpn.giganews.com'],
    ['Jakarta', 'id1.vpn.giganews.com'],
    ['Auckland', 'nz1.vpn.giganews.com'],
    ['Hanoi', 'vn1.vpn.giganews.com'],
    ['Bangkok', 'th1.vpn.giganews.com'],
    ['Reykjavik', 'is1.vpn.giganews.com'],
    ['Manila','ph1.vpn.giganews.com']
]


def main():
    os.mkdir("data")
    file = open('config.conf', 'r')
    data = file.read()
    s = Template(data)

    count = 1
    for location in server_locations:
        path = "data/%s/" % (count,)
        os.mkdir(path)
        r = s.substitute(name=location[0], server=location[1])
        file = open(path + "config.conf", "w")
        file.write(r)
        file.close()

        shutil.copyfile("ca.crt", path + "ca.crt")
        count += 1


if __name__ == '__main__':
    main()


