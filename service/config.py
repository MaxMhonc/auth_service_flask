class Config:

    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:postgres@localhost:5432/roles_users_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # to log SQL queries
    # SQLALCHEMY_ECHO = True
