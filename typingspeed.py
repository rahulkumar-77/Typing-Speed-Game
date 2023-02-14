words=['Developer','Mango','television','cat','Grapee','Villion','Hero','against','door']
def labelslider():
    global count,sliderwords # global so that we can modify from anywhere
    text = "Welcome to Typing speed Game"
    if(count >=len(text)):
        count=0
        sliderwords=''
    sliderwords += text[count]
    count +=1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(100,labelslider) #it calls the function in given micro secs

def time():
    global timeleft,score,miss
    if (timeleft>0):
        timeleft-=1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        notification=messagebox.askretrycancel("Notification","To play again click Retry")
        if(notification==True):
            score=0
            timeleft=14
            miss=0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
        else:
            wordEntry.configure(state='disabled')

def startGame(event): #event because to bind we have give an argument
    global score,miss
    if(timeleft==14):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score +=1
        scoreLabelCount.configure(text=score)
    else:
        miss +=1

    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END) #to clear entry when we hit enter


from tkinter import *
from tkinter import  messagebox
import random
root=Tk() #to make screen but for only sec

root.geometry('800x600+300+50') #to fix the position of appearannce
root.configure(bg='powder blue')
root.title('Typing Speed Game')
root.iconbitmap('typingspeed.ico')

################  Variable ########
score=0
timeleft=14
count=0
sliderwords=''
miss=0


################ Label Method ############
fontLabel = Label(root,text ="",font=('airal',25,'italic bold'),bg='powder blue',fg='red',width=40)
fontLabel.place(x=10,y=10)
labelslider()

random.shuffle(words)
wordLabel=Label(root,text=words[0],font=('airal',40,'italic bold'),bg='powder blue')
wordLabel.place(x=300,y=200)

scoreLabel=Label(root,text='Your Score : ',font=('airal',25,'italic bold'),bg='powder blue')
scoreLabel.place(x=10,y=100)

scoreLabelCount=Label(root,text=score,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scoreLabelCount.place(x=80,y=180)


timerLabel=Label(root,text='Time Left :',font=('airal',25,'italic bold'),bg='powder blue')
timerLabel.place(x=600,y=100)

timeLabelCount=Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timeLabelCount.place(x=680,y=180)


gamePlayDetailLabel=Label(root,text="Type Word and Hit Enter Button",font=('airal',20,'italic bold'),bg='powder blue',fg='dark gray')
gamePlayDetailLabel.place(x=220,y=400)


################# Entry Method ##############
wordEntry= Entry(root,font=('airal',25,'italic bold'),bd=15,justify='center')
wordEntry.place(x=220,y=300)
wordEntry.focus_set() # without clicking anywhere on scrren start typing

#########################################
root.bind('<Return>',startGame)
root.mainloop()# it will make screen to stay till we want