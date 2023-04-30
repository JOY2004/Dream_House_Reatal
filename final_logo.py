from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# Load image
image = Image.open("dream.png")

# Create PhotoImage object
photo = ImageTk.PhotoImage(image)

# Create Label widget
label = Label(image=photo)

# Add Label widget to window
label.pack()

root.mainloop()
