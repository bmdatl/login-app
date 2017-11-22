from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db', echo=True)
base = declarative_base()


class User(base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)

    def __init__(self, name, username, password):
        """"""
        self.name = name
        self.username = username
        self.password = password


base.metadata.create_all(engine)
