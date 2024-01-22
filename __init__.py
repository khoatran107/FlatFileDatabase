from EmployeeUI import EmployeeUI
from OwnerUI import OwnerUI
from CustomerUI import CustomerUI

UI_controllers = [CustomerUI, OwnerUI, EmployeeUI]
displays = ["Customer", "Owner", "Employee"]

for index, display in enumerate(displays):
    print(index, display, sep='. ')

selected_index = int(input('> Who are you?: '))
controller = UI_controllers[selected_index]()
authenticated = controller.authenticate()
if not authenticated:
    exit()
controller.run()

'''
customerUI = CustomerUI()
authenticated = customerUI.authenticate()
if not authenticated:
    exit()
customerUI.run()

ownerUI = OwnerUI()
authenticated = ownerUI.authenticate()
if not authenticated:
    exit()
ownerUI.run()

employeeUI = EmployeeUI()
authenticated = employeeUI.authenticate()
if not authenticated:
    exit()
employeeUI.run()
'''
