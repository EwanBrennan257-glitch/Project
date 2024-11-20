from Model.User import User
class ProductType:

    def __init__(self, name:str, material:str, size:str,):
        self.name = name
        self.material = material
        self.size = size

    def __repr__(self):
        return f"ProductType(name='{self.name})"
class Product:
    def __init__(self, name:str, description:str, stock:int, price:float, imageurl:str, created_by:User, product_type:ProductType):
        self.name = name
        self.description = description
        self.stock = stock
        self.price = price
        self.imageurl = imageurl
        self.created_by = created_by
        self.product_type =product_type

    def __repr__(self):
        return f"Product(name='{self.name})"




