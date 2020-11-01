##  In this Project we want to build an Image Slider in which show our images in order and in
##      specific time delay that we set

import tkinter as tk
from itertools import cycle  ## use cycle to have the reputative App


class App(tk.Tk):  # Parameter in the defined class
    def __init__(self, image_file, x, y, delay):                    # Define function in class and Parameter
        tk.Tk.__init__(self)                                        # Use Tk interface
        self.geometry('+ {}+ {}'format(x, y))                       # use the picture to size the window that show
        self.delay = delay                                          # define the Delay in the class
        self.picture = cycle((tk.PhotoImage(file=image), image)     # cycle the images in imeg_file list
                             for image in image_file)               # PhotoImage class is used to display images
        self.picture_display = tk.Label(self)
        self.picture_display.pack()

    def show_slides(self):
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()

    delay = 3500                                                    # milisec
    image_file = ['Images']
    x = 100
    y = 50
    app = App(image_file, x, y, delay)
    app.show_slides()
    app.run()
