# This program creates an emoty window
# but uses OOP

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Enter the tkinter main loop
        tkinter.mainloop()

# Create and instance of the MyGUI class
my_gui = MyGUI()

