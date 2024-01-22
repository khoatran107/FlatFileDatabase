from DataFileNames import DataFileNames
from DataReader import OrderReader


class OrderUpdater:
    @staticmethod
    def rewrite(all_orders):
        f = open(DataFileNames.order_file_name, "w")
        for order in all_orders:
            f.write(f"{order.order_id},{order.customer_id},"
                    f"{order.employee_id},{order.order_date},"
                    f"{order.shipped_date},{order.shipping_fee}\n")

    @staticmethod
    def update(order_id, changed_order):
        if changed_order.order_id != order_id:
            raise Exception('The order and id does not match!')
        all_orders = OrderReader.get_instances()
        for i in range(len(all_orders)):
            if all_orders[i].order_id == order_id:
                all_orders[i] = changed_order
        OrderUpdater.rewrite(all_orders)


class ProductUpdater:
    @staticmethod
    def rewrite(all_products):
        f = open(DataFileNames.product_file_name, "w")
        for product in all_products:
            f.write(f"{product.product_id},{product.product_code},"
                    f"{product.product_name},{product.category},"
                    f"{product.quantity_per_unit},{product.list_price}\n")

    @staticmethod
    def add(new_product):
        f = open(DataFileNames.product_file_name, "a")
        f.write(f"{new_product.product_id},{new_product.product_code},"
                f"{new_product.product_name},{new_product.category},"
                f"{new_product.quantity_per_unit},{new_product.list_price}\n")
