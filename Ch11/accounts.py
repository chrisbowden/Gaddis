# The SavingsAccount class represents a
# savings account

class SavingsAccount:
    # The __init__ should accept arguments for the
    # account number, interest rate and balance

    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__int_rate = int_rate
        self.__balance = bal

    # The following are the mutators

    def set_account_num(self, account_num):
         self.__account_num = account_num

    def set_interest_rate(self, int_rate):
         self.__int_rate = int_rate

    def set_balance(self, bal):
         self.__balance = bal

    # These are the accessor methods
    
    def get_account_num(self):
         return self.__account_num
    
    def get_interest_rate(self):
         return self.__int_rate
    
    def get_balance(self):
         return self.__balance
    
# The CD account represents a certificate of
# deposit (CD) account. It is a subclass of
# the SavingsAccount class
    
class CD(SavingsAccount):
     
     # Init accepts account number, interest rate, balance
     # and maturity date

    def __init__(self, account_num, int_rate, bal, mat_date):
        # Start by calling the SavingsAccount class init first
        SavingsAccount.__init__(self, account_num, int_rate, bal)

        # Init the new attribute
        self.__maturity_date = mat_date

    # The set_maturity_date is the mutator methid
    def set_maturity_date(self, mat_date):
         self.__maturity_date = mat_date

    # The accessor
    def get_maturity_date(self):
         return self.__maturity_date
    
                   
    
