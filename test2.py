import tkinter as tk
import os
import datetime
import platform
import cv2
from tkinter import messagebox 
from PIL import ImageTk,Image,ImageOps
from tkinter.filedialog import askopenfilename 





class Detector():
    def __init__(self,master):
        self.master = master
        self.current_date_and_time_string = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        self.file_path= os.getcwd()
        self.arroww = self.check_system()
        self.master.geometry('450x570')
        frame = tk.Frame(self.master, relief=tk.RIDGE, borderwidth=2)
        frame.pack(fill=tk.BOTH,expand=1)
        self.master.title('Social Distance Detector')
        self.master.resizable(False,False)
        # self.master.iconbitmap(self.file_path + self.arroww + "demo1_icon.ico")
        frame.config(background='light blue')
        self.file_path= os.getcwd()
        self.image = Image.open(self.file_path + self.arroww+ "demo1.jpg")
        self.image = ImageOps.fit(self.image, (500, 570))
        self.image = ImageTk.PhotoImage(self.image)
        test = tk.Label(frame, image = self.image, bg="#ffb8e1")
        test.pack()
        new_menu = tk.Menu(self.master)
        self.master.config(menu=new_menu)
        self.create_menu(menu=new_menu,labels1='Tools',labels2='set configuration',menu_command=self.confo)
        self.create_menu(menu=new_menu,labels1='Help',labels2='open cv docs',menu_command=self.hel)
        self.create_menu(menu=new_menu,labels1='About',labels2='Social Distance Detector',menu_command=self.anotherWin)
        self.button(frame=frame,width=39,button_command=self.web,text="open cam",x=5,y=104)
        self.button(frame=frame,width=39,button_command=self.webrec,text="Open Cam & Record",x=5,y=176)
        self.button(frame=frame,width=39,button_command=self.webdet,text="Open Cam & Detect",x=5,y=250)
        self.button(frame=frame,width=39,button_command=self.webdetrec,text="Select File to Detect",x=5,y=322)
        self.button(frame=frame,width=5,button_command=self.exitt,text="EXIT",x=210,y=478)


    def check_system(self):
        if platform.system() == "Linux":
            arroww = "/"
        else:
            arroww = "\\"
        return arroww


    def hel(self):
        help(cv2)

    def anotherWin(self):
       messagebox.showinfo("About",'Social Distance Detector version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')

        
    def open_app(self):
        filename= askopenfilename(parent=root,initialdir=os.getcwd(),title="Select File",filetypes=[
                    ("all video format", ".mp4"),
                    ("all video format", ".flv"),
                    ("all video format", ".avi"),
                    ("All files","*.*")
                ])
   #  print(filename)
        return(filename)

    def web(self):
        capture =cv2.VideoCapture(0)
        while True:
            ret,frame=capture.read()
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()

    def webrec(self):
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
    

    def webdet(self):
        os.system('python social_distance_detector.py')
   

    def webdetrec(self):
        self.file_name=self.open_app()
        self.master.update()
        os.system('python social_distance_detector.py -i ' + str(self.file_name) + ' -o ' +'\"' + self.current_date_and_time_string + '.avi'+'\"')
        #  print('python social_distance_detector.py -i ' + str(file_name) + ' -o ' +'\"' + current_date_and_time_string + '.avi'+'\"')

    def nothing(self):
        pass

    def exitt(self):
        exit()

    def button(self,frame,width=39,button_command=nothing,text="error",x=5,y=104):
        but1=tk.Button(frame,padx=0,pady=5,width=width,bg='white',fg='black',relief=tk.GROOVE,command=button_command,text=text,font=('helvetica 15 bold'))
        but1.place(x=x,y=y)


    def create_menu(self,menu,labels1,labels2,menu_command):
        subm = tk.Menu(menu,tearoff=False)
        menu.add_cascade(label=labels1,menu=subm)
        subm.add_command(label=labels2,command=menu_command)
    
    def confo(self):
        self.app = configuration(self.master)


class configuration():
    def __init__(self,master):
        self.master=master
        self.app = tk.Toplevel(self.master)
        self.app.title('Configuration settings')
        self.app.geometry('450x570')
        self.weight_value = self.entry(app=self.app,text='Select weight:',x1 = 5,y1 = 90,x2 = 240,y2 = 90,default_value = "yolov3-tiny.weights", options = ["yolov3-tiny.weights", "yolov3.weights"],entry_command=self.callback)
        self.con_value = self.entry(app=self.app,text='Select configuration file:',x1 = 5,y1 = 120,x2 = 240,y2 = 120,default_value = "yolov3-tiny.cfg", options = ["yolov3-tiny.cfg", "yolov3.cfg"],entry_command=self.callback)
        self.threshold_value = self.entry(app=self.app,text='Select threshold:',x1 = 5,y1 = 150,x2 = 240,y2 = 150,default_value = 0.5, options = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],entry_command=self.callback)
        self.gpu_value = self.entry(app=self.app,text='Select GPU:',x1 = 5,y1 = 180,x2 = 240,y2 = 180,default_value = False, options = [False,True],entry_command=self.callback)
        self.dist_value = self.entry(app=self.app,text='Select Distance:',x1 = 5,y1 = 210,x2 = 240,y2 = 210,default_value = 0.5, options = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],entry_command=self.callback)
        self.config_value = self.entry(app=self.app,text='Select Configuration:',x1 = 5,y1 = 240,x2 = 240,y2 = 240,default_value = 0.3, options = ["yolov3-tiny.weights", "yolov3.weights"],entry_command=self.callback)
        self.save_button(app=self.app,save_text='save',x1=240,y1=450)


    def button_click(self,con,threshold,gpu,dist,weight,config):
        # self.app.update()
        tk.file = open("config.py","w")
        tk.file.writelines("MIN_CONF = "+ str(con)+"\n")
        tk.file.writelines("NMS_THRESH = "+ str(threshold)+"\n")
        tk.file.writelines("USE_GPU = "+ str(gpu)+"\n")
        tk.file.writelines("MIN_DISTANCE = "+ str(dist)+"\n")
        tk.file.writelines('WEIGHT_PATH = '+ '"'+str(weight)+'"'+"\n")
        tk.file.writelines("CONFIG_PATH = "+'"'+ str(config)+'"')
        tk.file.close()
        self.app.update()
        self.master.update()
        self.app.destroy()

    def save_button(self,app,save_text,x1,y1):
        button = tk.Button(app,text=save_text, command=self.button_click(con=self.con_value,threshold=self.threshold_value,gpu=self.gpu_value,dist=self.dist_value,weight=self.weight_value,config=self.config_value))
        button.pack()
        button.place(x=x1,y=y1)


    def callback(self,selection):
        return selection
        #print(selection)


    def entry(self,app,text,x1,y1,x2,y2,default_value,options,entry_command):
        label = tk.Label(app, text = text)
        label.pack()
        label.place(x=x1,y=y2)

        value = tk.StringVar(app)
        value.set(default_value) # default value

        w = tk.OptionMenu(app, value,options,command=entry_command(value))
        w.pack()
        w.place(x=x2,y=y2)





if __name__ == "__main__":
    root = tk.Tk()
    Detector(root)
    root.mainloop()
