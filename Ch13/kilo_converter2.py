# This program converts distances in kilometres
# to miles. The result is displayed in a lebel
# on the main window

import tkinter

class KiloConverterGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in kilometres:')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # pack the top frame widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Create middle frame widgets
        self.descr_label = tkinter.Label(self.mid_frame, text='Converted to miles:')

        # We need to create a StingVar object to associate with
        # an ouput label. Use the object's set method
        # to store a string of blank characters
        self.value = tkinter.StringVar()
        
        # Create a label and associate it with the StringVar object
        # Any value stored on the StringVar object
        # will be automatically displayed in the label
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # pack the mid frame widgets
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        # Create the button widgets in the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', 
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit',
                                          command=self.main_window.destroy)
        
        # Pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Main loop
        tkinter.mainloop()

    def convert(self):
        # get the value entered into the entry box
        kilo = float(self.kilo_entry.get())    

        # Convert to miles
        miles = kilo * 0.6214

        # Convert miles to a string and store
        # in the StringVar object. This will auto update
        # the miles_label widget
        self.value.set(miles)

# Main
kilo_conv = KiloConverterGUI()
