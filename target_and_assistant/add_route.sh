#!/bin/sh
ip route add 10.190.4.137 via 192.168.1.11 dev eth0

exec "$@"
