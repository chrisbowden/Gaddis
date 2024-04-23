# This program demonstrates the Canvas Widget
import tkinter

class MyGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create the Canvas widget
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Darw two lines
        self.canvas.create_line(10,10,189,10,100,189,10,10)
        

        # Pack the canvas
        self.canvas.pack()

        # Main loop
        tkinter.mainloop()

# Create object
my_gui = MyGUI()

        