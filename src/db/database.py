from pymongo import MongoClient

#singleton pattern

class Database:
    _client = None
    _db = None
    
    #inicializar conexion
    @classmethod
    def initialize(cls):
        if cls._client is None:
            cls._client = MongoClient("mongodb://localhost:27017/")  #server connection
            cls._db = cls._client["my_database"]   #database name
            print("Database initialized.")
     #obtener instancia de la conexion
    @classmethod
    def get_db(cls):
        if cls._db is None:
            raise Exception("Call `initialize` first.")
        return cls._db
    #cerrar conexion
    @classmethod
    def close_connection(cls):
        if cls._client:
            cls._client.close()
            cls._client = None  
            cls._db = None 
            
            print("Database connection closed.")
