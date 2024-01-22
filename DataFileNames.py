from os import path


class DataFileNames:
    database_folder = 'database'
    customer_file_name = path.join(database_folder, 'customers.txt')
    employee_file_name = path.join(database_folder, 'employees.txt')
    product_file_name = path.join(database_folder, 'products.txt')
    order_file_name = path.join(database_folder, 'orders.txt')
    order_detail_file_name = path.join(database_folder, 'order_detail.txt')
