from tkinter import *
import random
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

#GUI
#Initialize the window
root = Tk()
#Set width and height
root.geometry('400x400')
#Fix the size of the window
root.resizable(0,0)
#Title of the window
root.title('Rock,Paper,Scissors')
#Set the color of the background
root.config(bg = 'seashell3')

#Label() widget used when we want to display text that users cant modify
Label(root,text='Rock, Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()

#**********************
#User Choice using text
user_take = ""
#Label(root,text='Choose: rock | paper | cissors', font='arial 15 bold',bg = 'seashell2').place(x=20,y=70)
#Entry is used when we want to create an input text field
#Entry(root,font = 'arial 15', textvariable = user_take, bg='antiquewhite2').place (x=90,y=130)

#User choice using buttons
def choice(option):
    global user_take
    user_take=option
    
Label(root,text='Choose', font='arial 15 bold',bg = 'seashell2').place(x=150,y=50)
Button(root, font = 'arial 13 bold', text = 'ROCK'  ,padx =5,bg ='seashell4' ,command = choice('rock')).place(x=50,y=100)
Button(root, font = 'arial 13 bold', text = 'PAPER'  ,padx =5,bg ='seashell4' ,command = choice('paper')).place(x=150,y=100)
Button(root, font = 'arial 13 bold', text = 'SCISSORS'  ,padx =5,bg ='seashell4' ,command = choice('scissors')).place(x=250,y=100)
#***********************
#Computer Choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

#***********************
#Start Game
Result = StringVar()

def play():
    user_pick = user_take
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')


#***********************
#Function to Reset
def Reset():
    Result.set("")
    user_take = ""

#***********************
#Function to Exit
def Exit():
    root.destroy()

#***********************
#Define Buttons
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


root.mainloop()
