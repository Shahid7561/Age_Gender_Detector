import tkinter as tk
from tkinter import filedialog
from tkinter import *

from keras.models import load_model
from PIL import Image,ImageTk
import numpy as np
import cv2

# Loading the model
model = load_model('Age_Sex_Detection.h5')

# Initializing the GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Age & Gender Detector')
top.configure(background='#CDCDCD')

# Initializing the labels (1 for age and 1 for sex)
label1 = Label(top,background='#CDCDCD', font=('arial',15,'bold'))
label2 = Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

# Defining Detect Function which detects the age and gender of the person in image using the model
def Detect(file_path):
    global Label_packed
    image = Image.open(file_path)
    image=image.resize((48,48))
    image=np.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    sex_f = ['Male','Female']
    image = np.array([image])/255
    pred = model.predict(image)
    age = int(np.round(pred[1][0]))
    sex = int(np.round(pred[0][0]))
    print("Predicted Age is: " + str(age))
    print("Pridicted Gender is: " + sex_f[sex])
    label1.configure(foreground='#011638',text=age)
    label2.configure(foreground='#011638',text=sex_f[sex])


# Defining the show detect button function
def show_detect_button(file_path):
    detect_b = Button(top,text='Detect Image',command=lambda:Detect(file_path),padx=10,pady=5)
    detect_b.configure(background='#364156',foreground='white',font=('arial',10,'bold'))
    detect_b.place(relx=0.79,rely=0.46)


# Defining the upload image function
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label1.configure(text = '')
        label2.configure(text = '')
        show_detect_button(file_path)
    except:
        pass

upload = Button(top,text = "Upload Image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156',foreground='white',font=('arial',20,'bold'))
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand='True')
label1.pack(side='bottom',expand='True')
label2.pack(side='bottom',expand='True')
heading = Label(top,text='Emotion Detector',pady=20,font=('arial',25,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
