from tkinter import * 
import tkinter.messagebox 

class calci_1:
    def __init__(self):
        calci.geometry("350x350")
        title=Label(calci, text="calculator",pady=2)
        title.pack()
        frame=Frame(calci, bg="indigo")
        frame.pack()
        entry=Entry(frame,text="enter")
        entry.grid(row=0,column=0,columnspan=50,padx=5,pady=5,ipadx=10,ipady=10)

        def myclick(number):
            entry.insert(END, number)
 
 
        def equal(enter):
            try:
                y = str(eval(entry.get()))
                entry.delete(0,END)
                entry.insert(0, y)
            except:
                tkinter.messagebox.showinfo("calculator is not exist")
 
 
        def clear():
            entry.delete(0,END)



        button_b = Button(frame, text = '(', padx=2,pady=3,command=lambda:myclick("("),width=3)
        button_b.grid(row=1,column=0, padx=2,pady=3)
        button_b1= Button(frame, text = ')', padx=2,pady=3,command=lambda:myclick(")"),width=3)
        button_b1.grid(row=1,column=1, padx=2,pady=2)
        button_b2= Button(frame, text = '%', padx=2,pady=3,command=lambda:myclick("%"),width=3)
        button_b2.grid(row=1,column=2, padx=2,pady=2)
        button_b3= Button(frame, text = '/', padx=2,pady=3,command=lambda:myclick("/"),width=3)
        button_b3.grid(row=1,column=3, padx=2,pady=2)
        


        button_7 = Button(frame, text = '7', padx=2,pady=3,command=lambda:myclick(7),width=3)
        button_7.grid(row=2,column=0, padx=2,pady=2)
        button_8= Button(frame, text = '8', padx=2,pady=3,command=lambda:myclick(8),width=3)
        button_8.grid(row=2,column=1, padx=2,pady=2)
        button_9= Button(frame, text = '9', padx=2,pady=3,command=lambda:myclick(9),width=3)
        button_9.grid(row=2,column=2, padx=2,pady=2)
        button_M= Button(frame, text = '*', padx=2,pady=3,command=lambda:myclick("*"),width=3)
        button_M.grid(row=2,column=3, padx=2,pady=2)
        
        
        
        button_4 = Button(frame, text = '4', padx=2,pady=3,command=lambda:myclick(4),width=3)
        button_4.grid(row=3,column=0, padx=2,pady=2)
        button_5= Button(frame, text = '5', padx=2,pady=3,command=lambda:myclick(5),width=3)
        button_5.grid(row=3,column=1, padx=2,pady=2)
        button_6= Button(frame, text = '6', padx=2,pady=3,command=lambda:myclick(6),width=3)
        button_6.grid(row=3,column=2, padx=2,pady=2)
        button_Mi= Button(frame, text = '-', padx=2,pady=3,command=lambda:myclick("-"),width=3)
        button_Mi.grid(row=3,column=3, padx=2,pady=2)
        
        
        
        button_1 = Button(frame, text = '1', padx=2,pady=3,command=lambda:myclick(1),width=3)
        button_1.grid(row=4,column=0, padx=2,pady=2)
        button_2= Button(frame, text = '2', padx=2,pady=3,command=lambda:myclick(2),width=3)
        button_2.grid(row=4,column=1, padx=2,pady=2)
        button_3= Button(frame, text = '3', padx=2,pady=3,command=lambda:myclick(3),width=3)
        button_3.grid(row=4,column=2, padx=2,pady=2)
        button_P= Button(frame, text = '+', padx=2,pady=3,command=lambda:myclick("+"),width=3)
        button_P.grid(row=4,column=3, padx=2,pady=2)


        button_Z = Button(frame, text = '0', padx=2,pady=3,command=lambda:myclick(0),width=3)
        button_Z.grid(row=5,column=0, padx=2,pady=2)
        button_d= Button(frame, text = '.', padx=2,pady=3,command=lambda:myclick("."),width=3)
        button_d.grid(row=5,column=1, padx=2,pady=2)
        button_e= Button(frame, text = '=', padx=2,pady=3,command=lambda:equal("enter"),width=3)
        button_e.grid(row=5,column=2, padx=2,pady=2)
        button_c= Button(frame, text = 'CE',command=clear)
        button_c.grid(row=5,column=3, ipadx=3,ipady=3)

calci=Tk()
obj=calci_1()
calci.mainloop()