#!/usr/bin/env python
from setuptools import setup, find_packages
from kademlia3 import version

setup(
    name="kademlia3",
    version=version,
    description="Kademlia is a distributed hash table for decentralized peer-to-peer computer networks.",
    author="luxcem, Brian Muller",
    author_email="a@luxcem.fr",
    license="MIT",
    url="http://github.com/luxcem/kademlia",
    packages=find_packages(),
    requires=["twisted", "rpcudp"],
    install_requires=['twisted>=14.0', "rpcudp>=1.0"]
)
