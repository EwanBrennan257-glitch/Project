from DAO.ProductDao import ProductDAO# import product DAO so it can interact with the product data
from db import create_product, create_producttype, select_product_by_name
class ProductService:
    def __init__(self):#intialises productservice and creates an instance of productdao
        self.productDAO = ProductDAO()

    def get_products(self):# takes products from the DAO
        return self.productDAO.getAllProducts()


    def get_product(self, name):#takes a single product taken by its name
        return select_product_by_name(name)

    def add_product_to_cart(self, user, productname, cart):#adds a product to the users shopping cart
        product = self.get_product(productname)  # Fetch product details
        # Check if the product is already in the cart
        for item in cart["items"]:
            if item["name"] == product["name"]:
                if item["stock"]==1:
                    return cart
                item["quantity"] += 1  # Increase quantity if already in the cart
                break
        else:
            new_item = product
            new_item["quantity"] = 1
            # Add the product to the cart if not already present
            cart["items"].append(new_item)

        # Update the number of items in the cart
        cart["numberofitems"] = sum(item["quantity"] for item in cart["items"])

        return cart

    def create_product(self,name, description, stock, price, imageurl, created_by,
                    created_at, producttypename, producttypematerial, producttypesize):
        #calling database function to create a new product
        product_type = create_producttype(producttypename, producttypematerial, producttypesize)
        create_product(name, description, stock, price, imageurl, created_by,
                   product_type, created_at)



