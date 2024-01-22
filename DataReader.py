from entity_classes.Customer import Customer
from entity_classes.Employee import Employee
from entity_classes.Product import Product
from entity_classes.Order import Order
from entity_classes.OrderDetail import OrderDetail
from DataFileNames import DataFileNames


class FileReader:
    @staticmethod
    def get_lines(filename):
        f = open(filename, 'r')
        lines = f.read().split('\n')
        lines = list(filter(None, lines))
        return lines


class DataReader:
    @staticmethod
    def read():
        pass

    @staticmethod
    def get_instances():
        pass


class CustomerReader(DataReader):
    @staticmethod
    def read():
        return FileReader.get_lines(DataFileNames.customer_file_name)

    @staticmethod
    def get_instances():
        return list(map(Customer, CustomerReader.read()))


class EmployeeReader(DataReader):
    @staticmethod
    def read():
        return FileReader.get_lines(DataFileNames.employee_file_name)

    @staticmethod
    def get_instances():
        return list(map(Employee, EmployeeReader.read()))


class ProductReader(DataReader):
    @staticmethod
    def read():
        return FileReader.get_lines(DataFileNames.product_file_name)

    @staticmethod
    def get_instances():
        return list(map(Product, ProductReader.read()))


class OrderReader(DataReader):
    @staticmethod
    def read():
        return FileReader.get_lines(DataFileNames.order_file_name)

    @staticmethod
    def get_instances():
        return list(map(Order, OrderReader.read()))


class OrderDetailReader(DataReader):
    @staticmethod
    def read():
        return FileReader.get_lines(DataFileNames.order_detail_file_name)

    @staticmethod
    def get_instances():
        return list(map(OrderDetail, OrderDetailReader.read()))
