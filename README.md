shadowsocks
===========

 [![PyPI version](https://badge.fury.io/py/shadowsocks-pro.svg)](https://pypi.org/project/shadowsocks-pro/)
 [![Downloads](https://pepy.tech/badge/shadowsocks-pro/month)](https://pepy.tech/project/shadowsocks-pro)
 [![Downloads](https://static.pepy.tech/personalized-badge/shadowsocks-pro?period=total&units=international_system&left_color=green&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/shadowsocks-pro)

A fast tunnel proxy that helps you bypass firewalls.

## Main focus on shadowsocks client

Features:
- TCP & UDP support
- User management API
- TCP Fast Open
- Workers and graceful restart
- Destination IP blacklist


Client
------

### Install

Debian / Ubuntu:
```sh
apt install python3-pip libcrypto++-dev
```
```sh
pip3 install shadowsocks-pro
```
### Usage
```sh
sslocal -c config.json
```

### Config.json example
```json
{
    "server": "example.shadowsocks.org",
    "server_port": 8388,
    "password": "u1rRWTssNv0p",
    "method": "aes-256-cfb",
    "timeout":400,
    "local_address": "127.0.0.1",
    "local_port":1080
 }
 ```

## Tutorial
[Watch Here](https://youtu.be/sRarEzteWRE)

Server
------

### Install

Debian / Ubuntu:
```sh
    apt install python3-pip libcrypto++-dev
    pip install shadowsocks-pro
```
CentOS:
```sh
    yum install python-setuptools && easy_install pip
    pip install shadowsocks-pro
```
Windows:

See [Install Shadowsocks Server on Windows](https://github.com/shadowsocks/shadowsocks/wiki/Install-Shadowsocks-Server-on-Windows).

### Usage
```sh
ssserver -p 443 -k password -m aes-256-cfb
```
To run in the background:
```sh
sudo ssserver -p 443 -k password -m aes-256-cfb --user nobody -d start
```
To stop:
```sh
sudo ssserver -d stop
```
To check the log:
```sh
sudo less /var/log/shadowsocks.log
```
Check all the options via `-h`. You can also use a [Configuration] file
instead.

### Usage with Config File

[Create configeration file and run](https://github.com/shadowsocks/shadowsocks/wiki/Configuration-via-Config-File)

To start:
```sh
ssserver -c /etc/shadowsocks.json
```

Documentation
-------------

You can find all the documentation in the [Wiki](https://github.com/shadowsocks/shadowsocks/wiki).

License
-------

MIT License
