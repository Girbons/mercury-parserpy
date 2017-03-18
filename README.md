# Mercury Web Parser Python
[![Build Status](https://travis-ci.org/Girbons/MercuryParserpy.svg?branch=master)](https://travis-ci.org/Girbons/MercuryParserpy)
[![Coverage Status](https://coveralls.io/repos/github/Girbons/MercuryParserpy/badge.svg?branch=master)](https://coveralls.io/github/Girbons/MercuryParserpy?branch=master)


```python
from mercury_parser.client import MercuryParser

parser = MercuryParser('TOKEN')
article = parser.parse_article('ARTICLE_URL')
article.json()
```
