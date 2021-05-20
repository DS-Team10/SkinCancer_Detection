from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

import tensorflow as tf
import cv2
import os

root=Tk()
root.geometry('740x600')
#root.resizable(0,0)
root.iconbitmap('')
root.title('Skin Cancer Detector')
root.config(bg='white')
root.iconbitmap(r'C:\Users\new\Downloads\project_icon.ico')

img = 'C:/Users/new/OneDrive/Desktop/img.jpg'
color='white'

types=['Benign','Malignant']
#model=tf.keras.models.load_model('B-vs-M-64x2-1621331197.h5')
def prediction(filepath):
    global types
    #print(filepath)
    model=tf.keras.models.load_model(r'C:\Users\new\AJ_PROJECT\B-vs-M-64x2-1621331197.h5')
    size=50
    img_array=cv2.imread(filepath)
    img_array=cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    new_array=cv2.resize(img_array,(size,size))
    result=model.predict(new_array.reshape(-1,size,size,3))
    predicted_name.config(text=types[int(result[0][0])])
    #return new_array.reshape(-1,size,size,3)

def openfile():
    global img
    root.filename=filedialog.askopenfilename(initialdir=r"C:\Users\new\AJ_PROJECT",title='Select an image',filetypes=(('jpg files','*.jpg'),('all files','*.*')))
    root.filename.replace('\/','/')
    img=root.filename
    re_size=Image.open(img)
    re_size=re_size.resize((300,300))
    image=ImageTk.PhotoImage(re_size)
    default_img.configure(image=image)
    default_img.image=image
    #print(img)

def removefile():
    global img
    img='C:/Users/new/OneDrive/Desktop/img.jpg'
    re_size=Image.open(img)
    re_size=re_size.resize((300,300))
    image=ImageTk.PhotoImage(re_size)
    default_img.configure(image=image)
    default_img.image=image
    predicted_name.config(text='')

frame=Frame(root)
frame.pack(pady=10,padx=10)

img_frame=Frame(frame,bg=color,padx=10,pady=10)
img_frame.grid(row=0,column=0,pady=10,padx=10)

predicted_name=Label(img_frame,text='',bg=color,fg='green',font=('sans-serif',20),padx=20,pady=10)
predicted_name.grid(row=1,column=1)

image=Image.open(img)
image=ImageTk.PhotoImage(image)

default_img=Label(img_frame,image=image)
default_img.grid(row=0,column=1,columnspan=2)

button_frame=Frame(frame,bg=color,padx=5,pady=10)
button_frame.grid(row=1,column=0)

open_image=Button(button_frame,text="Upload Image",command=openfile,font=('sans-serif',20),bg='#3333ff',fg='white',pady=20,padx=20,bd=0)
open_image.grid(row=1,column=0,padx=5,pady=5)

remove_image=Button(button_frame,text="Remove Image",command=removefile,font=('sans-serif',20),bg='#3333ff',fg='white',pady=20,padx=20,bd=0)
remove_image.grid(row=1,column=1,padx=(0,5),pady=5)

predict_button=Button(button_frame,text="Predict Image",command=lambda:prediction(img),font=('sans-serif',20),bg='#3333ff',fg='white',pady=20,padx=20,bd=0)
predict_button.grid(row=1,column=2)


    
#prediction1=model.predict([prepare(os.path.abspath('melanoma.jpg'))])
#prediction2=model.predict([prepare(os.path.abspath('benign.jpg'))])
#print(prediction1)
#print(prediction2)


root.mainloop()