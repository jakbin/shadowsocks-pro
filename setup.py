import codecs
from setuptools import setup


with codecs.open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="shadowsocks-pro",
    version="1.0.0",
    license="MIT License",
    description="A fast tunnel proxy that help you get through firewalls",
    author='jakbin',
    author_email='jakbin4747@gmail.com',
    url='https://github.com/jakbin/shadowsocks-pro',
    packages=['shadowsocks', 'shadowsocks.crypto'],
    package_data={
        'shadowsocks': ['README.md', 'LICENSE']
    },
    install_requires=[],
    entry_points="""
    [console_scripts]
    sslocal = shadowsocks.local:main
    ssserver = shadowsocks.server:main
    """,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)
