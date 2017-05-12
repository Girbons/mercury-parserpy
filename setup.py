from setuptools import setup, find_packages


setup(
    name="mercury-parserpy",
    version="0.2",
    description="Mercury Parser Web API",
    long_description=open('README.rst').read(),
    author="Alessandro De Angelis",
    author_email="alessandrodea22@gmail.com",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    license="MIT",
    url="https://github.com/Girbons/mercury-parserpy",
)
