import http.client

import pytest
from pytest_socket import SocketBlockedError

from logging_extended_handlers import BufferingSMTPHandler, HTTPHandlerCustomHeader


@pytest.mark.dependency(name="ensure_socket_blocked")
def test_socket_blocked(fixt_test_host):
    connection = http.client.HTTPConnection(host=fixt_test_host)

    with pytest.raises(SocketBlockedError):
        connection.request("GET", "/")


@pytest.mark.dependency(depends=["ensure_socket_blocked"])
def test_smtp_handler_init():
    BufferingSMTPHandler("myhost", "sender@com.com", ["recp@com.com"], "test", 999)


@pytest.mark.dependency(depends=["ensure_socket_blocked"])
def test_http_handler_init():
    HTTPHandlerCustomHeader("bin657rfgdiol123.com", "", header_key_value_pairs=[("k1", "v1")])
