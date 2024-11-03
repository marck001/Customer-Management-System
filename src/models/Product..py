from pymongo.errors import DuplicateKeyError
from db.database import Database


class Product:
    collection = Database.get_db()["products"]

    def __init__(self, code, name,category, price, stock):
        self.code = code
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    @staticmethod
    def insert(code, name, category,price, stock):
        return Product.collection.insert_one({
            'code': code,
            'name': name,
            'category':category,
            'price': price,
            'stock': stock
        })

    @classmethod
    def find_by_code(cls, code):
        product_data = cls.collection.find_one({'code': code})
        return cls(product_data['code'], product_data['name'],  product_data['category'],product_data['price'], product_data['stock']) if product_data else None

    @classmethod
    def find_by_name(cls, name):
        product_data = cls.collection.find_one({'name': name})
        return cls(product_data['code'], product_data['name'],  product_data['category'],product_data['price'], product_data['stock']) if product_data else None
    

    def update(self, **kwargs):
        update_data = {key: value for key, value in kwargs.items() if hasattr(self, key)}
        return self.collection.update_one({'code': self.code}, {'$set': update_data})

    def delete(self):
        return self.collection.delete_one({'code': self.code})

    @classmethod
    def list_all(cls):
        products = []
        for product_data in cls.collection.find():
            products.append(cls(product_data['code'], product_data['name'],  product_data['category'],product_data['price'], product_data['stock']))
        return products
    
    def list_by_category(cls,category):
        products = []
        for product_data in cls.collection.find({'category': category}):
            products.append(cls(product_data['code'], product_data['name'],  product_data['category'],product_data['price'], product_data['stock']))
        return products

    def decrease_stock(self, amount):
        if self.stock >= amount:
            self.stock -= amount
            return self.collection.update_one({'code': self.code}, {'$set': {'stock': self.stock}})
        else:
            raise ValueError("Insufficient stock")