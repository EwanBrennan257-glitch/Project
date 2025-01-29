from Model.User import User
import datetime
class ProductType:# Class to define the type/category of a product

    def __init__(self, name:str, material:str, size:str,):
        self.name = name
        self.material = material
        self.size = size

    def __repr__(self):
        return f"ProductType(name='{self.name})"
class ProductTypeRead(ProductType):
    def __init__(self, id:int, name:str, material:str, size:str):
        super().__init__(name, material, size)
        self.id = id

    def to_dict(self) -> dict:
        return {
            "id":self.id, "name":self.name, "material":self.material, "size":self.size
        }
class Product:# Class to define a product with all its details
    def __init__(self, name:str, description:str, stock:int, price:float, imageurl:str, created_by:User, product_type:ProductType, created_at:datetime):
        self.name = name
        self.description = description
        self.stock = stock
        self.price = price
        self.imageurl = imageurl
        self.created_by = created_by
        self.product_type =product_type
        self.created_at = created_at

    def to_dict(self): # Convert product details to a dictionary
        return {
            'name': self.name,
            'description': self.description,
            'stock': self.stock,
            'price': self.price,
            'imageurl': self.imageurl,
            'created_by': self.created_by.email,#tried to make it so we could create products in this version but could not
            #get it to work some code still in the project
        }

    # Create a Product object from a dictionary
    @staticmethod
    def from_dict(data):
        return Product(
            name=data['name'],
            description=data['description'],
            stock=data['stock'],
            price=data['price'],
            imageurl=data['imageurl'],
            created_by=data['created_by'],
            product_type=data['product_type']
        )


    def __repr__(self):#string for the project object
        return f"Product(name='{self.name})"

class ProductRead(Product):
    def __init__(self, id, name, description, stock, price, imageurl, created_by, product_type, created_at):
        super().__init__(name, description, stock, price, imageurl, created_by, product_type, created_at)
        self.id=id


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'stock': self.stock,
            'price': self.price,
            'imageurl': self.imageurl,
            'created_by': self.created_by,
            'product_type': self.product_type,
            'created_at': self.created_at
        }




