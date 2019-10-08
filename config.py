import os


class Development(Base):
    """ development config """

    DEBUG = (True,)
    SQLALCHEMY_DATABASE_URI = "postgresql:///water_pollution_db"


class Testing(Base):
    """ test environment config """

    TESTING = (True,)
    DEBUG = (True,)
    # use a separate db

    SQLALCHEMY_DATABASE_URI = "postgresql:///water_pollution_db_testing"


class Production(Base):
    """ production config """

    DEBUG = (False,)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")


app_config = {"development": Development, "testing": Testing, "production": Production}

