class HTTPStatus:
    """
    HTTP Status indicates whether a specific request has been successfully completed.
    """

    def __init__(self, name: str, code: int):
        self._name = name
        self._code = code

    def name(self) -> str:
        "Returns the HTTP Status name"
        return self._name

    def code(self) -> int:
        "Returns the HTTP Status code"
        return self._code


# 1xx STATUS
STATUS_CONTINUE = HTTPStatus("Continue", 100)
STATUS_SWITCHING_PROTOCOLS = HTTPStatus("Switching Protocols", 101)
STATUS_PROCESSING = HTTPStatus("Processing", 102)
STATUS_EARLY_HINTS = HTTPStatus("Early Hints", 103)

# 2XX STATUS
STATUS_OK = HTTPStatus("OK", 200)
STATUS_CREATED = HTTPStatus("Created", 201)
STATUS_ACCEPTED = HTTPStatus("Accepted", 202)
STATUS_NON_AUTHORATIVE_INFO = HTTPStatus("Non Authorative Information", 203)
STATUS_NO_CONTENT = HTTPStatus("No Content", 204)
STATUS_RESET_CONTENT = HTTPStatus("Reset Content", 205)
STATUS_PARTIAL_CONTENT = HTTPStatus("Partial Content", 206)

# 3xx STATUS
STATUS_MULTIPLE_CHOICES = HTTPStatus("Multiple Choices", 300)
STATUS_MOVED_PERMANENTLY = HTTPStatus("Moved Permanently", 301)
STATUS_FOUND = HTTPStatus("Found", 302)
STATUS_SEE_OTHER = HTTPStatus("See Other", 303)
STATUS_NOT_MODIFIED = HTTPStatus("Not Modified", 304)
STATUS_USE_PROXY = HTTPStatus("Use Proxy", 305)
STATUS_UNUSED = HTTPStatus("Unused", 306)
STATUS_TEMPORARY_REDIRECT = HTTPStatus("Temporary Redirect", 307)
STATUS_PERMANENT_REDIRECT = HTTPStatus("Permanent Redirect", 308)

# 4XX STATUS
STATUS_BAD_REQUEST = HTTPStatus("Bad Request", 400)
STATUS_UNAUTHORIZED = HTTPStatus("Unauthorized", 401)
STATUS_PAYMENT_REQUIRED = HTTPStatus("Payment Required", 402)
STATUS_FORBIDDEN = HTTPStatus("Forbidden", 403)
STATUS_NOT_FOUND = HTTPStatus("Not Found", 404)
STATUS_METHOD_NOT_ALLOWED = HTTPStatus("Method Not Allowed", 405)
STATUS_NOT_ACCEPTABLE = HTTPStatus("Not Acceptable", 406)
STATUS_PROXY_AUTH_REQUIRED = HTTPStatus("Proxy Authentication Required", 407)
STATUS_REQUEST_TIMEOUT = HTTPStatus("Request Timeout", 408)
STATUS_CONFLICT = HTTPStatus("Conflict", 409)
STATUS_GONE = HTTPStatus("Gone", 410)
STATUS_LENGTH_REQUIRED = HTTPStatus("Length Required", 411)
STATUS_PRECONDITION_FAILED = HTTPStatus("Precondition Failed", 412)
STATUS_PAYLOAD_TOO_LARGE = HTTPStatus("Payload Too Large", 413)
STATUS_URI_TOO_LONG = HTTPStatus("URI Too Long", 414)
STATUS_UNSUPPORTED_MEDIA_TYPE = HTTPStatus("Unsupported Media Type", 415)
STATUS_RANGE_NOT_SATISFIABLE = HTTPStatus("Range Not Satisfiable", 416)
STATUS_EXPECTATION_FAILED = HTTPStatus("Expectation Failed", 417)
STATUS_IM_A_TEAPOT = HTTPStatus("Im a Teapot", 418)
STATUS_MISDIRECTED_REQUEST = HTTPStatus("Misdirected Request", 421)
STATUS_TOO_EARLY = HTTPStatus("Too Early", 425)
STATUS_UPGRADE_REQUIRED = HTTPStatus("Upgrade Required", 426)
STATUS_PRECONDITION_REQUIRED = HTTPStatus("Precondition Required", 428)
STATUS_TOO_MANY_REQUESTS = HTTPStatus("Too Many Requests", 429)


# 5XX STATUS
STATUS_INTERNAL_SERVER_ERROR = HTTPStatus("Internal Server Error", 500)
STATUS_NOT_IMPLEMENTED = HTTPStatus("Not Implemented", 501)
STATUS_BAD_GATEWAY = HTTPStatus("Bad Gateway", 502)
STATUS_SERVICE_UNAVAILABLE = HTTPStatus("Service Unavailable", 503)
STATUS_GATEWAY_TIMEOUT = HTTPStatus("Gateway Timeout", 504)
STATUS_HTTP_VERSION_NOT_SUPPORTED = HTTPStatus("HTTP Version Not Supported", 505)
STATUS_NETWORK_AUTH_REQUIRED = HTTPStatus("Network Authentication Required", 511)
