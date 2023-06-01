from setuptools import setup, find_packages
from remla01_lib import version

setup(
    name="remla01_lib",
    version=version,
    description="Library for ML steps for REMLA23",
    url="https://github.com/remla23-team01/lib",
    packages=find_packages(),
)