from uuid import uuid4
from typing import Dict, Union

from sqlalchemy.dialects.postgresql import UUID

from service.utils.query import Query
from service.extensions import db


class UserRole(db.Model):
    """Model to implement many-to-many relations between role and user"""
    __tablename__ = 'user_role'

    user_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey('users.id'), primary_key=True
    )
    role_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey('roles.id'), primary_key=True
    )


class User(db.Model):
    """
    User model, contains user personal data and relations to roles
        schema:
        {
            "id": "str"            # creates automatically
            "email": "str",
            "psw": "str",
            "urole": ["role_id"]   # not necessary to post
        }
    """
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    email = db.Column(db.String(120), unique=True, nullable=False)
    psw = db.Column(db.String(120), nullable=False)
    role = db.relationship('Role', secondary='user_role')

    def to_json(self, role_ids: bool = True) -> dict:
        """Convert model instance to JSON"""
        # ToDo: implement role_ids
        roles_list = [str(role.id) for role in self.role] if role_ids else []
        roles = {
            "count": len(self.role),
            "ids": roles_list
        }
        return {
            "id": str(self.id),
            "email": self.email,
            "psw": self.psw,
            "roles_dis": roles
        }

    @classmethod
    def from_json(cls, fields: Dict[str, Union[str, list, None]]) -> 'User':
        """Convert JSON form instance to Model instance"""
        user = cls()
        user.email = fields['email'],
        user.psw = fields['psw']

        roles = fields.get('role')
        if roles:
            for role in roles:
                role_to_add = Query(Role).get_record_by_id(role)
                user.role.append(role_to_add)

        return user

    def update(self, fields: Dict[str, Union[str, list, None]]) -> None:
        """Update Model instance fields from data in JSON form"""
        for key, value in fields.items():
            if key == 'role':
                for role_id in value:
                    role_to_add = Query(Role).get_record_by_id(role_id)
                    self.role.append(role_to_add)
            else:
                setattr(self, key, value)

    def __repr__(self) -> str:
        return f'User: {self.email}'

    @staticmethod
    def title(plural: bool = False) -> str:
        return 'users' if plural else 'user'


class Role(db.Model):
    """
    Role model, include role identifying and describing  data.
        schema:
        {
            "id": "str"              # creates automatically
            "name": "str",
            "description": "str",
            "user": ["user_id"]      # not necessary to post
        }
    """
    __tablename__ = 'roles'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name = db.Column(db.String(25), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    user = db.relationship('User', secondary='user_role')

    def to_json(self, user_ids: bool = True) -> dict:
        """Convert model instance to JSON"""
        # ToDo: implement user_ids
        uer_list = [str(user.id) for user in self.user] if user_ids else []
        users = {
            "count": len(self.user),
            "ids": uer_list
        }
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "user_ids": users
        }

    @classmethod
    def from_json(cls, fields: Dict[str, Union[str, list, None]]) -> 'Role':
        """Convert JSON form instance to Model instance"""
        role = cls()
        role.name = fields['name'],
        role.description = fields['description']

        users = fields.get('user_ids')
        if users:
            for user in users:
                user_to_add = Query(User).get_record_by_id(user)
                role.user.append(user_to_add)

        return role

    def update(self, fields: Dict[str, Union[str, list, None]]) -> None:
        """Update Model instance fields from data in JSON form"""
        for key, value in fields.items():
            if key == 'user':
                for user_id in value:
                    user_to_add = Query(User).get_record_by_id(user_id)
                    self.user.append(user_to_add)
            else:
                setattr(self, key, value)

    def __repr__(self) -> str:
        return f'Role: {self.name}'

    @staticmethod
    def title(plural: bool = False) -> str:
        return 'roles' if plural else 'role'
