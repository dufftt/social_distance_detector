import numpy
import time
import cv2
from tkinter import *
import tkinter.messagebox
import datetime
import os
from tkinter import filedialog
from PIL import Image,ImageTk,ImageOps
from tkinter import ttk 
import platform
# from test import detector,detect_people
# from social_distancing_config import L

if platform.system() == "Linux":
   arroww = "/"
else:
   arroww = "\\"

#Prepare file Path Name
current_date_and_time = datetime.datetime.now()

current_date_and_time_string = str(current_date_and_time)

file_path= os.getcwd()


root=Tk()
root.geometry('450x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Social Distance Detector')
root.resizable(False,False)
# root.iconbitmap(r"/demo1_icon.ico")
# root.tk.call('wm', 'iconphoto', root._w, PhotoImage(Image.open("./demo1_icon.ico")))
frame.config(background='light blue')
# label = Label(frame, text="Detector",bg='light blue',font=('Times 35 bold'))
# label.pack(side=TOP)


image = Image.open(file_path + arroww + "demo1.jpg")
image = ImageOps.fit(image, (500, 570))
image = ImageTk.PhotoImage(image)
test = Label(frame, image = image, bg="#ffb8e1")
test.pack()


# L = [0.3,0.3,50,False,'yolov3-tiny.cfg','yolov3-tiny.weights']





def save_info(threshold,con,dist,gpu,config,weight):
    file = open("config.py","w")
    file.writelines("MIN_CONF = "+ str(con)+"\n")
    file.writelines("NMS_THRESH = "+ str(threshold)+"\n")
    file.writelines("USE_GPU = "+ str(gpu)+"\n")
    file.writelines("MIN_DISTANCE = "+ str(dist)+"\n")
    file.writelines('WEIGHT_PATH = '+ '"'+str(weight)+'"'+"\n")
    file.writelines("CONFIG_PATH = "+'"'+ str(config)+'"')
    file.close()


def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributor","Sourav Sharma")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Social Distance Detector version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
   
                                  
   

def confo():
   #Enter configuration file here
   set_conf = Toplevel()
   set_conf.title('Configuration settings')
   set_conf.geometry('450x570')

   def callback(selection):
    print(selection)



   # weight path selection

   weight_label = Label(set_conf, text = 'Select weight:')
   weight_label.pack()
   weight_label.place(x=5,y=90)

   weight = StringVar(set_conf)
   weight.set("yolov3-tiny.weights") # default value

   w = OptionMenu(set_conf, weight, "yolov3-tiny.weights", "yolov3.weights",command=callback)
   w.pack()
   w.place(x=240,y=90)


   # config file selection

   config_label = Label(set_conf, text = 'Select Config:')
   config_label.pack()
   config_label.place(x=5,y=120)

   config = StringVar(set_conf)
   config.set("yolov3-tiny.cfg") # default value

   c = OptionMenu(set_conf, config, "yolov3-tiny.cfg", "yolov3.cfg",command=callback)
   c.pack()
   c.place(x=240,y=120)
   
   # GPU availablity

   gpu_label = Label(set_conf, text = 'Do you Have GPU:')
   gpu_label.pack()
   gpu_label.place(x=5,y=150)

   gpu = BooleanVar(set_conf)
   gpu.set(False) # default value

   g = OptionMenu(set_conf, gpu, True,False,command=callback)
   g.pack()
   g.place(x=240,y=150)


   # minimum distance

   dist_label = Label(set_conf, text = 'Select Minimum Distance:')
   dist_label.pack()
   dist_label.place(x=5,y=180)


   dist = IntVar(set_conf)
   dist.set(50) # default value

   d = OptionMenu(set_conf, dist, 10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100 ,command=callback)
   d.pack()
   d.place(x=240,y=180)

   # minimum configuration

   con_label = Label(set_conf, text = 'Select Minimum Configuration:')
   con_label.pack()
   con_label.place(x=5,y=210)


   con = DoubleVar(set_conf)
   con.set(0.3) # default value

   co = OptionMenu(set_conf, con, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,command=callback)
   co.pack()
   co.place(x=240,y=210)

   #minimum threshold

   thres_label = Label(set_conf, text = 'Select Minimum Threshold:')
   thres_label.pack()
   thres_label.place(x=5,y=240)

   threshold = DoubleVar(set_conf)
   threshold.set(0.3) # default value

   t = OptionMenu(set_conf, threshold, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,command=callback)
   t.pack()
   t.place(x=240,y=240)
  
   def but_click():
      
     
      set_conf.update()
      set_conf.destroy()
      root.update()
      save_info(threshold=threshold.get(),con=con.get(),dist=dist.get(),gpu=gpu.get(),config=config.get(),weight=weight.get())
    


   button1 = Button(set_conf, text='Save', command=but_click)
   button1.pack()
   button1.place(x=240,y=450)


menu = Menu(root)
root.config(menu=menu)

#Tools
subm1 = Menu(menu,tearoff=False)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Set Configuration",command=confo)

#Help
subm2 = Menu(menu,tearoff=False)
menu.add_cascade(label="Help",menu=subm2)
subm2.add_command(label="Open CV Docs",command=hel)

#About
subm3 = Menu(menu,tearoff=False)
menu.add_cascade(label="About",menu=subm3)
subm3.add_command(label="Social Distance Detection",command=anotherWin)
subm3.add_command(label="Contributors",command=Contri)



def exitt():
   exit()

def open_app():
    filename= filedialog.askopenfilename(parent=root,initialdir=os.getcwd(),title="Select File",filetypes=[
                    ("all video format", ".mp4"),
                    ("all video format", ".flv"),
                    ("all video format", ".avi"),
                    ("All files","*.*")
                ])
    return(filename)
    
  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,frame=capture.read()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter(current_date_and_time_string + '.avi',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   


   
def webdet():
    os.system('python social_distance_detector.py')
   


def webdetrec():
    file_name=open_app()
    root.update()
    # detector(file_name,L)
    os.system("python social_distance_detector.py -i " + str(file_name))


   
but1=Button(frame,padx=0,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=0,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Record',font=('helvetica 15 bold'))
but2.place(x=5,y=176)

but3=Button(frame,padx=0,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdet,text='Open Cam & Detect',font=('helvetica 15 bold'))
but3.place(x=5,y=250)


but4=Button(frame,padx=0,pady=5,width=39,bg='white',fg='black',relief=GROOVE,text='Select File to Detect',command=webdetrec,font=('helvetica 15 bold'))
but4.place(x=5,y=322)

but5=Button(frame,padx=0,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=210,y=478)




root.mainloop()