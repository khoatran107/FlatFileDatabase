from Controller import Controller
from DataReader import EmployeeReader, OrderReader
from Queries import OrderQuery, Matcher
from DataUpdater import OrderUpdater
from datetime import datetime


class EmployeeUI(Controller):
    def __init__(self):
        self.__options = ['See All My Orders',
                        'See Undone Orders',
                        'Do Order']
        self.__functions = [self.__show_orders,
                          self.__show_undone_orders,
                          self.__do_order]

    def authenticate(self):
        id = input("What's your employee id? ")
        employees = EmployeeReader.get_instances()
        for employee in employees:
            if employee.employee_id == id:
                self.employee = employee
                self.__get_orders()
                return True

        print("That employee id does not exist!")
        return False

    def run(self):
        if self.employee is None:
            return
        self.__print_menu()
        option_index = int(input("What's your option? "))
        self.__functions[option_index]()

    def __print_menu(self):
        for index, option in enumerate(self.__options):
            print(index, option, sep='. ')

    def __get_orders(self):
        self.__orders = list(filter(Matcher.match_employee_id(self.employee.employee_id),
                           OrderReader.get_instances()))
        self.__undone_orders = list(filter(lambda ord: not ord.shipped_date, self.__orders))

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

    def __do_order(self):
        order_id = input("ID of order: ")
        selected_order = next(filter(Matcher.match_order_id(order_id), self.__undone_orders), None)
        if selected_order is None:
            print("The order with that ID either has been completed or does not exist!")
            return
        selected_order.shipped_date = datetime.today().strftime('%m/%d/%Y')
        OrderUpdater.update(order_id, selected_order)
        print("Done!")
