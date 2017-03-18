from setuptools import setup, find_packages

setup(
    name='mercury-parserpy',
    version='0.1',
    description='Mercury Parser Web API',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
