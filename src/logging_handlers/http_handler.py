from logging import LogRecord
from logging.handlers import HTTPHandler
from ssl import SSLContext


class HTTPHandlerCustomHeader(HTTPHandler):
    def __init__(self, host: str, url: str, method: str = "GET", secure: bool = False, header_key_value_pairs: list[tuple[str, str]] | None = None, context: SSLContext | None = None) -> None:
        super().__init__(host=host, url=url, method=method, secure=secure, credentials=None, context=context)
        self.header_key_value_pairs = header_key_value_pairs

    def emit(self, record: LogRecord) -> None:
        """
        Emit a record.

        Send the record to the web server as a percent-encoded dictionary

        header_key_value_pairs represents arbitrary keay value pairs which are put into the header
        """
        try:
            import urllib.parse
            host = self.host
            h = self.getConnection(host, self.secure)
            url = self.url
            data = urllib.parse.urlencode(self.mapLogRecord(record))
            if self.method == "GET":
                if (url.find('?') >= 0):
                    sep = '&'
                else:
                    sep = '?'
                url = url + "%c%s" % (sep, data)
            h.putrequest(self.method, url)
            # support multiple hosts on one IP address...
            # need to strip optional :port from host, if present
            i = host.find(":")
            if i >= 0:
                host = host[:i]
            if self.method == "POST":
                h.putheader("Content-type",
                            "application/x-www-form-urlencoded")
                h.putheader("Content-length", str(len(data)))
            for key, value in self.header_key_value_pairs:
                import base64
                k = base64.b64encode(key.encode('utf-8')).strip().decode('ascii')
                v = base64.b64encode(value.encode('utf-8')).strip().decode('ascii')
                h.putheader(k, v)
            h.endheaders()
            if self.method == "POST":
                h.send(data.encode('utf-8'))
            h.getresponse()
        except Exception:
            self.handleError(record)
