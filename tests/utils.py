import os


def get_api_key():
    try:
        return os.environ['API_KEY']
    except KeyError:
        raise ('API KEY not set')


API_KEY = get_api_key()
