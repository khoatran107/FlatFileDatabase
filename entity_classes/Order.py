class Order:
    def __init__(self, line=','*5):
        args = line.split(',')
        self.order_id = args[0]
        self.customer_id = args[1]
        self.employee_id = args[2]
        self.order_date = args[3]
        self.shipped_date = args[4]
        self.shipping_fee = float(args[5])
