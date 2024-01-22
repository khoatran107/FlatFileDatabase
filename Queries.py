from prettytable import PrettyTable
from DataReader import OrderReader, OrderDetailReader, ProductReader


class Matcher:
    @staticmethod
    def match_order_id(order_id):
        return lambda instance: instance.order_id == order_id

    @staticmethod
    def match_employee_id(employee_id):
        return lambda instance: instance.employee_id == employee_id

    @staticmethod
    def match_product_id(product_id):
        return lambda instance: instance.product_id == product_id

    @staticmethod
    def match_customer_id(customer_id):
        return lambda instance: instance.customer_id == customer_id


class OrderQuery:
    @staticmethod
    def get_report(order_id):
        order = next(filter(
            Matcher.match_order_id(order_id), OrderReader.get_instances()))
        order_details = filter(
                Matcher.match_order_id(order_id),
                OrderDetailReader.get_instances())
        products = ProductReader.get_instances()
        result = "-"*10 + "\n"
        result += f"ORDER #{order.order_id}\n"
        result += "-"*10 + "\n"
        product_table = PrettyTable(["Product Name", "Unit", "Unit Price ($)",
                                     "Quantity", "Cost ($)"])
        total_cost = 0
        for order_detail in order_details:
            cost = order_detail.unit_price * order_detail.quantity
            total_cost += cost
            product = next(filter(
                Matcher.match_product_id(order_detail.product_id),
                products))
            product_table.add_row([product.product_name,
                                   product.quantity_per_unit,
                                   order_detail.unit_price,
                                   order_detail.quantity, cost])
        result += str(product_table) + "\n"
        result += f"Shipping fee: ${order.shipping_fee}\n"
        total_cost += order.shipping_fee
        result += f"Total cost: ${total_cost}\n"
        result += "-"*10 + "\n"
        result += f"Order date: {order.order_date}\n"
        result += f"Shipped date: {(order.shipped_date or 'Not yet')}\n"
        return result
