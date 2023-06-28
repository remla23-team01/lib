from setuptools import setup, find_packages
import json

ver = ""
with open("remla01_lib/version.json", "r") as versionfile:
    version_json = json.load(versionfile)
    ver = version_json['version']

setup(
    name="remla01_lib",
    version=ver,
    description="Library for ML steps for REMLA23",
    url="https://github.com/remla23-team01/lib",
    packages=find_packages(),
)