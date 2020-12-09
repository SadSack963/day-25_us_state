"""Hello,

If you want to use Tkinter and want some tips :
- Create a canvas then add an image like in section 28 with pack()
- You can start the game clicking on the canvas. In this case, add the binding.
(Note that I created a class for my UI):"""

    # mouseclick event
    self.canvas.bind("<Button 1>", self.on_click)

"""In the on_click method you can access to the pointer coordinates :"""

    def on_click(self, event):
        x, y = self.printcoords(event)

"""and more important you start the loop here.
To open a dialog box, you can use this :"""

    def open_dialog_popup(self):
        title = f"States founded : {self.good_answers}/50"
        self.dialog_box = simpledialog.askstring(title, "Quel est ce pays ?")
        if self.dialog_box:
            self.dialog_box = self.dialog_box.title()

"""you need to import this from the tkinter library :"""

    from tkinter import simpledialog

"""One more thing, the coordinate system is not the same. On turtle the (0,0) is in the center, 
whereas on the tkinter canvas, it's in the upper left corner. Therefore you have to modify the data.
This function does the job :"""

    def convert_csv(file_from, file_to):
        data = pandas.read_csv(file_from)
        data_column_x = data.x + IMG_WIDTH / 2
        data_column_y = - data.y + IMG_HEIGHT / 2
        data_dict = {
            "state": data.state.to_list(),
            "x": data_column_x.to_list(),
            "y": data_column_y.to_list()
        }
        new_data = pandas.DataFrame(data_dict)
        new_data.to_csv(file_to)

"""Have fun with Tkinter, adding buttons and more !"""