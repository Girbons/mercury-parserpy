import pytest

from ..client import MercuryParser
from ..exceptions import InvalidApiKey, ParserError


API_KEY_TEST = 'CJF8X9y9tKxFWpd70WgAics4G6pePqOKoSYT4Pwn'
URL_TEST = 'https://trackchanges.postlight.com/building-awesome-cms-f034344d8ed'


def test_parser_with_invalid_key():
    parser = MercuryParser('1234567890')
    with pytest.raises(InvalidApiKey) as ex:
        parser.validate_api_key()
    assert '401 Unauthorized' in str(ex.value)


def test_parser_with_valid_key():
    parser = MercuryParser(API_KEY_TEST)
    response = parser.validate_api_key()
    assert response.status_code == 200


def test_parse_article_with_invalid_key():
    parser = MercuryParser('1234567890')
    with pytest.raises(InvalidApiKey) as ex:
        parser.parse_article(URL_TEST)
    assert '401 Unauthorized' in str(ex.value)


def test_parse_fake_url():
    parser = MercuryParser(API_KEY_TEST)
    with pytest.raises(ParserError) as ex:
        parser.parse_article('http://asadfdf.net/')
    assert 'Error while parsing url: http://asadfdf.net/' in str(ex.value)


def test_parse_article():
    parser = MercuryParser(API_KEY_TEST)
    response = parser.parse_article(URL_TEST)
    assert response.status_code == 200
