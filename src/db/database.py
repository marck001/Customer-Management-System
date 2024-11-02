from pymongo import MongoClient

class Database:
    _client = None
    _db = None

    def initialize(cls, uri="mongodb://localhost:27017/", db_name="my_database"):
        if cls._client is None:
            cls._client = MongoClient(uri)
            cls._db = cls._client[db_name]
            print("Database initialized.")

    def get_db(cls):
        if cls._db is None:
            raise Exception("Call `initialize` first.")
        return cls._db

    def close_connection(cls):
        if cls._client:
            cls._client.close()
            print("Database connection closed.")
