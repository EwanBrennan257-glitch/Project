from DAO.ProductDao import ProductDAO

class ProductService:
    def __init__(self):
        self.productDAO = ProductDAO()

    def get_products(self):
        return self.productDAO.getAllProducts()
