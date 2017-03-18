# Mercury Web Parser Python


```python
from mercury_parser.client import MercuryParser

parser = MercuryParser('TOKEN')
article = parser.parse_article('ARTICLE_URL')
article.json()
```
