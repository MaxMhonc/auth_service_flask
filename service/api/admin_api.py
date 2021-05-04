from typing import Optional, Tuple

from flask import request
from flask.views import MethodView

from service.models.models import Role, User
from service.utils.query import Query


class AdminAPI(MethodView):
    """Implement CRUD operation with DB records
    according to Model instances."""

    def get(self, id_: Optional[str] = None) -> Tuple[dict, int]:
        """Return record by id if id not None, else - all records"""
        return self._get_records(id_) if id_ else self._get_record()

    def post(self) -> Tuple[dict, int]:
        """Create new record"""
        #  ToDo: fields validation
        fields = request.get_json()
        inst = self.query.post_record(fields)
        return {'message': f'{inst} created successfully'}, 201

    def put(self, id_: str) -> Tuple[dict, int]:
        """Replace record by id by new record"""
        #  ToDo: fields validation
        fields = request.get_json()
        return self._update_record(id_, fields)

    def patch(self, id_: str) -> Tuple[dict, int]:
        """Update record by id"""
        #  ToDo: fields validation
        fields = request.get_json()
        return self._update_record(id_, fields)

    def delete(self, id_: str) -> Tuple[dict, int]:
        """Delete role bt id"""
        self.query.delete_record(id_)
        return {
                   'message': f'{self.query.model.title()} {id_} '
                              f'deleted successfully'
               }, 200

    def _update_record(self, id_: str, fields: dict) -> Tuple[dict, int]:
        """Update record by id"""
        self.query.patch_record(id_, fields)
        return {
                   'message': f'{self.query.model.title()} {id_} '
                              f'updated successfully'
               }, 200

    def _get_records(self, id_: str) -> Tuple[dict, int]:
        """Return one record by id."""
        return self.query.get_record_by_id(id_).to_json(), 200

    def _get_record(self) -> Tuple[dict, int]:
        """Return all records."""
        records = self.query.get_records()
        records = {
            'count': len(records),
            f'{self.query.model.title(plural=True)}': [
                record.to_json() for record in records
            ]
        }
        return records, 200


class Roles(AdminAPI):
    query = Query(Role)


class Users(AdminAPI):
    query = Query(User)
