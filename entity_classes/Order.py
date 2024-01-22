class Order:
    def __init__(self, line=','*5):
        args = line.split(',')
        self.order_id = args[0]
        self.customer_id = args[1]
        self.employee_id = args[2]
        self.order_date = args[3]
        self.shipped_date = args[4]
        self.shipping_fee = 0 if not args[5] else float(args[5])


class OrderBuilder:
    def __init__(self):
        self.order_id = ""
        self.customer_id = ""
        self.employee_id = ""
        self.order_date = ""
        self.shipped_date = ""
        self.shipping_fee = 0.0

    def set_order_id(self, order_id):
        self.order_id = order_id
        return self

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
        return self

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id
        return self

    def set_order_date(self, order_date):
        self.order_date = order_date
        return self

    def set_shipped_date(self, shipped_date):
        self.shipped_date = shipped_date
        return self

    def set_shipping_fee(self, shipping_fee):
        self.shipping_fee = float(shipping_fee) if shipping_fee else 0.0
        return self

    def build(self):
        return Order(
            f"{self.order_id},{self.customer_id},{self.employee_id},"
            f"{self.order_date},{self.shipped_date},{self.shipping_fee}"
            )
