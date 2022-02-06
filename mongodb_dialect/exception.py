from __future__ import absolute_import


class MongoDBException(Exception):
    def __init__(self, msg):
        super(MongoDBException, self).__init__(msg)
        self.msg = msg