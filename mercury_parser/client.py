import requests
import json

from .exceptions import ParserError, InvalidApiKey


class MercuryParser:
    def __init__(self, api_key):
        self.api_key = api_key
        self._headers = {'x-api-key': self.api_key}

    def validate_api_key(self):
        """
        Check if api key is valid
        """
        url = 'https://trackchanges.postlight.com/building-awesome-cms-f034344d8ed'
        api_request = 'https://mercury.postlight.com/parser?url={}'.format(url)
        response = requests.get(api_request, headers=self._headers)
        if response.status_code is not 200:
            raise InvalidApiKey('{} Unauthorized'.format(response.status_code))
        return response

    def parse_article(self, article_url):
        """
        Parse article URL
        """
        self.validate_api_key()
        api_request = 'https://mercury.postlight.com/parser?url={}'.format(article_url)
        response = requests.get(api_request, headers=self._headers)
        if response.json():
            return response
        else:
            raise ParserError('Error while parsing url: {}'.format(article_url))

    def parse_multiple_articles(self, *urls):
        """
        Parse a list of urls in JSON
        """
        self.validate_api_key()
        parsed_articles = []
        session = requests.Session()
        for url in urls:
            api_request = 'https://mercury.postlight.com/parser?url={}'.format(url)
            response = session.get(api_request, headers=self._headers)
            if response.json():
                parsed_articles.append(response.json())
        response = json.loads(json.dumps(parsed_articles))
        return response
