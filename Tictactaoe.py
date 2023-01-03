from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("TIC TAE TOE")
root.minsize(340,450)

def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global click,count
    b1=Button(text="",width=15,height=10,command=lambda:b_click(b1))
    b1.grid(row=0,column=0)
    b2=Button(text="",width=15,height=10,command=lambda:b_click(b2))
    b2.grid(row=0,column=1)
    b4=Button(text="",width=15,height=10,command=lambda:b_click(b4))
    b4.grid(row=1,column=0)
    b5=Button(text="",width=15,height=10,command=lambda:b_click(b5))
    b5.grid(row=1,column=1)
    b3=Button(text="",width=15,height=10,command=lambda:b_click(b3))
    b3.grid(row=0,column=2)
    b6=Button(text="",width=15,height=10,command=lambda:b_click(b6))
    b6.grid(row=1,column=2)
    b7=Button(text="",width=15,height=10,command=lambda:b_click(b7))
    b7.grid(row=2,column=0)
    b8=Button(text="",width=15,height=10,command=lambda:b_click(b8))
    b8.grid(row=2,column=1)
    b9=Button(text="",width=15,height=10,command=lambda:b_click(b9))
    b9.grid(row=2,column=2)
    
click=True
count=0
def chkwinner():
    global winner,count,click
    winner=False
    if(b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0"):
        b1["bg"]="pink"
        b2["bg"]="pink"
        b3["bg"]="pink"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 1 is winner")
        disable()


    elif(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X"):
        b1["bg"]="cyan"
        b2["bg"]="cyan"
        b3["bg"]="cyan"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 2 is winner")
        disable()
    elif(b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0"):
        b4["bg"]="pink"
        b5["bg"]="pink"
        b6["bg"]="pink"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 1 is winner")
        disable()
    elif(b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X"):
        b4["bg"]="cyan"
        b5["bg"]="cyan"
        b6["bg"]="cyan"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 2 is winner")
        disable()
    elif(b7["text"]=="0" and b8["text"]=="0" and b9["text"]=="0"):
        b7["bg"]="pink"
        b8["bg"]="pink"
        b9["bg"]="pink"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 1 is winner")
        disable()
    elif(b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X"):
        b7["bg"]="cyan"
        b8["bg"]="cyan"
        b9["bg"]="cyan"
        messagebox.showinfo("Winner","Congratulation player 2 is winner")
        disable()
    elif(b1["text"]=="0" and b4["text"]=="0" and b7["text"]=="0"):
        b1["bg"]="pink"
        b4["bg"]="pink"
        b7["bg"]="pink"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 1 is winner")
        disable()
    elif(b2["text"]=="0" and b5["text"]=="0" and b8["text"]=="0"):
        b2["bg"]="pink"
        b5["bg"]="pink"
        b8["bg"]="pink"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 1 is winner")
        disable()
    elif(b3["text"]=="0" and b6["text"]=="0" and b9["text"]=="0"):
        b3["bg"]="pink"
        b6["bg"]="pink"
        b9["bg"]="pink"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 1 is winner")
        disable()
    elif(b1["text"]=="0" and b5["text"]=="0" and b9["text"]=="0"):
        b1["bg"]="pink"
        b4["bg"]="pink"
        b7["bg"]="pink"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 1 is winner")
        disable()
    elif(b3["text"]=="0" and b5["text"]=="0" and b7["text"]=="0"):
        b1["bg"]="pink"
        b4["bg"]="pink"
        b7["bg"]="pink"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 1 is winner")
        disable()

    elif(b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X"):
        b1["bg"]="cyan"
        b4["bg"]="cyan"
        b7["bg"]="cyan"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 2 is winner")
        disable()
    elif(b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X"):
        b2["bg"]="cyan"
        b5["bg"]="cyan"
        b8["bg"]="cyan"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 2 is winner")
        disable()
    elif(b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
        b3["bg"]="cyan"
        b6["bg"]="cyan"
        b9["bg"]="cyan"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 2 is winner")
        disable()
    elif(b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X"):
        b1["bg"]="cyan"
        b4["bg"]="cyan"
        b7["bg"]="cyan"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 2 is winner")
        disable()
    elif(b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        b1["bg"]="cyan"
        b4["bg"]="cyan"
        b7["bg"]="cyan"
        winner=True
        messagebox.showinfo("Winner","Congratulation player 2 is winner")
        disable()
    if(count==9 and winner==False):
        messagebox.showinfo("Tie","its a tie!!!")
        disable()
    
def b_click(b):
    global click
    global count
    if b["text"]=="" and click==True:
            b["text"]="0"
            count+=1
            click=False
            chkwinner()
    elif b["text"]=="" and click==False:
            b["text"]="X"
            click=True
            count+=1
            chkwinner()
    else:
        messagebox.showinfo("tic Tae Toe","Already selected")
   

    
my_menu=Menu(root)
root.config(menu=my_menu)
file_name=Menu(my_menu)
my_menu.add_cascade(label="options",menu=file_name)
file_name.add_command(label="Reset",command=reset)

reset()
root.mainloop()