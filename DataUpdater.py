from DataFileNames import DataFileNames
from DataReader import OrderReader


class OrderDetailUpdater:
    @staticmethod
    def rewrite(all_order_detail):
        f = open(DataFileNames.order_detail_file_name, "w")
        for order_detail in all_order_detail:
            f.write(f"{order_detail.order_id},{order_detail.product_id},"
                    f"{order_detail.unit_price},{order_detail.quantity}\n")

    @staticmethod
    def add(new_order_detail):
        f = open(DataFileNames.order_detail_file_name, "a")
        f.write(f"{new_order_detail.order_id},{new_order_detail.product_id},"
                f"{new_order_detail.unit_price},{new_order_detail.quantity}\n")


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

    @staticmethod
    def add(new_order):
        f = open(DataFileNames.order_file_name, "a")
        f.write(f"{new_order.order_id},{new_order.customer_id},"
                f"{new_order.employee_id},{new_order.order_date},"
                f"{new_order.shipped_date},{new_order.shipping_fee}\n")


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
