from Model.Product import Product, ProductType
from Model.User import User
#to hold all users in global list
GLOBAL_PRODUCT_LIST=list()


# class to hold all users in memory, using this instead of database
class ProductDAO:

    is_defaultproductscreated=False
    def __init__(self, product_list=None):
        # Initialize user_list as an empty list if None is provided
        self.product_list = GLOBAL_PRODUCT_LIST
        if product_list:
            self.product_list.extend(product_list)
        if not self.is_defaultproductscreated:
            self.product_list=self.create_default_products()
            self.is_defaultproductscreated=True

    # This method grabs all users, and creates some if the list is empty
    def getAllProducts(self):
        return self.product_list

    def create_product(self, name, description, imageurl, stock, price, created_by, product_type):
        product = Product(name=name, description=description, imageurl= imageurl,
                          stock=stock, price=price, created_by= created_by, product_type=product_type)
        self.product_list.append(product)

    def create_product_type(self, name, material, size):
        return ProductType(name=name, material=material, size=size)

    def get_product_by_name(self, name):
        for product in self.product_list:
             if name == product.name:
                 return product

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
        P1 = Product(name=f"product_{1}", description=f"description {1}", imageurl="/static/Images/product_1.png",
            stock=10, price=20, created_by=User.getadmin(), product_type=product_types[0])

        P2 = Product(name=f"product_{2}", description=f"description {2}", imageurl="/static/Images/product_2.png",
            stock=10, price=20, created_by=User.getadmin(), product_type=product_types[1])

        P3 = Product(name=f"product_{3}", description=f"description {3}", imageurl="/static/Images/product_1.png",
            stock=10, price=20, created_by=User.getadmin(), product_type=product_types[2])

        P4 = Product(name=f"product_{4}", description=f"description {4}", imageurl="/static/Images/product_2.png",
            stock=10, price=20, created_by=User.getadmin(), product_type=product_types[3])

        P5 = Product(name=f"product_{5}", description=f"description {5}", imageurl="/static/Images/product_1.png",
                     stock=10, price=20, created_by=User.getadmin(), product_type=product_types[4])

        P6 = Product(name=f"product_{6}", description=f"description {6}", imageurl="/static/Images/product_2.png",
                     stock=10, price=20, created_by=User.getadmin(), product_type=product_types[5])

        P7 = Product(name=f"product_{7}", description=f"description {7}", imageurl="/static/Images/product_1.png",
                     stock=10, price=20, created_by=User.getadmin(), product_type=product_types[6])

        P8 = Product(name=f"product_{8}", description=f"description {8}", imageurl="/static/Images/product_2.png",
                     stock=10, price=20, created_by=User.getadmin(), product_type=product_types[7])

        products = [P1, P2, P3, P4, P5, P6, P7, P8]


        return products