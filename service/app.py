from typing import Tuple, TypeVar

from flask import Flask

from service.extensions import db
from service.api.admin_api import Users, Roles
from service.api.authentication_api import authentication_api
from service.errors import ServiceErrors
from service.admin_ui.admin_view import admin_ui

CustomError = TypeVar('CustomError')

app = Flask(__name__)
db.init_app(app)

app.config.from_object('service.config.Config')

roles_api = Roles.as_view('roles')
users_api = Users.as_view('users')

app.add_url_rule(
    '/roles',
    methods=['GET', 'POST'],
    view_func=roles_api
)
app.add_url_rule(
    '/roles/<id_>',
    methods=['GET', 'PUT', 'PATCH', 'DELETE'],
    view_func=roles_api
)
app.add_url_rule(
    '/users',
    methods=['GET', 'POST'],
    view_func=users_api
)
app.add_url_rule(
    '/users/<id_>',
    methods=['GET', 'PUT', 'PATCH', 'DELETE'],
    view_func=users_api
)
app.register_blueprint(authentication_api)

app.register_blueprint(admin_ui)


# @app.errorhandler(Exception)
# def handle_error(exception: 'Exception') -> Tuple[dict, int]:
#     """Handle unexpected errors"""
#     print('<><>Tipo Log<><>', exception)
#     code = getattr(exception, 'code', 500)
#     message = getattr(exception, 'description', 'Something went wrong.')
#     reason = '.'.join([
#         exception.__class__.__module__,
#         exception.__class__.__name__,
#     ])
#     return {
#         'code': code,
#         'message': message,
#         'reason': reason
#     }, code
#
#
# @app.errorhandler(ServiceErrors)
# def handle_error(exception: CustomError) -> Tuple[dict, int]:
#     """Handle errors caused by incorrect requests and responses"""
#     error_output = exception.json()
#     print('<><>Tipo Log<><>', error_output)
#     return error_output, error_output['status']


if __name__ == '__main__':
    app.run()
