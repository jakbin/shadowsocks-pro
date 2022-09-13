shadowsocks
===========

 [![PyPI version](https://badge.fury.io/py/shadowsocks-pro.svg)](https://pypi.org/project/shadowsocks-pro/)
 [![Downloads](https://pepy.tech/badge/shadowsocks-pro/month)](https://pepy.tech/project/shadowsocks-pro)
 [![Downloads](https://static.pepy.tech/personalized-badge/shadowsocks-pro?period=total&units=international_system&left_color=green&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/shadowsocks-pro)

A fast tunnel proxy that helps you bypass firewalls.

Features:
- TCP & UDP support
- User management API
- TCP Fast Open
- Workers and graceful restart
- Destination IP blacklist

Server
------

### Install

Debian / Ubuntu:

    apt-get install python-pip
    pip install shadowsocks

CentOS:

    yum install python-setuptools && easy_install pip
    pip install shadowsocks

Windows:

See [Install Shadowsocks Server on Windows](https://github.com/shadowsocks/shadowsocks/wiki/Install-Shadowsocks-Server-on-Windows).

### Usage

    ssserver -p 443 -k password -m aes-256-cfb

To run in the background:

    sudo ssserver -p 443 -k password -m aes-256-cfb --user nobody -d start

To stop:

    sudo ssserver -d stop

To check the log:

    sudo less /var/log/shadowsocks.log

Check all the options via `-h`. You can also use a [Configuration] file
instead.

### Usage with Config File

[Create configeration file and run](https://github.com/shadowsocks/shadowsocks/wiki/Configuration-via-Config-File)

To start:

    ssserver -c /etc/shadowsocks.json


Documentation
-------------

You can find all the documentation in the [Wiki](https://github.com/shadowsocks/shadowsocks/wiki).

License
-------

MIT License
