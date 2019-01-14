from mercury_parser.client import MercuryParser

from .utils import API_KEY


TEST_URL = 'https://trackchanges.postlight.com/building-awesome-cms-f034344d8ed'


def test_parse_article():
    parser = MercuryParser(API_KEY)
    response = parser.parse_article(TEST_URL)
    assert 'Building Awesome CMS' in response.json()['title']
    assert response.json()['domain'] == 'postlight.com'
    assert response.json()['word_count'] == 426
    assert response.status_code == 200


def test_parse_multiple_articles_with_invalid_key():
    urls = [
        'https://www.wired.com/2017/03/dont-blame-batteries-every-lithium-ion-explosion/',
        'https://www.wired.com/2017/03/siris-not-even-best-iphone-assistant-anymore/',
        'https://www.wired.com/2017/03/phishing-scams-fool-even-tech-nerds-heres-avoid/'
    ]
    parser = MercuryParser('1234567890')
    response = parser.parse_multiple_articles(*urls)
    expected = {
        'https://www.wired.com/2017/03/phishing-scams-fool-even-tech-nerds-heres-avoid/': {
            'Message': 'User is not authorized to access this resource with an explicit deny'
        },
        'https://www.wired.com/2017/03/dont-blame-batteries-every-lithium-ion-explosion/': {
            'Message': 'User is not authorized to access this resource with an explicit deny'
        },
        'https://www.wired.com/2017/03/siris-not-even-best-iphone-assistant-anymore/': {
            'Message': 'User is not authorized to access this resource with an explicit deny'}
    }
    assert response == expected


def test_parse_multiple_articles():
    urls = [
        'https://www.wired.com/2017/03/dont-blame-batteries-every-lithium-ion-explosion/',
        'https://www.wired.com/2017/03/siris-not-even-best-iphone-assistant-anymore/',
        'https://www.wired.com/2017/03/phishing-scams-fool-even-tech-nerds-heres-avoid/'
    ]
    parser = MercuryParser(API_KEY)
    response = parser.parse_multiple_articles(*urls)
    assert len(response.keys()) == 3
