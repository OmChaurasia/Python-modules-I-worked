from tkinter import *
import cv2
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
root = Tk()
root.title("hello")
root.geometry("500x500")

start=(0,0)
end=(0,0)

l1=t1=r1=b1=(0,0)


def openfileselectionbox():
    filepath= filedialog.askopenfilename(title="Select an Image file", filetypes=(("PNG files" ,"*.png"),("JPG files","*.jpg")))
    img= cv2.imread(filepath)
    end= img.shape[0],img.shape[1]
    canvas=Canvas(root, width=img.shape[1], height=img.shape[0], )
    img= ImageTk.PhotoImage(Image.open(filepath))
    canvas.pack()
    canvas.create_image(10,10,anchor=NW,image=img)
    # messagebox.showinfo("showinfo", "file fetch")

button = Button(root, text = 'Select File',command=openfileselectionbox)
button.pack(side = TOP, pady = 5)


root.mainloop()
