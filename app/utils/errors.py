class JsonApiException(Exception):
    """Base exception class for unknown errors"""

    title = "Unknown error"
    status = "500"
    source = None

    def __init__(
        self,
        detail,
        source=None,
        title=None,
        status=None,
        code=None,
        id_=None,
        links=None,
        meta=None,
    ):
        """Initialize a jsonapi exception

        :param dict source: the source of the error
        :param str detail: the detail of the error
        """
        self.detail = detail
        self.source = source
        self.code = code
        self.id = id_
        self.links = links or {}
        self.meta = meta or {}
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status

    def to_dict(self):
        """Return values of each fields of an jsonapi error"""
        error_dict = {}
        for field in (
            "status",
            "source",
            "title",
            "detail",
            "id",
            "code",
            "links",
            "meta",
        ):
            if getattr(self, field, None):
                error_dict.update({field: getattr(self, field)})

        return error_dict


class TunnelError(JsonApiException):
    """Raised when there is an error creating/deleting a tunnel"""

    title = "Tunnel Error"
    status = "500"


class SubdomainError(JsonApiException):
    """Raised when there is an error creating/deleting a tunnel"""

    title = "Subdomain Error"
    status = "500"
    detail = "Database error when changing subdomains"


class NotFoundError(JsonApiException):
    """Raised when there is an error creating/deleting a tunnel"""

    title = "Not Found Error"
    detail = "Not Found"
    status = "404"


class UnprocessableEntity(JsonApiException):
    """Raised when the request has the correct syntax, but is semantically incorrect"""

    title = "Unprocessable Entity"
    detail = "Unprocessable Entity"
    status = "422"


class BadRequest(JsonApiException):
    """BadRequest error"""

    title = "Bad request"
    detail = "Request does not match a known schema"
    status = "400"


class SubdomainTaken(JsonApiException):
    """SubdomainTaken error"""

    title = "Subdomain Taken"
    detail = "Subdomain has already been reserved"
    status = "400"


class SubdomainInUse(JsonApiException):
    """SubdomainTaken error"""

    title = "Subdomain is being used"
    detail = "Subdomain is associated with a running tunnel"
    status = "403"


class AccessDenied(JsonApiException):
    """Throw this error when user does not have access"""

    title = "Access denied"
    detail = "Access denied"
    status = "403"


class UserNotConfirmed(JsonApiException):
    """Throw this error when user has not confirmed their email"""

    title = "Unconfirmed User"
    detail = "Must confirm email before you use the service"
    status = "403"


class ConsulLockException(JsonApiException):
    # Extends the base ConsulException in case caller wants to group the exception handling together
    title = "ConsulLockException"
    status = "500"


class LockAcquisitionException(JsonApiException):
    title = "LockAcquisitionException"
    status = "500"
