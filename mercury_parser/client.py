import requests
import json


# default api_endpoint
API_ENDPOINT = "http://localhost:3000/"


class MercuryParser:
    def __init__(self, api_endpoint=API_ENDPOINT, api_key=None):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.headers = {"x-api-key": self.api_key}

    def parse_article(self, article_url):
        """
        Parse article URL returns a requests.Response
        """
        url = "{}parser?url={}".format(self.api_endpoint, article_url)
        response = requests.get(url, headers=self.headers)
        return response

    def parse_multiple_articles(self, *urls):
        """
        Parse a list of urls
        returns a dict where the key is the article url
        """
        parsed_articles = {}
        session = requests.Session()
        for url in urls:
            url = "{}parser?url={}".format(self.api_endpoint, url)
            response = session.get(url, headers=self.headers)
            parsed_articles[url] = response.json()

        response = json.loads(json.dumps(parsed_articles))
        return response
