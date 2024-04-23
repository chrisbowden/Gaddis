# This program draws a piechart on a canvas
import tkinter

class MyGUI:
    def __init__(self):
        self.__CANVAS_WIDTH = 320
        self.__CANVAS_HEIGHT = 240
        self.__X1 = 60
        self.__Y1 = 20
        self.__X2 = 260
        self.__Y2 = 220
        self.__PIE1_START = 0
        self.__PIE1_WIDTH = 45
        self.__PIE2_START = 45
        self.__PIE2_WIDTH = 90
        self.__PIE3_START = 135
        self.__PIE3_WIDTH = 120
        self.__PIE4_START = 255
        self.__PIE4_WIDTH = 105

        # Create the main window
        self.main_window = tkinter.Tk()

        # Create the canvas
        self.canvas = tkinter.Canvas(self.main_window, width=self.__CANVAS_WIDTH,
                                     height=self.__)
        