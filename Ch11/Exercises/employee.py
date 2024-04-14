# Start with Employee class

class Employee:
    def __init__(self, name, number):
        self.__emp_name = name
        self.__emp_num = number

    def get_emp_name(self):
        return self.__emp_name
    
    def get_emp_number(self):
        return self.__emp_num
    

class ProductionWorker(Employee):
    def __init__(self, name, number, snumber, pay):
        # Start by using the superclass inint
        Employee.__init__(self, name, number)

        self.__shift_number = snumber
        self.__pay_rate = pay

    def set_shift(self, snumber):
        self.__shift_number = snumber

    def get_shift(self):
        return self.__shift_number
    
    def get_pay_rate(self):
        return self.__pay_rate
    

    

    

