# This program displays two labels with text

import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create two label widgets
        self.label1 = tkinter.Label(self.main_window, text = "Hello World!")
        self.label2 = tkinter.Label(self.main_window, text = "This is my GUI program")

        # Call the label widget's pack method
        self.label1.pack()
        self.label2.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

# Create and instance of the MyGUI class
my_gui = MyGUI()