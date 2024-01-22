class OrderDetail:
    def __init__(self, line=','*3):
        args = line.split(',')
        self.order_id = args[0]
        self.product_id = args[1]
        self.unit_price = float(args[2])
        self.quantity = int(args[3])
