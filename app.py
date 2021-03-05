from initial import *
from tkinter import *
import time
def process():
    top = Tk()
    top.title("News Reviewer")

    def checkAndDecide():
        L8.config(text="Please wait... Checking Database...")
        # time.sleep(2)
        input_ = text.get("1.0",END)
        answer = thinking(input_)
        L8.config(text=answer)

    photo = PhotoImage(file = 'news1.PNG')
    photo = photo.subsample(2)
    lbl = Label(top,image = photo)
    lbl.image = photo
    lbl.pack()
    #L1
    L1 = Label(top,text="News Reviewer",font = ( "bold" , 32 , ), fg="blue")
    L1.pack()
    
    #L2
    L2 = Label(top,text="Enter the headline to classify news",font = ( "bold" , 15 , ), fg="green")
    L2.pack()

    L6 = Label(top,text="")
    L6.pack(pady=10)

    text = Text(top,width=50, height=3)
    text.pack()

    L7 = Label(top,text="")
    L7.pack(pady=4)

    B1 = Button(top,text="Check", fg="white", bg="green", command=checkAndDecide)
    B1.pack(padx="4",pady="2")

    L8 = Label(top,text="")
    L8.pack(pady=3)

    L5 = Label(top,text="")
    L5.pack(pady=10)

    top.resizable(0,0)
    top.mainloop()

process()