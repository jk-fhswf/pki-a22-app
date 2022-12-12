import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
#import cv2
from PIL import Image, ImageTk

#TKinter Fenster initialisieren (PS_2022-12-12)
root = tk.Tk()
root.title('Projekt Gruppe a2-2 - Thema: Bilderkennung Haar-Cascades')

#Fenster width x height (PS_2022-12-12)
window_width = 800
window_height = 600

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

#FH SWF Logo einbinden (PS_2022-12-12)
#fh_logo_path = r"C:\Users\Peter\Desktop\Studium\01_Semester\01_Programmierung für KI\Projekt\ressources\Logo.jpg"
fh_logo_path = "pki_a22_app\gui_tkinter\Logo.jpg"
fh_logo = Image.open(fh_logo_path)
fh_logo = fh_logo.resize((200,50), Image.ANTIALIAS)
fh_logo_tk = ImageTk.PhotoImage(fh_logo)
ttk.Label(root, image=fh_logo_tk).place(x=0,y=0)

#Textlabel Überschriften (PS_2022-12-12)
input_label = ttk.Label(root, text="INPUT IMAGE")
input_label.place(x=150,y=55)

output_label = ttk.Label(root, text="OUTPUT IMAGE")
output_label.place(x=550,y=55)

#Input Bild einbinden (PS_2022-12-12)
input_img_max_width = 350
input_img_max_height = 350
#input_img_path = r"C:\Users\Peter\Desktop\Studium\01_Semester\01_Programmierung für KI\Projekt\ressources\kokos.jpg"
input_img_path = "pki_a22_app\gui_tkinter\kokos.jpg"
input_img = Image.open(input_img_path)

width, height = input_img.size
if width > height:
    scalingfactor = input_img_max_width /width
    width = input_img_max_width
    height = int(height*scalingfactor)
else:
    scalingfactor = input_img_max_height/height
    height = input_img_max_height
    width = int(width*scalingfactor)

input_img = input_img.resize((width,height), Image.ANTIALIAS)
input_img_tk = ImageTk.PhotoImage(input_img)
ttk.Label(root, image=input_img_tk).place(x=25,y=75)

#Output Bild einbinden (PS_2022-12-12)
output_img_max_width = 350
output_img_max_height = 350
#input_img_path = r"C:\Users\Peter\Desktop\Studium\01_Semester\01_Programmierung für KI\Projekt\ressources\kokos.jpg"
output_img_path = "pki_a22_app\gui_tkinter\kokos.jpg"
output_img = Image.open(output_img_path)

width, height = output_img.size
if width > height:
    scalingfactor = output_img_max_width /width
    width = output_img_max_width
    height = int(height*scalingfactor)
else:
    scalingfactor = output_img_max_height/height
    height = output_img_max_height
    width = int(width*scalingfactor)

output_img = output_img.resize((width,height), Image.ANTIALIAS)
output_img_tk = ImageTk.PhotoImage(output_img)
output_img_tk_label = ttk.Label(root, image=output_img_tk)
output_img_tk_label.place(x=425,y=75)

#Bild öffnen Button (PS_2022-12-12)
def fileopen():
    path = tk.filedialog.askopenfilename()
    print (path)
    #output_img_tk_label.config(image=path)
    #return path
open_btn = ttk.Button(root, text='Bild öffnen', command=lambda: fileopen())
open_btn.place(x=150,y=450)

#Pulldown für Haar Cascades (PS_2022-12-12)
dropdown = [
"Eye Filter",
"Mouth Filter",
"Head Filter"
] #usw

dropdown_wahl = tk.StringVar(root)
dropdown_wahl.set(dropdown[0])

dropdown_label = tk.OptionMenu(root, dropdown_wahl, *dropdown)
dropdown_label.place(x=550,y=480)

def update():
    print (dropdown_wahl.get())
    #dropdown_label.pack()

update_btn = tk.Button(root, text="Output Update", command=update)
update_btn.place(x=550,y=450)

#Fenster Hauptschleife (PS_2022-12-12)
root.mainloop()