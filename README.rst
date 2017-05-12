=========================
Mercury Web Parser Python
=========================

.. image:: https://travis-ci.org/Girbons/mercury-parserpy.svg?branch=master
    :target: https://travis-ci.org/Girbons/mercury-parserpy
.. image:: https://coveralls.io/repos/github/Girbons/MercuryParserpy/badge.svg?branch=master
    :target: https://coveralls.io/github/Girbons/MercuryParserpy?branch=master
.. image:: https://requires.io/github/Girbons/mercury-parserpy/requirements.svg?branch=master
    :target: https://requires.io/github/Girbons/mercury-parserpy/requirements/?branch=master
    :alt: Requirements Status

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
