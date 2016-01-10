#!/bin/sh

if [ `id -u` -ne 0 ]; then
    echo "This script must be run as root"
    exit 1
fi

mon_device=/dev/i2c-3

_5400() {
    sudo ddccontrol -r 0x14 -w 4 -s dev:$mon_device > /dev/null
    sudo ddccontrol -r 0x0C -w 24 -s dev:$mon_device > /dev/null
}

_6500() {
    sudo ddccontrol -r 0x14 -w 5 -s dev:$mon_device > /dev/null
    sudo ddccontrol -r 0x0C -w 35 -s dev:$mon_device > /dev/null
}

hour=`date +%H`
if [ $hour -ge 19 ] && [ $hour -le 2 ]; then
    _5400
else
    _6500
fi
