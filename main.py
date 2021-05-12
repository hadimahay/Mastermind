
from tkinter import *
from tkinter import messagebox
from random import randint


count =0

def LEVEL1():
    global count
    if count != 0 :
        count = 0

    
    def comparison():
        global count 
        count +=1

        try:
            num_user_l1 = int(num.get())

        except Exception as e:
            messagebox.showerror("error","Error\n\n%s"%e)  
            LEV1.mainloop()  
        
        if num_user_l1 == num_system_l1:
            messagebox.showinfo("information","YOU WIN!!!!!!!!!\n guess : %s"%count )
            LEV1.mainloop()

        elif num_user_l1 > num_system_l1:
            tips.config(text = "my number is smaller than your's")

        elif num_user_l1 < num_system_l1:
            tips.config(text = "my number is bigger than your's") 
        for i in range(4):
            num.delete(0)
  
        
    num_system_l1 = randint(1000,10000)
    
    LEV1 = Tk(className="Level(1)")

    LEV1.geometry('500x500')
   
    
    Label(LEV1 , text = 'PLEASE INTER YOUR NUMBER').pack()

    num = Entry(LEV1,font = ("nazanin",30),bd = 2,  bg = 'old lace',width = 15,justify='center')
    num.pack()

    start = Button(LEV1 ,text = "START" ,command=comparison,font=("nazanin",22),width = 13, height =1 ,padx = 50,activebackground = 'turquoise1' , bg = 'gray99' , bd = 6 )
    start.place(x = 70,y =90)

    EXIT = Button(LEV1 ,text = "EXIT" ,command=quit,font=("nazanin",22),width = 13, height =1,padx = 50 ,activebackground = 'red', bg = 'gray99' , bd = 6 )
    EXIT.place(x = 70,y =150)

    tips = Label(LEV1 , text = "Start the game and I will help",font=("nazanin",18) ,fg = 'black' , bg = 'pink',height =3,padx =70)
    tips.place(x = 5,y =250)

    LEV1.resizable(width = False , height = False)  
    
    LEV1.configure(background = "maroon1")
    LEV1.mainloop()
    
def LEVEL2():
    global count
    if count != 0 :
        count = 0

    
    def comparison():
        global count 
        count +=1

        try:
            num_user_l1 = int(num.get())

        except Exception as e:
            messagebox.showerror("error","Error\n\n%s"%e)  
            LEV2.mainloop()  
        
        if num_user_l1 == num_system_l1:
            messagebox.showinfo("information","YOU WIN!!!!!!!!!\n guess : %s"%count )
            LEV2.mainloop()

        elif num_user_l1 > num_system_l1:
            tips.config(text = "my number is smaller than your's")

        elif num_user_l1 < num_system_l1:
            tips.config(text = "my number is bigger than your's") 
        for i in range(5):
            num.delete(0)
  
        
    num_system_l1 = randint(10000,100000)
    
    LEV2 = Tk(className="Level(2)")

    LEV2.geometry('500x500')
   
    
    Label(LEV2 , text = 'PLEASE INTER YOUR NUMBER').pack()

    num = Entry(LEV2,font = ("nazanin",30),bd = 2,  bg = 'old lace',width = 15,justify='center')
    num.pack()

    start = Button(LEV2 ,text = "START" ,command=comparison,font=("nazanin",22),width = 13, height =1 ,padx = 50,activebackground = 'turquoise1' , bg = 'gray99' , bd = 6 )
    start.place(x = 70,y =90)

    EXIT = Button(LEV2 ,text = "EXIT" ,command=quit,font=("nazanin",22),width = 13, height =1,padx = 50 ,activebackground = 'red', bg = 'gray99' , bd = 6 )
    EXIT.place(x = 70,y =150)

    tips = Label(LEV2 , text = "Start the game and I will help",font=("nazanin",18) ,fg = 'black' , bg = 'pink',height =3,padx =70)
    tips.place(x = 5,y =250)

    LEV2.resizable(width = False , height = False)  
    
    LEV2.configure(background = "maroon2")
    LEV2.mainloop()

def LEVEL3():
    global count
    if count != 0 :
        count = 0

    
    def comparison():
        global count 
        count +=1

        try:
            num_user_l1 = int(num.get())

        except Exception as e:
            messagebox.showerror("error","Error\n\n%s"%e)  
            LEV3.mainloop()  
        
        if num_user_l1 == num_system_l1:
            messagebox.showinfo("information","YOU WIN!!!!!!!!!\n guess : %s"%count )
            LEV3.mainloop()

        elif num_user_l1 > num_system_l1:
            tips.config(text = "my number is smaller than your's")

        elif num_user_l1 < num_system_l1:
            tips.config(text = "my number is bigger than your's") 
        for i in range(6):
            num.delete(0)
  
        
    num_system_l1 = randint(100000,1000000)
    
    LEV3 = Tk(className="Level(3)")

    LEV3.geometry('500x500')
   
    
    Label(LEV3 , text = 'PLEASE INTER YOUR NUMBER').pack()

    num = Entry(LEV3,font = ("nazanin",30),bd = 2, bg = 'old lace',width = 15,justify='center')
    num.pack()

    start = Button(LEV3 ,text = "START" ,command=comparison,font=("nazanin",22),width = 13, height =1 ,padx = 50,activebackground = 'turquoise1' , bg = 'gray99' , bd = 6 )
    start.place(x = 70,y =90)

    EXIT = Button(LEV3 ,text = "EXIT" ,command=quit,font=("nazanin",22),width = 13, height =1,padx = 50 ,activebackground = 'red', bg = 'gray99' , bd = 6 )
    EXIT.place(x = 70,y =150)

    tips = Label(LEV3 , text = "Start the game and I will help",font=("nazanin",18) ,fg = 'black' , bg = 'pink',height =3,padx =70)
    tips.place(x = 5,y =250)

    LEV3.resizable(width = False , height = False)  
    
    LEV3.configure(background = "maroon3")
    LEV3.mainloop()
    
def LEVEL4():
    global count
    if count != 0 :
        count = 0

    
    def comparison():
        global count 
        count +=1

        try:
            num_user_l1 = int(num.get())

        except Exception as e:
            messagebox.showerror("error","Error\n\n%s"%e)  
            LEV4.mainloop()  
        
        if num_user_l1 == num_system_l1:
            messagebox.showinfo("information","YOU WIN!!!!!!!!!\n guess : %s"%count )
            LEV4.mainloop()

        elif num_user_l1 > num_system_l1:
            tips.config(text = "my number is smaller than your's")

        elif num_user_l1 < num_system_l1:
            tips.config(text = "my number is bigger than your's") 
        for i in range(7):
            num.delete(0)
  
        
    num_system_l1 = randint(1000000,10000000)
    
    LEV4 = Tk(className="Level(4)")

    LEV4.geometry('500x500')
   
    
    Label(LEV4 , text = 'PLEASE INTER YOUR NUMBER').pack()

    num = Entry(LEV4,font = ("nazanin",30),bd = 2, bg = 'old lace',width = 15,justify='center')
    num.pack()

    start = Button(LEV4 ,text = "START" ,command=comparison,font=("nazanin",22),width = 13, height =1 ,padx = 50,activebackground = 'turquoise1' , bg = 'gray99' , bd = 6 )
    start.place(x = 70,y =90)

    EXIT = Button(LEV4 ,text = "EXIT" ,command=quit,font=("nazanin",22),width = 13, height =1,padx = 50 ,activebackground = 'red', bg = 'gray99' , bd = 6 )
    EXIT.place(x = 70,y =150)

    tips = Label(LEV4 , text = "Start the game and I will help",font=("nazanin",18) ,fg = 'black' , bg = 'pink',height =3,padx =70)
    tips.place(x = 5,y =250)

    LEV4.resizable(width = False , height = False)  
    
    LEV4.configure(background = "maroon4")
    LEV4.mainloop()
    
def LEVEL5():
    global count
    if count != 0 :
        count = 0

    
    def comparison():
        global count 
        count +=1

        try:
            num_user_l1 = int(num.get())

        except Exception as e:
            messagebox.showerror("error","Error\n\n%s"%e)  
            LEV5.mainloop()  
        
        if num_user_l1 == num_system_l1:
            messagebox.showinfo("information","YOU WIN!!!!!!!!!\n guess : %s"%count )
            LEV5.mainloop()

        elif num_user_l1 > num_system_l1:
            tips.config(text = "my number is smaller than your's")

        elif num_user_l1 < num_system_l1:
            tips.config(text = "my number is bigger than your's") 
        for i in range(8):
            num.delete(0)
  
        
    num_system_l1 = randint(10000000,100000000)
    
    LEV5 = Tk(className="Level(5)")

    LEV5.geometry('500x500')
   
    
    Label(LEV5 , text = 'PLEASE INTER YOUR NUMBER').pack()

    num = Entry(LEV5,font = ("nazanin",30),bd = 2, bg = 'old lace',width = 15,justify='center')
    num.pack()

    start = Button(LEV5 ,text = "START" ,command=comparison,font=("nazanin",22),width = 13, height =1 ,padx = 50,activebackground = 'turquoise1' , bg = 'gray99' , bd = 6 )
    start.place(x = 70,y =90)

    EXIT = Button(LEV5 ,text = "EXIT" ,command=quit,font=("nazanin",22),width = 13, height =1,padx = 50 ,activebackground = 'red', bg = 'gray99' , bd = 6 )
    EXIT.place(x = 70,y =150)

    tips = Label(LEV5 , text = "Start the game and I will help",font=("nazanin",18) ,fg = 'black' , bg = 'pink',height =3,padx =70)
    tips.place(x = 5,y =250)

    LEV5.resizable(width = False , height = False)  
    
    LEV5.configure(background = "magenta4")
    LEV5.mainloop()
    
 
#region MENO
win = Tk(className="Mastermind")

win.configure(background="greenyellow")

win.geometry('500x500')

Label(win , text = "Mastermind games ",font=("nazanin",22) ,fg = 'black' , bg = 'magenta3',padx =600).pack()

Label(win , text = "Welcom, please enter your Level ",font=("nazanin",30) ,fg = 'black' , bg = 'gold2',).pack()

level_1 = Button(win ,text = "LEVEL 1" ,command=LEVEL1,font=("nazanin",22),width = 13, height =1 ,padx = 50 , bd = 6 ,activebackground = 'turquoise1' , bg = 'gray99')
level_1.pack()

level_2 = Button(win ,text = "LEVEL 2" ,command=LEVEL2,font=("nazanin",22),width = 13, height =1,padx = 50, bd = 6 ,activebackground = 'turquoise1', bg = 'gray99')
level_2.pack()

level_3 = Button(win ,text = "LEVEL 3" ,command=LEVEL3,font=("nazanin",22),width = 13, height =1,padx = 50 ,bd = 6 ,activebackground = 'turquoise1', bg = 'gray99')
level_3.pack()

level_4 = Button(win ,text = "LEVEL 4" ,command=LEVEL4,font=("nazanin",22),width = 13, height =1,padx = 50 ,bd = 6 ,activebackground = 'turquoise1', bg = 'gray99')
level_4.pack()

level_5 = Button(win ,text = "LEVEL 5" ,command=LEVEL5,font=("nazanin",22),width = 13, height =1,padx = 50 ,bd = 6 ,activebackground = 'turquoise1', bg = 'gray99')
level_5.pack()

EXIT = Button(win ,text = "EXIT" ,command=quit,font=("nazanin",22),width = 13, height =1,padx = 50 ,bd = 6 ,activebackground = 'red', bg = 'gray99')
EXIT.pack()

win.mainloop()

#endregion