from tkinter import *
from PIL import Image,ImageTk
from random import randint

 
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="#9b59b6")


#picture
rock_img =ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img =ImageTk.PhotoImage(Image.open("paper-user.png"))
scissors_img =ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp =ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp =ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_comp =ImageTk.PhotoImage(Image.open("scissors.png"))

#insert picture
user_label = Label(root,image=scissors_img,bg="#9b59b6")
comp_label = Label(root,image=scissors_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators
user_indicator=Label(root,font=50,text="User",bg="#9b59b6",fg="white")
comp_indicator=Label(root,font=50,text="Computer",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#message
msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

#update msg
def updatemessage(x):
    msg['text']=x

#update score
def updateUserScore():
    score=int(playerscore["text"])
    score+=1
    playerscore["text"]=str(score)
def updateCompScore():
    score=int(computerscore["text"])
    score+=1
    computerscore["text"]=str(score)

#check winner
def checkWin(player,computer):
    if player==computer:
        updatemessage("Its a tie!")
    elif player=="rock":
        if computer=="paper":
            updatemessage("You Loose")
            updateCompScore()
        else:
            updatemessage("You Win")
            updateUserScore
    elif player=="paper":
        if computer=="scissors":
            updatemessage("You Loose")
            updateCompScore()
        else:
            updatemessage("You Win")
            updateUserScore()
    elif player=="scissors":
        if computer=="rock":
            updatemessage("You loose")
            updateCompScore()
        else:
            updatemessage("You Win")
            updateUserScore()
    else:
        pass
    
#update choices

choices=["rock","paper","scissors"]
def updateChoice(x):
#for comp
    compChoice=choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)
#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)
        
    checkWin(x,compChoice)

#buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissors=Button(root,width=20,height=2,text="SCISSORS",bg="#0ABDE3",fg="white",command=lambda:updateChoice("scissors")).grid(row=2,column=3)


root.mainloop()