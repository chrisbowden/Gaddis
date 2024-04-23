import tkinter

class MyGUI:
    def __init__(self):
        # Create the main windows
        self.main_window = tkinter.Tk()

        # Create two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create 3 string labels that will hold the address lines
        self.line1 = tkinter.StringVar()
        self.line2 = tkinter.StringVar()
        self.line3 = tkinter.StringVar()

        
        # Create three labels in the top frame and associate them with the vars
        self.label_line1 = tkinter.Label(self.top_frame, textvariable=self.line1)
        self.label_line2 = tkinter.Label(self.top_frame, textvariable=self.line2)
        self.label_line3 = tkinter.Label(self.top_frame, textvariable=self.line3)
        
        # Now we pack the buttons
        self.label_line1.pack()
        self.label_line2.pack()
        self.label_line3.pack()
        

        # Create the bottom frame buttons
        self.show_info_button = tkinter.Button(self.bottom_frame, text='Show Info',
                                               command=self.populate_message)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit',
                                         command=self.main_window.destroy)

        # Pack the buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Create the main loop
        tkinter.mainloop()

    def populate_message(self):
        # Set the variables to be displayed
        self.line1.set('Line One')
        self.line2.set('Line Two')
        self.line3.set('Line Three')



# Create the object
my_gui=MyGUI()


    