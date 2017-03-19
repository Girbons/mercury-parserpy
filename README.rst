Mercury Web Parser Python
=========================

.. image:: https://badge.fury.io/py/mercury-parserpy.svg
    :target: https://badge.fury.io/py/mercury-parserpy
.. image:: https://travis-ci.org/Girbons/MercuryParserpy.svg?branch=master
    :target: https://travis-ci.org/Girbons/MercuryParserpy
.. image:: https://coveralls.io/repos/github/Girbons/MercuryParserpy/badge.svg?branch=master
    :target: https://coveralls.io/github/Girbons/MercuryParserpy?branch=master

Setup
=====

From the command line::

    pip install mercury-parserpy

Usage
=====

example::

    from mercury_parser.client import MercuryParser

    parser = MercuryParser(api_key='YOUR API KEY')
    article = parser.parse_article('ARTICLE_URL')
    article.json()
