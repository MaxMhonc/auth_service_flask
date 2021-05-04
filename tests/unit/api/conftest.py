from pytest import fixture

from service.app import app
from service.extensions import db


# @fixture(scope='session')
# def client():
#     # app.testing = True
#     with app.test_client() as client:
#         yield client


def fill_in_test_db():
    with open('tests/unit/api/mock_data/test_db_data.sql', 'r') as file:
        sql_query = file.read()
    connection = db.engine.connect()
    connection.execute(sql_query)
    connection.close()


def set_up_test_db():
    with app.app_context():
        db.create_all()
        fill_in_test_db()


def tear_down_test_db():
    with app.app_context():
        db.drop_all()


@fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        'postgresql://postgres:postgres@localhost:5432/roles_users_db_test'
    )

    set_up_test_db()

    yield app.test_client()

    tear_down_test_db()
