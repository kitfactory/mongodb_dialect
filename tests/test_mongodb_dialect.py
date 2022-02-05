from mongodb_dialect import __version__

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


if __name__ == '__main__':
    test_main()
