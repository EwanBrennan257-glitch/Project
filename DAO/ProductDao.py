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
    def getAllProducts(self):# Returns the entire list of products stored in the product_list attribute
        return self.product_list

    def get_product_by_name(self, name):
        for product in self.product_list:#loops through product list to get product by name
             if name == product.name:#if product name matches name then return
                 return product

    def create_default_products(self):
        product_types =[#creates product type object with their 3 unique attributes required
        ProductType("Long pants", "Denim", "small"),
        ProductType("Longsleeve", "cotton", "medium"),
        ProductType("T-shirt", "cotton", "large"),
        ProductType("Long pants", "Denim", "Meduim"),
        ProductType("Longsleeve", "leather", "medium"),
        ProductType("T-shirt", "polyester", "large"),
        ProductType("Long pants", "polyester", "small"),
        ProductType("Long Jumper", "cotton", "medium"),
        ]

        #creates instance of the product class for items in the inventory
        P1 = Product(name=f"Worn Jeans", description=f"Worn Jeans that do not include stains", imageurl="/static/Images/product_1.png",
            stock=14, price=40, created_by=User.getadmin(), product_type=product_types[0])

        P2 = Product(name=f"LongSleeve Shirt", description=f"Regular long sleeve shirt with no extra features", imageurl="/static/Images/product_2.png",
            stock=18, price=29, created_by=User.getadmin(), product_type=product_types[1])

        P3 = Product(name=f"T-Shirt", description=f"Vintage T-Shirt worn by Nicholas Cage, on the red carpet, May include stains", imageurl="/static/Images/product_3.png",
            stock=14, price=200, created_by=User.getadmin(), product_type=product_types[2])

        P4 = Product(name=f"Black Vintage Jeans", description=f"Comfortable black jeans, with pockets on back and front does not include belt", imageurl="/static/Images/product_4.png",
            stock=11, price=45, created_by=User.getadmin(), product_type=product_types[3])

        P5 = Product(name=f"Jacket", description=f"Vintage longsleeve jacket with multiple pockets", imageurl="/static/Images/product_5.png",
                     stock=10, price=70, created_by=User.getadmin(), product_type=product_types[4])

        P6 = Product(name=f"Black T-Shirt", description=f"Black T-Shirt that includes no pockets", imageurl="/static/Images/product_6.png",
                     stock=18, price=15, created_by=User.getadmin(), product_type=product_types[5])

        P7 = Product(name=f"Cargo Pants", description=f"Vintage Cargo pants with multiple pockets", imageurl="/static/Images/product_7.png",
                     stock=16, price=35, created_by=User.getadmin(), product_type=product_types[6])

        P8 = Product(name=f"Vintage Jumper", description=f"Comfortable Vintage jumper that has no pockets just comfortable", imageurl="/static/Images/product_8.png",
                     stock=25, price=74, created_by=User.getadmin(), product_type=product_types[7])

        products = [P1, P2, P3, P4, P5, P6, P7, P8]#list to hold all products


        return products