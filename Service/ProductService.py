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
