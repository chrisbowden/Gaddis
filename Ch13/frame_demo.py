# The program creates labels in 2 different frames

import tkinter

class MyGUI:
    def __init__(self):
        # Create main window widget
        self.main_window = tkinter.Tk()

        # Create 2 frames, one for the top op the
        # window and one for the bottom

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the three label widgets
        self.label1 = tkinter.Label(self.top_frame, text = 'Winken')
        self.label2 = tkinter.Label(self.top_frame, text = 'Blinken')
        self.label3 = tkinter.Label(self.top_frame, text = 'Nod')

        # Pack the labels in the top frame
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # Create three label widgets for the bottom frame
        self.label4 = tkinter.Label(self.bottom_frame, text = 'Winken')
        self.label5 = tkinter.Label(self.bottom_frame, text = 'Blinken')
        self.label6 = tkinter.Label(self.bottom_frame, text = 'Nod')

        # Pack the three bottom labels
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')
        
        # We need to pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the main loop
        tkinter.mainloop()

# Create the instance of the MyGui class
my_gui = MyGUI()


