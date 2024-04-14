# This program uses a GUI to get three test scores
# and display their average

import tkinter

class TestAverage:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create five frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack widgets for test1 frame
        self.test1_label = tkinter.Label(self.test1_frame, text='Enter a score for test 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Create and pack widgets for test2 frame
        self.test2_label = tkinter.Label(self.test2_frame, text='Enter a score for test 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame, width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')
        
        # Create and pack widgets for test1 frame
        self.test3_label = tkinter.Label(self.test3_frame, text='Enter a score for test 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame, width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # Create and pack widgets for the average
        self.result_label = tkinter.Label(self.avg_frame, text = 'Average:')
        self.avg = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.avg_frame, textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # Create and pack the button widgets
        self.calc_button = tkinter.Button(self.button_frame, text='Average', 
                                          command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit',
                                          command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Start the GUI loop
        tkinter.mainloop()

    # The clac_avg method is the callback function for the 
    # calc_button widget
    def calc_avg(self):
        # get the three test scores and store in variables
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # Calculate the average
        self.average = (self.test1 + self.test2 + self.test3 ) /3.0

        # Update the Avg label with the value
        self.avg.set(self.average)

# Create the object
test_avg = TestAverage()

        


        