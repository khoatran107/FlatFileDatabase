class Product:
    def __init__(self, line=','*5):
        args = line.split(',')
        self.product_id = args[0]
        self.product_code = args[1]
        self.product_name = args[2]
        self.category = args[3]
        self.quantity_per_unit = args[4]
        self.list_price = float(args[5])
