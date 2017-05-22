=========================
Mercury Web Parser Python
=========================

.. image:: https://img.shields.io/travis/Girbons/mercury-parserpy/master.svg?style=flat-square
    :target: https://travis-ci.org/Girbons/mercury-parserpy
    :alt: Build Status
.. image:: https://img.shields.io/coveralls/Girbons/mercury-parserpy/master.svg?style=flat-square
    :target: https://coveralls.io/github/Girbons/mercury-parserpy?branch=master
    :alt: Test Coverage

Setup
=====

From the command line::

    pip install mercury-parserpy

Usage
=====

.. code-block:: python

    from mercury_parser.client import MercuryParser

    parser = MercuryParser(api_key='YOUR API KEY')
    article = parser.parse_article('ARTICLE_URL')
    article.json()

    # parse multiple articles urls return a JSON
    articles = parser.parse_multiple_articles(*ARTICLES_URLS)
