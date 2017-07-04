from setuptools import setup, find_packages
import os
import re


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


VERSION = get_version('mercury_parser')
LONG_DESCRIPTION = open('README.rst').read()


setup(
    name="mercury-parserpy",
    version=VERSION,
    description="Mercury Parser Web API",
    long_description=LONG_DESCRIPTION,
    author="Alessandro De Angelis",
    author_email="alessandrodea22@gmail.com",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    license="MIT",
    url="https://github.com/Girbons/mercury-parserpy",
)
