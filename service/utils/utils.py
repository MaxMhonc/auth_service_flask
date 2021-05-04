import re
from typing import TypeVar, Callable

from sqlalchemy.exc import DataError, OperationalError

from service.errors import ServiceBadRequest, DBError

ClassAttribute = TypeVar('ClassAttribute')


def is_protected(method: ClassAttribute) -> bool:
    """Check if attribute is declared as protected."""
    substr = '[_][^_]'
    return bool(re.match(substr, str(method)))


def decorate_protected_methods(decorator: Callable) -> Callable:
    """Decorate attributes of class
    which are callable and declared as protected by 'decorator'"""
    def class_wrapper(cls):
        for attr in cls.__dict__:

            if is_protected(attr) and callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))

        return cls

    return class_wrapper


def db_errors_handler(func: Callable) -> Callable:
    """Catch SQLAlchemy errors"""
    def wrapper(*args, **kwargs):

        try:

            return func(*args, **kwargs)

        except DataError:
            raise ServiceBadRequest

        except OperationalError:
            raise DBError

    return wrapper
