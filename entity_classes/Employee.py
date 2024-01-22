class Employee:
    def __init__(self, line=','*3):
        args = line.split(',')
        self.employee_id = args[0]
        self.first_name = args[1]
        self.last_name = args[2]
        self.title = args[3]


class EmployeeBuilder:
    def __init__(self):
        self.employee = Employee()

    def set_employee_id(self, id):
        self.employee.employee_id = id

    def set_first_name(self, first_name):
        self.employee.first_name = first_name

    def set_last_name(self, last_name):
        self.employee.last_name = last_name

    def set_title(self, title):
        self.employee.title = title

    def build(self):
        return self.employee
