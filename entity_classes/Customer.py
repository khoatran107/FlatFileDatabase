class Customer:
    def __init__(self, line=','*6):
        args = line.split(',')
        self.customer_id = args[0]
        self.company_name = args[1]
        self.first_name = args[2]
        self.last_name = args[3]
        self.job_title = args[4]
        self.city = args[5]
        self.state = args[6]


class CustomerBuilder:
    def __init__(self):
        self.customer = Customer()

    def set_customer_id(self, customer_id):
        self.customer.customer_id = customer_id

    def set_company_name(self, company):
        self.customer.company_name = company

    def set_first_name(self, first_name):
        self.customer.first_name = first_name

    def set_last_name(self, last_name):
        self.customer.last_name = last_name

    def set_job_title(self, job_title):
        self.customer.job_title = job_title

    def set_city(self, city):
        self.customer.city = city

    def set_state(self, state):
        self.customer.state = state

    def build(self):
        return self.customer
