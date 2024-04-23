# This is my Python version of the 
# Object Oriented Clock 

import numberdisplay

class ClockDisplay():
    def __init__(self):
        
        # Constructor - creates hours and minutes objects
        # calls updateDisplay
        hours = numberdisplay.NumberDisplay(24)
        minutes = numberdisplay.NumberDisplay(60)
        displayString=''
        self.updateDisplay
        
    def timeTick(self): # increments (calls) minutes via increment method
        # checks if new value is 0, and if so updates the hours as well
        self.minutes.increment()
        if (self.minutes.getValue()) == 0:
            self.hours.increment()
        

    def setTime(hours, minutes): #accepts new values for hours and minutes (time) and calls the set methods for each objects
        hours.setValue(hours)
        minutes.setValue(minutes)

    def getTime():# calls / returns string value for time - Calls the displayString method
        return displayString

    def updateDisplay(): # creates Display string by calling getDisplayValue for each objects
        displayString = hours.getDisplayValue() + ':' + minutes.getDisplayValue()

clock = ClockDisplay()






