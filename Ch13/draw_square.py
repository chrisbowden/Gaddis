# This program demonstrates the Canvas Widget
import tkinter

class MyGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create the Canvas widget
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Darw two lines
        self.canvas.create_rectangle(20,20,180,180, dash=(5,2), width=3)

        

        # Pack the canvas
        self.canvas.pack()

        # Main loop
        tkinter.mainloop()

# Create object
my_gui = MyGUI()

        
