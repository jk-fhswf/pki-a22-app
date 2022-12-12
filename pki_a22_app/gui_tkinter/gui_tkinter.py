import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import cv2
from PIL import Image, ImageTk

#init
root = tk.Tk()
root.title('Projekt Gruppe A2-2')

#Window width x height
window_w = 800
window_h = 600

#Bildschirm width x height
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

#Bildschirmmitte
center_x = int(screen_w/2 - window_w / 2)
center_y = int(screen_h/2 - window_h / 2)

#Fenster mittig auf Bildschirm ausrichten
root.geometry(f'{window_w}x{window_h}+{center_x}+{center_y}')

#Fenstergroesse Ändern sperren
root.resizable(False, False)

#Textlabel
message = tk.Label(root, text="Hello, World!")
message.pack()

message2 = tk.Label(root, text="Hello, World!")
message2.pack()

#Button Funktion mit Callback
def select(option):
    print(np.add(s1.get_val(),10))
    
def fileopen():
    path = tk.filedialog.askopenfilename()
    print (path)
    message.config(text=path)
    #return path

b1 = ttk.Button(root, text='Button 1', command=lambda: select('Button 1'))
b1.pack()
b2 = ttk.Button(root, text='Button 2', command=lambda: select('Button 2'))
b2.pack()
b3 = ttk.Button(root, text='Datei öffnen', command=lambda: fileopen())
b3.pack()

#=====================
#CLASS Slider
#=====================
class slider:    
    def __init__(self,name,x_pos=0,y_pos=0):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.val = tk.IntVar() #Rückgabewerte des Slider, abfragen mit self.get_val()
        
        self.lbl = ttk.Label(root, text=name)
        self.lbl.place(x=self.x_pos,y=self.y_pos)
        
        self.s = ttk.Scale(root, from_=0, to=100, orient="horizontal",command=self.slider_change,variable=self.val)
        self.s.place(x=self.x_pos+100,y=self.y_pos)
        
        self.v = ttk.Label(root,text=self.get_val())
        self.v.place(x=self.x_pos+210,y=self.y_pos)
    def get_val(self):
        return self.val.get()
    def slider_change(self, event):
        self.v.configure(text=self.get_val())
        message2.config(text=str(self.get_val()))



path = r"C:\Users\Peter\Desktop\Studium\01_Semester\01_Programmierung für KI\Projekt\Logo.jpg"
#path = tk.filedialog.askopenfilename()
image = Image.open(path)
python_image = ImageTk.PhotoImage(image)
ttk.Label(root, image=python_image).pack()

#python_image = tk.PhotoImage(file=path)
#ttk.Label(root, image=python_image).place(x=0,y=0)

xpos_slider_window = 250
ypos_slider_window = 200
s1 = slider("ScaleFactor",xpos_slider_window,ypos_slider_window)
s2 = slider("MinNeighbors",xpos_slider_window,ypos_slider_window+30)
s3 = slider("minSize",xpos_slider_window,ypos_slider_window+60)
s4 = slider("maxSize",xpos_slider_window,ypos_slider_window+90)

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc
variable = tk.StringVar(root)
variable.set(OPTIONS[0]) # default value
w = tk.OptionMenu(root, variable, *OPTIONS)
w.place(x=0,y=0)

root.mainloop()