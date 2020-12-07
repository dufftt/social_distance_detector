import tkinter as tk 
from tkinter import ttk 
  
# Creating tkinter window 
window = tk.Tk() 
window.geometry('500x570') 
# Label 




def configuration():

        ttk.Label(window, text = "USE GPU :",  
                font = ("Times New Roman", 10)).grid(column = 0,  
                row = 15, padx = 10, pady = 25) 
  
        n = tk.StringVar() 
        USE_GPU = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
# Adding combobox drop down list 
        USE_GPU['values'] = (True,  
                          False) 
  
        USE_GPU.grid(column = 1, row = 15) 
        USE_GPU.current()






#MINIMUM DISTANCE

        ttk.Label(window, text = "MIN DISTANCE :",  
                font = ("Times New Roman", 10)).grid(column = 0,  
                row = 16, padx = 10, pady = 25) 
  
        n = tk.IntVar() 
        min_dist = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
# Adding combobox drop down list 
        min_dist['values'] = (10,  
                          20, 
                          30, 
                          40, 
                          50, 
                          60,  
                          70,  
                          80,  
                          90,  
                          100) 
  
        min_dist.grid(column = 1, row = 16) 
        min_dist.current()







#MINIMUM CONF

        ttk.Label(window, text = "Min Conf :",  
                font = ("Times New Roman", 10)).grid(column = 0,  
                row = 17, padx = 10, pady = 25) 
  
        n = tk.DoubleVar() 
        min_conf = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
# Adding combobox drop down list 
        min_conf['values'] = (0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0) 
  
        min_conf.grid(column = 1, row = 17) 
        min_conf.current()







#THRESHOLD


        ttk.Label(window, text = "Min Threshold :",  
                font = ("Times New Roman", 10)).grid(column = 0,  
                row = 18, padx = 10, pady = 25) 
  
        n = tk.DoubleVar() 
        min_thresh = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
# Adding combobox drop down list 
        min_thresh['values'] = (0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0) 
  
        min_thresh.grid(column = 1, row = 18) 
        min_thresh.current()  










#WEIGHT
        ttk.Label(window, text = "Weight File Name :",  
                font = ("Times New Roman", 10)).grid(column = 0,  
                row = 19, padx = 10, pady = 25) 
  
        n = tk.StringVar() 
        weight_path = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
# Adding combobox drop down list 
        weight_path['values'] = ('yolov3-tiny.weights') 
  
        weight_path.grid(column = 1, row = 19)
        weight_path.current()





        ttk.Label(window, text = "Config File Name :",  
                font = ("Times New Roman", 10)).grid(column = 0,  
                row = 20, padx = 10, pady = 25) 
  
        n = tk.StringVar() 
        config_path = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
# Adding combobox drop down list 
        config_path['values'] = ('yolov3-tiny.config') 
  
        config_path.grid(column = 1, row = 20)
        config_path.current()

        L=[]

        L = [USE_GPU.get(),min_conf.get(),
        min_dist.get(),min_thresh.get(),
        weight_path.get(),config_path.get()]
        return L



def upd():
        #window.update()
        print(x)

x = configuration()
   
# Shows february as a default value 
btn = ttk.Button(window, text="Get Value",command=upd())
btn.place(relx="0.5",rely="0.8")




window.mainloop() 
