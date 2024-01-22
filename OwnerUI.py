from DataReader import ProductReader
from DataUpdater import ProductUpdater
from Controller import Controller
from entity_classes.Product import ProductBuilder
from prettytable import PrettyTable


class OwnerUI(Controller):
    def __init__(self):
        self.__options = ['Show All Products', 'Add a new product']
        self.__functions = [self.__show_products, self.__add_product]
        self.__authenticated = False

    def __check_password(self, password):
        return password == "hihihehe"

    def authenticate(self):
        password = input("What's the owner's password? ")
        if not self.__check_password(password):
            print("Wrong password!")
            return False
        print("Logged in successfully! What you wanna do?")
        self.__authenticated = True
        self.__get_products()
        return True

    def run(self):
        if not self.__authenticated:
            return
        self.__print_menu()
        option_index = int(input("What's your option? "))
        self.__functions[option_index]()

    def __print_menu(self):
        for index, option in enumerate(self.__options):
            print(index, option, sep='. ')

    def __get_products(self):
        self.__all_products = ProductReader.get_instances()

    def __show_products(self):
        product_table = PrettyTable(["Product ID", "Product Code",
                                     "Product Name", "Category",
                                     "Quantity Per Unit", "List Price"])
        for product in self.__all_products:
            product_table.add_row([product.product_id, product.product_code,
                                   product.product_name, product.category,
                                   product.quantity_per_unit, product.list_price])
        print(product_table)

    def __add_product(self):
        product_builder = ProductBuilder()
        print("Now enter the new product info")
        new_product = product_builder\
                        .set_product_id(input("Product ID: "))\
                        .set_product_code(input("Product Code: "))\
                        .set_product_name(input("Product Name: "))\
                        .set_category(input("Category: "))\
                        .set_quantity_per_unit(input("Quantity per unit: "))\
                        .set_list_price(float(input("Price: ")))\
                        .build()
        self.__all_products.append(new_product)
        ProductUpdater.add(new_product)
        print("New product added. Congrats!")
