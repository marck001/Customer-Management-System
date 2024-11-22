from pymongo.errors import DuplicateKeyError
from db.database import Database
from functions.utils import encode_hash_function
class User:
    Database.initialize()
    collection = Database.get_db()["users"]
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def insert( username, email, password):
        existing_user = User.collection.find_one({'$or': [{'username': username}, {'email': email}]})

        if not existing_user:
            password = encode_hash_function(password)      
            User.collection.insert_one({
                'username': username,
                'email': email,
                'password': password
                        })
            return True
        else:
            return False
       
           
                   
    @classmethod
    def find_user(cls,  username):
        user_data =  cls.collection.find_one({'username': username})
        
        return cls(user_data['username'], user_data['email'], user_data['password']) if user_data else None

  
    def update(self, **kwargs):
        update_data = {key: value for key, value in kwargs.items() if hasattr(self, key)}
        return self.collection.update_one({'username': self.username}, {'$set': update_data})

    def delete(self):
        return self.collection.delete_one({'username': self.username})
    @classmethod
    def list_all(cls):
        users = []
        for user_data in cls.collection.find():
            users.append(cls(user_data['username'], user_data['email'], user_data['password']))
        return users