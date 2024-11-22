from pymongo.errors import DuplicateKeyError
from db.database import Database


class Selling:
    @staticmethod
    def get_collection():
        return Database.get_db()["sellings"]
    
    def __init__(self, user_name, product_name, code,category, price, date=None):
        self.user_name = user_name
        self.product_name = product_name
        self.code = code
        self.category = category
        self.price = price
        self.date = date
    #gaby
    @staticmethod
    def insert(user_name, product_name, code, category, price, date):
        collection = Selling.get_collection()
        try:
          
            date = date.strftime("%Y-%m-%d")
            return collection.insert_one({
                'user_name': user_name,
                'product_name': product_name,
                'code':code,
                'category': category,
                'price': price,
                'date': date
            })
        except DuplicateKeyError:
            print("Error: Duplicate entry.")
            return None

    @classmethod
    def find_by_code(cls, code):
        collection = cls.get_collection()
        selling_data = collection.find_one({'code':code})
        return cls(selling_data['user_name'],selling_data['product_name'],selling_data['code'],selling_data['category'],selling_data['price'],selling_data['date']) if selling_data else None

    @classmethod
    def list_all(cls, user):
        collection = cls.get_collection()
        sellings = []
        for selling_data in collection.find({'user_name': user}):
            sellings.append(cls(selling_data['user_name'],selling_data['product_name'],selling_data['code'],selling_data['category'],selling_data['price'],selling_data['date']))
        return sellings

    @classmethod
    def list_by_user(cls, user,date):
        collection = cls.get_collection()
        sellings = []
        for selling_data in collection.find({'user_name': user,'date':date}):
            sellings.append(cls(selling_data['user_name'],selling_data['product_name'],selling_data['code'],selling_data['category'],selling_data['price'],selling_data['date']))
        return sellings
    
