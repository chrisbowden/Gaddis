# This program has a quit button that calls
# the Tk class's destroy method when clicked

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

        # Create a Quit button. Will call the destroy method when clicked
        self.quit_button = tkinter.Button(self.main_window, text = ' Quit', 
                                          command = self.main_window.destroy)

        # Pack the button
        self.my_button.pack()
        self.quit_button.pack()

        # Main Loop
        tkinter.mainloop()

    # The do_something method is a call back function
    # for the button widget

    def do_something(self):
        # Display an info box
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')

# Create the object


my_gui = MyGUI()
