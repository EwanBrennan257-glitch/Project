from Model.User import User
class ProductType:# Class to define the type/category of a product

    def __init__(self, name:str, material:str, size:str,):
        self.name = name
        self.material = material
        self.size = size

    def __repr__(self):
        return f"ProductType(name='{self.name})"
class Product:# Class to define a product with all its details
    def __init__(self, name:str, description:str, stock:int, price:float, imageurl:str, created_by:User, product_type:ProductType):
        self.name = name
        self.description = description
        self.stock = stock
        self.price = price
        self.imageurl = imageurl
        self.created_by = created_by
        self.product_type =product_type

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




