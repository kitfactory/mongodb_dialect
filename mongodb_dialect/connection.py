import os

# import pandas as pd
from sqlalchemy import types
# from ps_parser import PandasSqlParser

from .cursor import MongoDBDialectCursor
from .log import logger


class MongoDBDialectConnection(object):
    # TODO Here should be modified
    FILE_DIR = '/vagrant'

    def __init__(self, username=None, password=None, host=None, database=None, **kwargs):
        print("MonogoDBDialectConnection#__init__")
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        # self.xl = pd.ExcelFile(os.path.join(self.FILE_DIR, database) + '.xlsx')
        self.limit = kwargs['limit'] if 'limit' in kwargs else 100000

    def close(self):
        logger.debug('Connection closed.')
        self.xl.close()

    def commit(self):
        logger.debug('Commit.')
        # self.xl.close()

    def rollback(self):
        logger.debug('Rollback.')

    def list_tables(self):
        return self.xl.sheet_names

    def list_columns(self, table_name):
        tb = self.xl.parse(table_name)
        return [{'name': str(c), 'type': types.String, 'nullable': False, 'default': None} for c in tb.columns]

    def table_path(self, table_name):
        return os.path.join(self.FILE_DIR, self.database, ':', table_name)

    def load_table(self, table_name):
        return self.xl.parse(table_name)

    def load_all_table(self, table_names):
        context = {}
        for tb_name in table_names:
            context[tb_name] = self.load_table(tb_name)
        return context

    def query(self, sql):
        print("query")
        # psp = PandasSqlParser(sql)
        table_names = []
        for db_name, tb_name in psp.source_tables(True):
            table_names.append(tb_name)
        context = self.load_all_table(table_names)
        # result_df = psp.execute(context)
        # return result_df, context

    def cursor(self):
        print("request cursor")
        return MongoDBDialectCursor(self)


def connect(username=None, password=None, host=None, database=None, **kwargs):
    print("connect")
    return MongoDBDialectConnection(username, password, host, database, **kwargs)