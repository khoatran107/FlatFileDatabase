from EmployeeUI import EmployeeUI

employeeUI = EmployeeUI()
authenticated = employeeUI.authenticate()
if not authenticated:
    exit()
employeeUI.run()
