from http import HTTPStatus
from typing import Dict


class ServiceErrors(Exception):
    """
    Custom error handling class to catch and handle errors
    caused by incorrect request or response from third party.
    """

    code = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(
            self,
            status_code=code,
            type_=code.phrase,
            message=code.description
    ) -> None:
        super().__init__()
        self.status_code = status_code
        self.message = message
        self.type_ = type_

    def json(self) -> Dict[str, str]:
        return {
            'status': self.status_code,
            'type': self.type_,
            'message': self.message
        }


class ServiceBadRequest(ServiceErrors):
    """Exceptions to raise for incorrect input data"""

    code = HTTPStatus.BAD_REQUEST

    def __init__(
            self,
            status_code=code,
            type_=code.phrase,
            message=code.description
    ) -> None:
        super(ServiceBadRequest, self).__init__(
            status_code=status_code,
            type_=type_,
            message=message
        )


class DBError(ServiceErrors):
    """Exceptions to handle errors from ORM,
    caused incorrect input data, or unexpected DB errors."""

    def __init__(
            self,
            message='DB connection error'
    ) -> None:
        super(DBError, self).__init__(
            message=message
        )
