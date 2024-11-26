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

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'stock': self.stock,
            'price': self.price,
            'imageurl': self.imageurl,
            'created_by': self.created_by.email, #to do use actual user serialised user object
            'product_type': self.product_type.name, #to do ...
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
            #to do .... complete
        )


    def __repr__(self):
        return f"Product(name='{self.name})"




