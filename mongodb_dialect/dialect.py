from __future__ import absolute_import

from sqlalchemy.engine import default
from sqlalchemy.sql.compiler import *


class MongoIdentifierPreparer(IdentifierPreparer):
    def __init__(self, dialect, initial_quote='', final_quote=None, escape_quote='', omit_schema=False):
        super(MongoIdentifierPreparer, self).__init__(dialect, initial_quote, final_quote, escape_quote, omit_schema)


import traceback
import sys
import re

class MongoDBDialect(default.DefaultDialect):
    name = 'mongodb_dialect'

    preparer = MongoIdentifierPreparer
    supports_sequences = True
    sequences_optional = True
    supports_native_decimal = True
    supports_default_values = True
    supports_native_boolean = True
    supports_statement_cache = True

    default_paramstyle = 'pyformat'

    def __init__(self, **kwargs):
        super(MongoDBDialect, self).__init__(self, **kwargs)
        self.driver = 'mongodb_connector'

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
        args = {}
        try:
            uri = str(url)
            match = re.match(r'^mongodb://((?P<user>.*):(?P<password>.*)@)?(?P<host>.*?)(:(?P<port>[1-9][0-9]*))?/(?P<database>.*)$', uri)
            d = match.groupdict()
            args = {
                'username': d.get('username', None),
                'password': d.get('password', None),
                'host': d.get('host', 'localhost'),
                'port': d.get('port', 27017),
                'database': d.get('database', 'testdb')
            }
        except Exception as e:
            print("failed parse url")
            print(e)
            opts = {}
        print("parsed arg",args)
        return url, args

    def get_table_names(self, connection, schema=None, **kw):
        ret = connection.connection.list_tables()
        print("dialect#get_table_names", ret)
        return ret

    def has_table(self, connection, table_name, schema=None):
        print("dialect#has_table")
        return table_name in self.get_table_names(connection, schema)

    def has_sequence(self, connection, sequence_name, schema=None):
        print("dialect#has_sequence")
        return False

    def get_columns(self, connection, table_name, schema=None, **kw):
        print("dialect#get_columns")
        cols = connection.connect().connection.connection.list_columns(table_name)
        return cols

    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        print("dialect#get_foreign_keys")
        return []

    def get_indexes(self, connection, table_name, schema=None, **kw):
        print("dialect#get_indexes")
        return []

    def get_view_names(self, connection, schema=None, **kw):
        print("dialect#get_view_names")
        return []

    def get_pk_constraint(self, conn, table_name, schema=None, **kw):
        print("dialect#get_pk_constraint")
        return {}

    def get_unique_constraints(self, connection, table_name, schema=None, **kw):
        print("dialect#get_unique_constraint")
        return []

