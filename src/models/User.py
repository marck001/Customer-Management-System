from pymongo.errors import DuplicateKeyError

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def insert(collection, username, email, password):
        return collection.insert_one({
            'username': username,
            'email': email,
            'password': password
        })

    def find_by_username(cls, collection, username):
        user_data = collection.find_one({'username': username})
        return cls(user_data['username'], user_data['email'], user_data['password']) if user_data else None

    def update(self, collection, **kwargs):
        update_data = {key: value for key, value in kwargs.items() if hasattr(self, key)}
        return collection.update_one({'username': self.username}, {'$set': update_data})

    def delete(self, collection):
        return collection.delete_one({'username': self.username})

    @classmethod
    def list_all(cls, collection):
        return [cls(user_data['username'], user_data['email'], user_data['password']) for user_data in collection.find()]
#comment a