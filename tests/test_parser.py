from mercury_parser.client import MercuryParser

from .utils import API_KEY


def test_parse_article():
    parser = MercuryParser(API_KEY)
    response = parser.parse_article('https://medium.com/swlh/alexa-play-some-music-isnt-the-only-time-amazon-is-listening-to-you-a556df19613f') # noqa
    assert 'Alexa, play some music' in response.json()['title']
    assert response.json()['domain'] == 'medium.com'
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
