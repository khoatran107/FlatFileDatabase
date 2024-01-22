class Product:
    def __init__(self, line=','*5):
        args = line.split(',')
        self.product_id = args[0]
        self.product_code = args[1]
        self.product_name = args[2]
        self.category = args[3]
        self.quantity_per_unit = args[4]
        self.list_price = 0 if not args[5] else float(args[5])


class ProductBuilder:
    def __init__(self):
        self.product_id = ""
        self.product_code = ""
        self.product_name = ""
        self.category = ""
        self.quantity_per_unit = ""
        self.list_price = 0.0

    def set_product_id(self, product_id):
        self.product_id = product_id
        return self

    def set_product_code(self, product_code):
        self.product_code = product_code
        return self

    def set_product_name(self, product_name):
        self.product_name = product_name
        return self

    def set_category(self, category):
        self.category = category
        return self

    def set_quantity_per_unit(self, quantity_per_unit):
        self.quantity_per_unit = quantity_per_unit
        return self

    def set_list_price(self, list_price):
        self.list_price = float(list_price) if list_price else 0.0
        return self

    def build(self):
        return Product(
            f"{self.product_id},{self.product_code},{self.product_name},"
            f"{self.category},{self.quantity_per_unit},{self.list_price}"
        )
