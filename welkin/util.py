import logging
import requests
from requests import HTTPError


##export PYTHONWARNINGS="ignore:Unverified HTTPS request"

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger("welkin")
logger.setLevel(logging.DEBUG)

# create handlers and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler('welkin.log')
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

__all__ = [
    "log_info",
    "log_debug",
]


def log_info(message, **params):
    logger.info(message)


def log_debug(message, **params):
    logger.debug(message)


def process_request(url, headers=None, json_data=None, params=None, data=None, method='get'):
    """
    :param json_data:
    :param url: string (fully qualified URL)
    :param headers: dict
    :param params: dict
    :param data: dict
    :param method: string (get, post, delete, patch, head, options)
    :return: class: requests.models.Response
    """

    if headers is None:
        headers = {}
    r = None
    try:
        r = requests.request(method=method, url=url, headers=headers, params=params, data=data, json=json_data,
                             verify=False)

        # ppr.pprint_response(r)  # for testing the response
        response_string = 'Invalid Token.'
        if r.ok:
            # NOTE: r.ok if status code between 200 and 399 (same as if r)
            return r
        else:
            # HTTPError will be raised for 4XX client errors or 5XX server errors. No raise if successful 2XX
            r.raise_for_status()

    except HTTPError as http_err:
        if r.status_code == 401:  # Invalid authorization
            return r
        elif r.status_code == 404:  # Resource not found
            return r
        elif r.status_code == 400:  # Resource not found
            return r
        else:
            # other 4XX and 5XX errors
            raise  # try again

    except Exception as err:  # timeouts, server errors, etc.
        raise  # try again
