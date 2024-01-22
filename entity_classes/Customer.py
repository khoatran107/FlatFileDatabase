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
