# mercury-parserpy

[![Build Status](https://travis-ci.org/Girbons/mercury-parserpy.svg?branch=master)](https://travis-ci.org/Girbons/mercury-parserpy)


## Getting Started

From the command line:

```
pip install mercury-parserpy
```

## Usage

```python
from mercury_parser.client import MercuryParser

# default api endpoint is http://localhost:3000/
parser = MercuryParser()
article = parser.parse_article('ARTICLE_URL')
article.json()

# parse multiple articles urls return a JSON
# where the key is the article url
articles = parser.parse_multiple_articles(*ARTICLES_URLS)
```

### Customize API Endpoint

```python
from mercury_parser.client import MercuryParser

parser = MercuryParser(api_endpoint="http://api-endpoint/")
```
