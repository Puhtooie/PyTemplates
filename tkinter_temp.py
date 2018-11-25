from tkinter import *
from tkinter import ttk

def select_ind(event):

    top = Tk()
        #Spinboxes for each of the variables
        #find out which ones take multiple variables
    set_test_btn= Button(top_3, text='Set Indicators')
    set_test_btn.bind('<Button-1>', graph_test)#see matplotlib_temp

    parameter_1_lab=Label(top, text= 'Commodity Channel Index')
    parameter_2_lab=Label(top, text= 'Money flow Index')
    parameter_3_lab=Label(top, text= 'StochRSI')
    parameter_4_lab=Label(top, text= 'RSI')

    parameter_1_c = IntVar()
    parameter_2_c = IntVar()
    parameter_3_c = IntVar()
    parameter_4_c = IntVar()

    parameter_1 = Checkbutton(top, text = "Use parameter_1", variable = parameter_1_c, \
                         onvalue = 1, offvalue = 0, height=5, \
                         width = 20)
    parameter_2 = Checkbutton(top, text = "Use parameter_2", variable = parameter_2_c, \
                         onvalue = 1, offvalue = 0, height=5, \
                         width = 20)
    parameter_3 = Checkbutton(top, text = "Use parameter_3", variable = parameter_3_c, \
                         onvalue = 1, offvalue = 0, height=5, \
                         width = 20)
    parameter_4 = Checkbutton(top, text = "Use parameter_4", variable = parameter_4_c, \
                         onvalue = 1, offvalue = 0, height=5, \
                         width = 20)

    parameter_1= Spinbox(top, from_=-150,to=300)
    parameter_2= Spinbox(top, from_=0,to=100)
    parameter_3= Spinbox(top, from_=0,to=1)
    parameter_4= Spinbox(top, from_=0,to=100)

    parameter_1_lab.grid(row=0 , column=0)
    parameter_2_lab.grid(row=0 ,column=2)
    parameter_3_lab.grid(row=0 ,column=4)
    parameter_4_lab.grid(row=2 ,column=0)

    parameter_1_Check.grid(row=1 , column=1)
    parameter_2_Check.grid(row=1 ,column=3)
    parameter_3_Check.grid(row=1 ,column=5)
    parameter_4_Check.grid(row=3 ,column=1)

    parameter_1.grid(row=1 ,column=0)
    parameter_2.grid(row=1 ,column=2)
    parameter_3.grid(row=1 ,column=4)
    parameter_4.grid(row=3 ,column=0)

    set_test_btn.grid(row=4 ,column=0)
    top.mainloop()

