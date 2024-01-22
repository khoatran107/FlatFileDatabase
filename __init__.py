from EmployeeUI import EmployeeUI
from OwnerUI import OwnerUI

ownerUI = OwnerUI()
authenticated = ownerUI.authenticate()
if not authenticated:
    exit()
ownerUI.run()

'''
employeeUI = EmployeeUI()
authenticated = employeeUI.authenticate()
if not authenticated:
    exit()
employeeUI.run()
'''
