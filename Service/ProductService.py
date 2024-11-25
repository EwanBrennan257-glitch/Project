from DAO.ProductDao import ProductDAO

class ProductService:
    def __init__(self):
        self.productDAO = ProductDAO()

    def get_products(self):
        return self.productDAO.getAllProducts()

    def create_product(self, name, description, imageurl, stock, price, created_by, producttype_name,
                       producttype_material, producttype_size):
        producttype=self.productDAO.create_product_type(producttype_name, producttype_material, producttype_size)
        self.productDAO.create_product(name, description, imageurl, stock, price, created_by, producttype)

    def get_product(self, name):
        return self.productDAO.get_product_by_name(name)

    def add_product_to_cart(self, user, productname, cart):
        product = self.get_product(productname)  # Fetch product details

        # Check if the product is already in the cart
        for item in cart["items"]:
            if item["name"] == product.name:
                item["quantity"] += 1  # Increase quantity if already in the cart
                break
        else:
            # Add the product to the cart if not already present
            cart["items"].append(product.to_dict())

        # Update the number of items in the cart
        cart["numberofitems"] = sum(item["quantity"] for item in cart["items"])

        return cart



