from mongodb_dialect import __version__
from mongodb_dialect import MongoDBDialect

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

import traceback

def test_dialect():
    try:
        engine = sqlalchemy.create_engine("mongodb://localhost:27017/testdb")
        Base.metadata.create_all(bind=engine)
        session = sessionmaker(bind=engine)()

        print("get session")
        apple = Fruit()
        apple.id = 3
        apple.name = 'apple'
        session.add(instance=apple)
        session.commit()
        print("commit session")

        apple2 = session.query(Fruit).filter(Fruit.id==3).first()
        apple2.name = 'melon'
        print(apple2)
        session.commit()
        print('update')

    except Exception as e:
        traceback.print_exc()
        print(e)



if __name__ == '__main__':
    # test_main()
    try:
        test_dialect()

    except Exception as e:
        print(e)