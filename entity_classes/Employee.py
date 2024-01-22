class Employee:
    def __init__(self, line=','*3):
        args = line.split(',')
        self.employee_id = args[0]
        self.first_name = args[1]
        self.last_name = args[2]
        self.title = args[3]
