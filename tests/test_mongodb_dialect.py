from mongodb_dialect import __version__

from mongodb_dialect import MongoDBDialect

import sqlalchemy

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

def test_version():
    assert __version__ == '0.1.0'


Base = declarative_base()

class Fruit(Base):

    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))

    __tablename__ = 'fruit'

def test_main():
    print("hello:", __version__)
    # エンジンの定義
    engine = sqlalchemy.create_engine('sqlite:///:memory:',  echo=True)
    Base.metadata.create_all(bind=engine)

    session = sessionmaker(bind=engine)()
    apple = Fruit()
    apple.id = 3
    apple.name = 'apple'
    session.add(instance=apple)
    session.commit()


from sqlalchemy.dialects import registry
registry.register("mongodb", "mongodb_dialect", "MongoDBDialect")

def test_dialect():
    engine = sqlalchemy.create_engine("mongodb://localhost:27001/mydb")
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    # test_main()
    try:
        test_dialect()

    except Exception as e:
        print(e)