from setuptools import setup
import json

versionfile = json.load("version.json")
ver = versionfile['version']

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Preprocessing-Library',
    url='https://github.com/remla23-team01/lib',
    author='Remla Team 01 ',
    author_email='test@remla.com',
    packages=['preprocessing'],
    install_requires=['numpy'],
    version=ver,
    license='REMLA01',
    description='This library contains the preprocessing functions for the REMLA project used in model-service and model-training.',
    long_description=open('README.txt').read(),
)