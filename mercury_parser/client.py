import json

from typing import Any, Dict, List
from dataclasses import dataclass

import requests


# default api_endpoint
API_ENDPOINT = "http://localhost:3000/"


@dataclass
class MercuryParser:
    api_key: str = None
    api_endpoint: str = API_ENDPOINT

    def __post_init__(self):
        self.headers = {"x-api-key": self.api_key}

    def parse_article(self, article_url: str) -> Dict[str, Any]:
        """
        Parse article URL returns a requests.Response
        """
        url = "{}parser?url={}".format(self.api_endpoint, article_url)
        response = requests.get(url, headers=self.headers)
        return response

    def parse_multiple_articles(self, urls: List[str]) -> List[Dict[str, Any]]:
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
