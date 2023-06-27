from setuptools import setup, find_packages
import json

versionfile = json.load("remla01_lib/version.json")
ver = versionfile['version']

setup(
    name="remla01_lib",
    version=ver,
    description="Library for ML steps for REMLA23",
    url="https://github.com/remla23-team01/lib",
    packages=find_packages(),
)