import tkinter as tk
import os
import datetime
import platform
import cv2





class Detector():
    def __init__(self,master):
        self.master = master
        self.current_date_and_time_string = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        self.file_path= os.getcwd()
        self.arroww = check_system()
        self.master.geometry('450x570')
        frame = tk.Frame(master, relief=RIDGE, borderwidth=2)
        frame.pack(fill=BOTH,expand=1)
        self.master.title('Social Distance Detector')
        self.master.resizable(False,False)
        # root.iconbitmap(file_path + arroww + "demo1_icon.ico")
        frame.config(background='light blue')
        file_path= os.getcwd()
        image = tk.Image.open(file_path + arroww + "demo1.jpg")
        image = tk.ImageOps.fit(image, (500, 570))
        image = tk.ImageTk.PhotoImage(image)
        test = tk.Label(frame, image = image, bg="#ffb8e1")
        test.pack()
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        create_menu(menu,labels1='Tools',labels2='set configuration',menu_command=confo)
        create_menu(menu,labels1='Help',labels2='open cv docs',menu_command=hel)
        create_menu(menu,labels1='About',labels2='Social Distance Detector',menu_command=anotherWin)
        button(frame=frame,width=39,button_command=web,text="open cam",x=5,y=104)
        button(frame=frame,width=39,button_command=webrec,text="Open Cam & Record",x=5,y=176)
        button(frame=frame,width=39,button_command=webdet,text="Open Cam & Detect",x=5,y=250)
        button(frame=frame,width=39,button_command=webdetrec,text="Select File to Detect",x=5,y=322)
        button(frame=frame,width=39,button_command=exit,text="EXIT",x=210,y=478)


    def check_system(self):
        if platform.system() == "Linux":
            arroww = "/"
        else:
            arroww = "\\"
        return arroww


    def hel(self):
        tk.help(cv2)

    def anotherWin(self):
       tk.messagebox.showinfo("About",'Social Distance Detector version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')

        
    def open_app(self):
        filename= tk.filedialog.askopenfilename(parent=root,initialdir=os.getcwd(),title="Select File",filetypes=[
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
        file_name=open_app()
        self.master.update()
        os.system('python social_distance_detector.py -i ' + str(file_name) + ' -o ' +'\"' + current_date_and_time_string + '.avi'+'\"')
        #  print('python social_distance_detector.py -i ' + str(file_name) + ' -o ' +'\"' + current_date_and_time_string + '.avi'+'\"')

    def nothing(self):
        pass


    def button(self,frame,width=39,button_command=nothing,text="error",x=5,y=104):
        but1=tk.Button(frame=frame,padx=0,pady=5,width=width,bg='white',fg='black',relief=GROOVE,command=button_command,text=text,font=('helvetica 15 bold'))
        but1.place(x=x,y=y)


    def create_menu(self,menu,labels1,labels2,menu_command):
        subm = tk.Menu(menu=menu,tearoff=False)
        menu.add_cascade(label=labels1,menu=subm)
        subm.add_command(label=labels2,command=menu_command)
    
    def confo(self):
        self.conf = tk.Toplevel(self.master)
        self.app = configuration(self.conf)


class configuration():
    def __init__(self,master):
        
        self.master=master
        self.master.title('Configuration settings')
        self.master.geometry('450x570')
        self.weight_value = entry(text='Select weight:',x1 = 5,y1 = 90,x2 = 240,y2 = 90,default_value = "yolov3-tiny.weights", options = ["yolov3-tiny.weights", "yolov3.weights"],entry_command=callback)
        self.con_value = entry(text='Select configuration file:',x1 = 5,y1 = 120,x2 = 240,y2 = 120,default_value = "yolov3-tiny.cfg", options = ["yolov3-tiny.cfg", "yolov3.cfg"],entry_command=callback)
        self.threshold_value = entry(text='Select threshold:',x1 = 5,y1 = 150,x2 = 240,y2 = 150,default_value = 0.5, options = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],entry_command=callback)
        self.gpu_value = entry(text='Select GPU:',x1 = 5,y1 = 180,x2 = 240,y2 = 180,default_value = False, options = [False,True],entry_command=callback)
        self.dist_value = entry(text='Select Distance:',x1 = 5,y1 = 210,x2 = 240,y2 = 210,default_value = 0.5, options = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],entry_command=callback)
        self.config_value = entry(text='Select Configuration:',x1 = 5,y1 = 240,x2 = 240,y2 = 240,default_value = 0.3, options = ["yolov3-tiny.weights", "yolov3.weights"],entry_command=callback)
        self.save_button(save_text='save',x1=240,y1=450)


    def button_click(self,con,threshold,gpu,dist,weight,config):
        self.master.update()
        tk.file = open("config.py","w")
        tk.file.writelines("MIN_CONF = "+ str(con)+"\n")
        tk.file.writelines("NMS_THRESH = "+ str(threshold)+"\n")
        tk.file.writelines("USE_GPU = "+ str(gpu)+"\n")
        tk.file.writelines("MIN_DISTANCE = "+ str(dist)+"\n")
        tk.file.writelines('WEIGHT_PATH = '+ '"'+str(weight)+'"'+"\n")
        tk.file.writelines("CONFIG_PATH = "+'"'+ str(config)+'"')
        tk.file.close()
        self.master.update()
        self.master.destroy()

    def save_button(self,save_text,x1,y1):
        button = tk.Button(self.master, text=save_text, command=button_click(con=con_value,threshold=threshold_value,gpu=gpu_value,dist=dist_value,config=config_value))
        button.pack()
        button.place(x=x1,y=y1)


    def callback(self,selection):
        return selection
        #print(selection)


    def entry(self,text,x1,y1,x2,y2,default_value,options,entry_command):
        label = tk.Label(self.master, text = text)
        label.pack()
        label.place(x=x1,y=y2)

        value = tk.StringVar(self.master)
        value.set(default_value) # default value

        w = tk.OptionMenu(self.master, value,options,command=entry_command(value))
        w.pack()
        w.place(x=x2,y=y2)





