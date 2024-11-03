from pymongo import MongoClient

class Database:
    _client = None
    _db = None

    @classmethod
    def initialize(cls):
        if cls._client is None:
            cls._client = MongoClient("mongodb://localhost:27017/")
            cls._db = cls._client["my_database"]
            print("Database initialized.")

    @classmethod
    def get_db(cls):
        if cls._db is None:
            raise Exception("Call `initialize` first.")
        return cls._db

    @classmethod
    def close_connection(cls):
        if cls._client:
            cls._client.close()
            cls._client = None  
            cls._db = None 
            print("Database connection closed.")
