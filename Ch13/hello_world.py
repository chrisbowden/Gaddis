# This program displays a label with text

import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create a label widget containing the text
        # Hello World!
        self.label = tkinter.Label(self.main_window, text = "Hello World!")

        # Call the label widget's pack method
        self.label.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

# Create and instance of the MyGUI class
my_gui = MyGUI()