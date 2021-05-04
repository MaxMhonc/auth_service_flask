from typing import TypeVar, Dict, Union, NoReturn, List

from service.extensions import db
from service.errors import ServiceBadRequest
from service.utils.utils import decorate_protected_methods, db_errors_handler

DBInstance = TypeVar('DBInstance')
DBModel = TypeVar('DBModel')
DBModelInstance = TypeVar('DBModelInstance')


@decorate_protected_methods(db_errors_handler)
class Query:
    """Class for interaction with ORM.
    All communication actions are in private methods."""

    def __init__(self, model: DBModel, db: DBInstance = db) -> None:
        self.model = model
        self.db = db

    def get_records(self) -> List[DBModelInstance]:
        """Get all instance records"""
        return self._get_all_records()

    def post_record(self, fields: Dict[str, Union[str, list, None]]) -> str:
        """Write new instance record"""
        instance = self.model.from_json(fields)
        self._write_to_db(instance)
        return str(instance)

    def get_record_by_id(self, id_: str) -> Union[DBModelInstance, NoReturn]:
        """Get one record by id"""
        return self._get(id_)

    def patch_record(
            self, id_: str, fields: Dict[str, Union[str, list, None]]
    ) -> None:
        """Update record fields by id"""
        instance = self._get(id_)
        instance.update(fields)
        self.db.session.commit()

    def delete_record(self, id_: str) -> None:
        """Delete record by id"""
        instance = self._get(id_)
        self._delete_from_db(instance)

    def _get_all_records(self) -> List[DBModelInstance]:
        """Get all instance records"""
        return self.model.query.all()

    def _write_to_db(self, instance: DBModelInstance) -> None:
        """Write record to DB"""
        self.db.session.add(instance)
        self.db.session.commit()

    def _delete_from_db(self, instance: DBModelInstance) -> None:
        """Delete record from DB"""
        self.db.session.delete(instance)
        self.db.session.commit()

    def _get(self, id_: str) -> Union[DBModelInstance, NoReturn]:
        """Get record from DB by id"""
        record = self.model.query.get(id_)
        if record:
            return record
        else:
            #  raise error to correct handling wrong inputted params
            raise ServiceBadRequest()
