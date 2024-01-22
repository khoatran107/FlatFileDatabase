from Controller import Controller
from DataReader import CustomerReader, OrderReader, ProductReader
from DataUpdater import OrderUpdater, OrderDetailUpdater
from Queries import OrderQuery, Matcher
from entity_classes.OrderDetail import OrderDetailBuilder
from entity_classes.Order import OrderBuilder
from prettytable import PrettyTable
from datetime import datetime


class CustomerUI(Controller):
    def __init__(self):
        self.__options = ['See All My Orders',
                          'See Undone Orders',
                          'Make New Order']
        self.__functions = [self.__show_orders,
                            self.__show_undone_orders,
                            self.__make_new_order]
        self.__order_details = []
        self.__all_products = []

    def authenticate(self):
        id = input("What's your customer id? ")
        customers = CustomerReader.get_instances()
        for customer in customers:
            if customer.customer_id == id:
                self.customer = customer
                self.__get_orders()
                return True

        print("That customer id does not exist!")
        return False

    def run(self):
        if self.customer is None:
            return
        self.__print_menu()
        option_index = int(input("What's your option? "))
        self.__functions[option_index]()

    def __print_menu(self):
        for index, option in enumerate(self.__options):
            print(index, option, sep='. ')

    def __get_orders(self):
        self.__orders = list(filter(
            Matcher.match_customer_id(self.customer.customer_id),
            OrderReader.get_instances()))
        self.__undone_orders = list(filter(
            lambda ord: not ord.shipped_date,
            self.__orders))

    def __show_orders(self):
        if not self.__orders:
            print("You have no orders")
        for order in self.__orders:
            print(OrderQuery.get_report(order.order_id))

    def __show_undone_orders(self):
        if not any(self.__undone_orders):
            print("You have no undone orders")
        for order in self.__undone_orders:
            print(OrderQuery.get_report(order.order_id))

    def __make_new_order(self):
        print("Let's order some stuff!")
        self.__new_order_id = OrderQuery.get_new_order_id()
        options = ['Add new product',
                   'Remove a product',
                   'Change quantity',
                   'Finish the order',
                   'Cancel the order']
        EXIT_INDICES = [len(options)-1, len(options)-2]
        functions = [self.__add_new_product,
                     self.__remove_product,
                     self.__change_quantity,
                     self.__finish_order,
                     self.__cancel_order]
        while True:
            for index, option in enumerate(options):
                print(index, option, sep='. ')
            option_index = int(input("What's your option? "))
            functions[option_index]()
            if option_index in EXIT_INDICES:
                break

    def __add_new_product(self):
        self.__show_products()
        product_id = input("> Enter the product ID: ")
        product = next(filter(
            lambda prod: prod.product_id == product_id,
            self.__all_products), None)
        if product is None:
            print("Please enter the right product ID!")
            return
        quantity = int(input("> Enter the quantity: "))
        unit_price = product.list_price
        order_detail = OrderDetailBuilder()\
            .set_product_id(product_id)\
            .set_quantity(quantity)\
            .set_unit_price(unit_price)\
            .set_order_id(self.__new_order_id)\
            .build()
        self.__order_details.append(order_detail)

    def __remove_product(self):
        pass

    def __change_quantity(self):
        pass

    def __finish_order(self):
        new_order = OrderBuilder()\
            .set_order_id(self.__new_order_id)\
            .set_customer_id(self.customer.customer_id)\
            .set_order_date(datetime.today().strftime('%m/%d/%Y'))\
            .build()
        OrderUpdater.add(new_order)
        for order_detail in self.__order_details:
            OrderDetailUpdater.add(order_detail)
        self.__empty_order()
        print("Ordered Successfully!")

    def __cancel_order(self):
        self.__empty_order()
        print("Ordered Canceled.")

    def __empty_order(self):
        self.__order_details = []
        self.__new_order_id = None

    def __show_products(self):
        product_table = PrettyTable(["Product ID", "Product Code",
                                     "Product Name", "Category",
                                     "Quantity Per Unit", "List Price"])
        if not self.__all_products:
            self.__all_products = ProductReader.get_instances()
        for product in self.__all_products:
            product_table.add_row([product.product_id, product.product_code,
                                   product.product_name, product.category,
                                   product.quantity_per_unit, product.list_price])
        print(product_table)
