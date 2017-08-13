import requests
import json

from .exceptions import (
    BadRequest,
    Forbidden,
    InternalServerError,
    ResourceNotFound,
    Unauthorized
)


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
        return self.handle_response(response)

    def parse_multiple_articles(self, *urls):
        """
        Parse a list of urls return a JSON
        """
        parsed_articles = []
        session = requests.Session()
        for url in urls:
            api_request = 'https://mercury.postlight.com/parser?url={}'.format(url)
            response = session.get(api_request, headers=self._headers)
            if self.handle_response(response):
                parsed_articles.append(response.json())
        response = json.loads(json.dumps(parsed_articles))
        return response

    def handle_response(self, response):
        status_code = response.status_code
        if 200 <= status_code <= 299:
            return response
        elif status_code == 400:
            raise BadRequest
        elif status_code == 401:
            raise Unauthorized
        elif status_code == 403:
            raise Forbidden
        elif status_code == 404:
            raise ResourceNotFound
        elif status_code == 500:
            raise InternalServerError
