__version__ = '0.1.0'

from .connection import connect
from .exception import *
from . dialect import *

paramstyle = 'pyformat'
threadsafety = 2

__all__ = [
    'MongoDBDialect', 
    'connect', 'apilevel', 'threadsafety', 'paramstyle',
    'Warning', 'Error', 'InterfaceError', 'DatabaseError', 'DataError', 'OperationalError', 'IntegrityError',
    'InternalError', 'ProgrammingError', 'NotSupportedError'
]