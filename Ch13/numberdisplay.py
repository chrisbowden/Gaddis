# This is a class module for the NumberDisplay
# used in the clock application

# Limit and value

class NumberDisplay:
    def __init__(self, rolloverlimit):
        self.__limit = rolloverlimit # This represents the maximum value the display can hold
        self.__value = 0 # This is the current value of the display

    def getValue(self):
        return self.__value
    
    def getDisplayValue(self): # Returns a string value
        if self.__value < 10:
            return '0' + self.__value
        else:
            return '' + self.__value

    def setValue(self, replacementvalue):
        # setValue - Updates current value - checks more than zero and less than limit
        if replacementvalue >= 0 and replacementvalue < self.__limit:
            self.__value = replacementvalue
 
    def increment(self):
        self.__value = (self.__value +1) % self.__limit








