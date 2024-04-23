# This program demonstrates the Canvas Widget
import tkinter

class MyGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create the Canvas widget
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Draw two ovals
        self.canvas.create_oval(20,20,70,70)
        self.canvas.create_oval(100,100,180,130)
        

        

        # Pack the canvas
        self.canvas.pack()

        # Main loop
        tkinter.mainloop()

# Create object
my_gui = MyGUI()

        
