# THis program demonstrates a button widget
# When the user clicks the button, an
# info dialog box is displayed

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # create the main windows
        self.main_window = tkinter.Tk()

        # Create a button widget. The text 'Click Me!' 
        # shoudl appear on the face of the button. The 
        # do_something method shoudl be executed when
        # the user clicks the Button

        self.my_button = tkinter.Button(self.main_window, text = 'Click Me!', \
                                        command=self.do_something)
        
        # Pack the button
        self.my_button.pack()

        # Main Loop
        tkinter.mainloop()

    # The do_something method is a call back function
    # for the button widget

    def do_something(self):
        # Display an info box
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')

# Create the object


my_gui = MyGUI()
