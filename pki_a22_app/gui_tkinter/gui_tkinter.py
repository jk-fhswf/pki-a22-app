import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import cv2
from PIL import Image, ImageTk


#TKinter Fenster initialisieren (PS_2022-12-12)
root = tk.Tk()
root.title('Projekt Gruppe a2-2 - Thema: Bilderkennung Haar-Cascades')

#Fenster width x height (PS_2022-12-12)
window_width = 800
window_height = 600
img_max_width = 350
img_max_height = 350

#Bildschirm Auslösung width x height (PS_2022-12-12)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Fenstermitte auf Bildschirmmitte (PS_2022-12-12)
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

#Fenster ausrichten und Größe einstellen (PS_2022-12-12)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#Fenstergroesse Änderung sperren (PS_2022-12-12)
root.resizable(False, False)

def file_open():
    global input_image
    filename = filedialog.askopenfilename(filetypes=(("jpg files", "*.jpg"),("png files", "*.png")))
    input_image = Image.open(filename).resize((img_max_width,img_max_height), Image.ANTIALIAS)
    input_image_tk = ImageTk.PhotoImage(input_image)
    input_img_label.config(image=input_image_tk)
    input_img_label.image = input_image_tk
    
    output_image = input_image
    output_image_tk = ImageTk.PhotoImage(output_image)
    output_img_label.config(image=output_image_tk)
    output_img_label.image = output_image_tk
    
def img_change(classifier):
    #rel_path_haarcascade = "resources/haarcascades/"
    #haarcascade_frontalface_default
    #cascade = cv2.CascadeClassifier(rel_path_haarcascade + classifier + ".xml")
    output_image = Image.open("pki_a22_app\gui_tkinter\Logo.jpg").resize((img_max_width,img_max_height), Image.ANTIALIAS)
    output_image_tk = ImageTk.PhotoImage(output_image)
    output_img_label.config(image=output_image_tk)
    output_img_label.image = output_image_tk
    print(classifier)
    

#Fenster Hauptschleife (PS_2022-12-12)
tk.Button(root, text="Bild öffnen", command=file_open).place(x=150,y=50)
tk.Button(root, text="Classifier anwenden", command=lambda: img_change("test")).place(x=550,y=50)

input_img_label = ttk.Label(root)
input_img_label.place(x=25,y=100)

output_img_label = ttk.Label(root)
output_img_label.place(x=425,y=100)

root.mainloop()