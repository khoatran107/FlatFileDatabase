class OrderDetail:
    def __init__(self, line=','*3):
        args = line.split(',')
        self.order_id = args[0]
        self.product_id = args[1]
        self.unit_price = 0 if not args[3] else float(args[2])
        self.quantity = 0 if not args[3] else int(args[3])


class OrderDetailBuilder:
    def __init__(self):
        self.order_id = ""
        self.product_id = ""
        self.unit_price = 0.0
        self.quantity = 0

    def set_order_id(self, order_id):
        self.order_id = order_id
        return self

    def set_product_id(self, product_id):
        self.product_id = product_id
        return self

    def set_unit_price(self, unit_price):
        self.unit_price = float(unit_price) if unit_price else 0.0
        return self

    def set_quantity(self, quantity):
        self.quantity = int(quantity) if quantity else 0
        return self

    def build(self):
        return OrderDetail(
            f"{self.order_id},{self.product_id},{self.unit_price},{self.quantity}"
        )
