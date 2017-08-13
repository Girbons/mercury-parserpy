import pytest

from unittest import mock

from mercury_parser.client import MercuryParser
from mercury_parser.exceptions import (
    BadRequest,
    Forbidden,
    ResourceNotFound,
    InternalServerError,
    Unauthorized
)

from .utils import API_KEY


URL_TEST = 'https://trackchanges.postlight.com/building-awesome-cms-f034344d8ed'


@mock.patch('mercury_parser.client.requests.get')
def test_parse_article_bad_request(mock_request):
    response = mock.Mock()
    response.status_code = 400
    mock_request.return_value = response
    parser = MercuryParser('1234567890')
    with pytest.raises(BadRequest):
        parser.parse_article(URL_TEST)


@mock.patch('mercury_parser.client.requests.get')
def test_parse_article_with_invalid_key(mock_request):
    response = mock.Mock()
    response.status_code = 401
    mock_request.return_value = response
    parser = MercuryParser('1234567890')
    with pytest.raises(Unauthorized):
        parser.parse_article(URL_TEST)


@mock.patch('mercury_parser.client.requests.get')
def test_parse_article_forbidden_request(mock_request):
    response = mock.Mock()
    response.status_code = 403
    mock_request.return_value = response
    parser = MercuryParser('1234567890')
    with pytest.raises(Forbidden):
        parser.parse_article(URL_TEST)


@mock.patch('mercury_parser.client.requests.get')
def test_parse_article_resource_not_found(mock_request):
    response = mock.Mock()
    response.status_code = 404
    mock_request.return_value = response
    parser = MercuryParser('1234567890')
    with pytest.raises(ResourceNotFound):
        parser.parse_article(URL_TEST)


@mock.patch('mercury_parser.client.requests.get')
def test_parse_article_internal_server_error(mock_request):
    response = mock.Mock()
    response.status_code = 500
    mock_request.return_value = response
    parser = MercuryParser('1234567890')
    with pytest.raises(InternalServerError):
        parser.parse_article(URL_TEST)


def test_parse_article():
    parser = MercuryParser(API_KEY)
    response = parser.parse_article(URL_TEST)
    assert response.json()['title'] == 'Building Awesome\xa0CMS'
    assert response.json()['domain'] == 'trackchanges.postlight.com'
    assert response.json()['lead_image_url'] == 'https://cdn-images-1.medium.com/max/1200/1*zo51eqdjJ_XSU0D8Vm8P9A.png'
    assert response.json()['word_count'] == 397
    assert response.status_code == 200


def test_parse_multiple_articles_with_invalid_key():
    urls = [
        'https://www.wired.com/2017/03/dont-blame-batteries-every-lithium-ion-explosion/',
        'https://www.wired.com/2017/03/siris-not-even-best-iphone-assistant-anymore/',
        'https://www.wired.com/2017/03/phishing-scams-fool-even-tech-nerds-heres-avoid/'
    ]
    parser = MercuryParser('1234567890')
    with pytest.raises(Forbidden):
        parser.parse_multiple_articles(*urls)


def test_parse_multiple_articles():
    urls = [
        'https://www.wired.com/2017/03/dont-blame-batteries-every-lithium-ion-explosion/',
        'https://www.wired.com/2017/03/siris-not-even-best-iphone-assistant-anymore/',
        'https://www.wired.com/2017/03/phishing-scams-fool-even-tech-nerds-heres-avoid/'
    ]
    parser = MercuryParser(API_KEY)
    response = parser.parse_multiple_articles(*urls)
    assert len(response) == 3


def test_parse_multiple_articles_return_empty_list():
    urls = [
        'https://asasasas.com',
        'https://sasasass.com',
        'https://ssaassa.com'
    ]
    parser = MercuryParser(API_KEY)
    response = parser.parse_multiple_articles(*urls)
    assert len(response) == 0
