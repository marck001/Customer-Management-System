from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox

class Database:
    _client = None
    _db = None
    _users_collection = None

    @classmethod
    def initialize(cls):
        if cls._client is None:
            cls._client = MongoClient("mongodb://localhost:27017/")
            cls._db = cls._client["my_database"]
            cls._users_collection = cls._db["users"]
            print("Database initialized.")

    @classmethod
    def get_db(cls):
        if cls._db is None:
            raise Exception("Call `initialize` first.")
        return cls._db
    
    @classmethod
    def find_user_by_username(cls, username):
        if cls._users_collection is None:
            raise Exception("La base de datos no ha sido inicializada.")
   
        user_data = cls._users_collection.find_one({"username": username})
        return cls(user_data['username'],user_data['email'],user_data['password']if user_data else None)


    @classmethod
    def close_connection(cls):
        if cls._client:
            cls._client.close()
            cls._client = None  
            cls._db = None 
            cls._users_collection = None
            print("Database connection closed.")
