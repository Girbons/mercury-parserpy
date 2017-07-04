import requests
import json

from .exceptions import InvalidApiKey


class MercuryParser:
    def __init__(self, api_key):
        self.api_key = api_key
        self._headers = {'x-api-key': self.api_key}

    def parse_article(self, article_url):
        """
        Parse article URL
        """
        api_request = 'https://mercury.postlight.com/parser?url={}'.format(article_url)
        response = requests.get(api_request, headers=self._headers)
        if response.status_code == 401:
            raise InvalidApiKey('{} Unauthorized'.format(response.status_code))
        return response

    def parse_multiple_articles(self, *urls):
        """
        Parse a list of urls return a JSON
        """
        parsed_articles = []
        session = requests.Session()
        for url in urls:
            api_request = 'https://mercury.postlight.com/parser?url={}'.format(url)
            response = session.get(api_request, headers=self._headers)
            if response.status_code == 401:
                raise InvalidApiKey('{} Unauthorized'.format(response.status_code))
            if response.ok:
                parsed_articles.append(response.json())
        response = json.loads(json.dumps(parsed_articles))
        return response
