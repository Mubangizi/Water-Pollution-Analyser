import os


class Development():
    """ development config """

    DEBUG = (True,)
    SQLALCHEMY_DATABASE_URI = "postgresql:///water_pollution_db"


class Testing():
    """ test environment config """

    TESTING = (True,)
    DEBUG = (True,)
    # use a separate db

    SQLALCHEMY_DATABASE_URI = "postgresql:///water_pollution_db_testing"


class Production():
    """ production config """

    DEBUG = (False,)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")


app_config = {"development": Development, "testing": Testing, "production": Production}

