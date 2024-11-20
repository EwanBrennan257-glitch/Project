from Model.Product import Product, ProductType
from Model.User import User
#to hold all users in global list
GLOBAL_PRODUCT_LIST=list()


# class to hold all users in memory, using this instead of database
class ProductDAO:

    def __init__(self, product_list=None):
        # Initialize user_list as an empty list if None is provided
        self.product_list = GLOBAL_PRODUCT_LIST
        if product_list:
            self.product_list.extend(product_list)

    # This method grabs all users, and creates some if the list is empty
    def getAllProducts(self):
        self.create_default_products()
        return self.product_list

    def create_default_products(self):
        product_types =[
        ProductType("T-shirt", "cotton", "small"),
        ProductType("T-shirt", "cotton", "medium"),
        ProductType("T-shirt", "cotton", "large"),
        ProductType("T-shirt", "polyester", "small"),
        ProductType("T-shirt", "polyester", "medium"),
        ProductType("T-shirt", "polyester", "large"),
        ProductType("Jeans", "denim", "small"),
        ProductType("Jeans", "denim", "medium"),
        ProductType("Jeans", "denim", "large"),
        ProductType("Jacket", "polyester", "small"),
        ProductType("Jacket", "polyester", "medium"),
        ProductType("Jacket", "polyester", "large"),
        ]

        #
        P1=Product(name=f"product_{1}", description=f"description {1}", imageurl="/static/Images/product_1.png",
            stock=10, price=20, created_by=User.getadmin(), product_type=product_types[0])

        P2=Product(name=f"product_{2}", description=f"description {2}", imageurl="/static/Images/product_2.png",
            stock=10, price=20, created_by=User.getadmin(), product_type=product_types[1])

        self.product_list.append(P1)
        self.product_list.append(P2)

        return self.product_list