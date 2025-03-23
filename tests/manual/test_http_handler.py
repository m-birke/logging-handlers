import logging

import pytest

from logging_extended_handlers import HTTPHandlerCustomHeader

_BIN_HOST = "<BIN_HOST>"
_BIN_URL = "/"


def _init_http_logger(method: str, headers: list) -> logging.Logger:
    uut = HTTPHandlerCustomHeader(host=_BIN_HOST, url=_BIN_URL, method=method, header_key_value_pairs=headers)
    uut.setLevel(logging.DEBUG)
    log = logging.getLogger("test_http_handler_custom_header")
    log.setLevel(logging.DEBUG)
    log.addHandler(uut)
    return log


@pytest.mark.skip(reason="This test requires a running mockbin server")
def test_empty_get_debug():
    log = _init_http_logger("GET", None)
    log.debug("test debug msg")


@pytest.mark.skip(reason="This test requires a running mockbin server")
def test_1header_get_info():
    log = _init_http_logger("GET", [("headerkey", "headervalue")])
    log.info("test info msg")


@pytest.mark.skip(reason="This test requires a running mockbin server")
def test_2headers_get_warning():
    log = _init_http_logger("GET", [("key1", "value1"),("key2", "value2")])
    log.warning("test warning msg")


@pytest.mark.skip(reason="This test requires a running mockbin server")
def test_empty_post_info():
    log = _init_http_logger("POST", [])
    log.info("test info msg")


@pytest.mark.skip(reason="This test requires a running mockbin server")
def test_1header_post_error():
    log = _init_http_logger("POST", [("headerkey", "headervalue")])
    log.error("test error msg")
