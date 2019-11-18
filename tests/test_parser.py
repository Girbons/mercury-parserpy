from mercury_parser.client import MercuryParser


def test_parse_article():
    parser = MercuryParser()
    response = parser.parse_article(
        "https://medium.com/swlh/alexa-play-some-music-isnt-the-only-time-amazon-is-listening-to-you-a556df19613f"
    )  # noqa
    assert "Alexa, play some music" in response.json()["title"]
    assert response.json()["domain"] == "medium.com"
    assert response.status_code == 200


def test_parse_multiple_articles():
    urls = [
        "https://www.wired.com/2017/03/dont-blame-batteries-every-lithium-ion-explosion/",
        "https://www.wired.com/2017/03/siris-not-even-best-iphone-assistant-anymore/",
        "https://www.wired.com/2017/03/phishing-scams-fool-even-tech-nerds-heres-avoid/",
    ]
    parser = MercuryParser()
    response = parser.parse_multiple_articles(*urls)
    assert len(response.keys()) == 3
