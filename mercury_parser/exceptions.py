

class BadRequest(Exception):
    """
    400 Bad Request
    """


class Unauthorized(Exception):
    """
    401 Unauthorized
    """


class Forbidden(Exception):
    """
    403 Forbidden
    """


class ResourceNotFound(Exception):
    """
    404 Resource Not Found
    """


class InternalServerError(Exception):
    """
    500 Internal Server Error
    """
