from __future__ import absolute_import

from sqlalchemy.engine import default
from sqlalchemy.sql.compiler import *


class MongoIdentifierPreparer(IdentifierPreparer):
    def __init__(self, dialect, initial_quote='', final_quote=None, escape_quote='', omit_schema=False):
        super(MongoIdentifierPreparer, self).__init__(dialect, initial_quote, final_quote, escape_quote, omit_schema)


import traceback
import sys

class MongoDBDialect(default.DefaultDialect):
    name = 'mongodb'

    preparer = MongoIdentifierPreparer
    supports_sequences = True
    sequences_optional = True
    supports_native_decimal = True
    supports_default_values = True
    supports_native_boolean = True

    default_paramstyle = 'pyformat'

    def __init__(self, **kwargs):
        super(MongoDBDialect, self).__init__(self, **kwargs)

    def initialize(self, connection):
        pass

    @classmethod
    def dbapi(cls):
        print("dbapi")
        f = sys._getframe(1)
        traceback.print_stack(f, limit=None, file=sys.stdout)
        return __import__('mongodb_connector')

    def create_connect_args(self, url):
        print("create_connect_args", url)
        # try:
        #     opts = url.translate_connect_args()
        #     args = {
        #         'username': opts['username'],
        #         'password': opts.get('password', ""),
        #         'host': opts.get('host', 'localhost'),
        #         'port': opts.get('port', 0),
        #         'database': opts['database']
        #     }
        #     args.update(url.query)
        # except Exception as e:
        #     print("failed parse url")
        #     print(e)
        #     opts = {}
        args = {
            'username': '',
            'password': '',
            'host': 'localhost',
            'port': 27017,
            'database': 'test'
        }
        print("parsed arg",args)
        return url, args

    def get_table_names(self, connection, schema=None, **kw):
        return connection.connect().connection.connection.list_tables()

    def has_table(self, connection, table_name, schema=None):
        return table_name in self.get_table_names(connection, schema)

    def has_sequence(self, connection, sequence_name, schema=None):
        return False

    def get_columns(self, connection, table_name, schema=None, **kw):
        cols = connection.connect().connection.connection.list_columns(table_name)
        return cols

    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        return []

    def get_indexes(self, connection, table_name, schema=None, **kw):
        return []

    def get_view_names(self, connection, schema=None, **kw):
        return []

    def get_pk_constraint(self, conn, table_name, schema=None, **kw):
        return {}

    def get_unique_constraints(self, connection, table_name, schema=None, **kw):
        return []

