from pymongo.errors import DuplicateKeyError
from db.database import Database

class User:
    Database.initialize()
    collection = Database.get_db()["users"]
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def insert( username, email, password):
        return User.collection.insert_one({
            'username': username,
            'email': email,
            'password': password
        })
    @classmethod
    def find_user(cls,  username, password):
        user_data =  cls.collection.find_one({'username': username,'password':password})
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
