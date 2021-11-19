from tkinter import * 
import tkinter.messagebox 
import random


al = []
ch = ["Bloodhound", "Gibraltar", "Lifeline", "Pathfinder", "Wraith", "Bangalore", "Caustic", "Mirage",
    "Octane", "Wattson", "Crypto", "Revenant", "Loba", "Rampart", "Horizon", "Fuse", "Valkyrie", "Seer", "Ash"]

def character_gen(ch,t):
    chs = random.sample(ch, t)
    for i in chs:
        label = Label(win,text=i,font=("device", 30))        
        label.pack()
        al.append(label)
    quit_check()
    for i in al:
        i.destroy()

def quit_check():
    result = tkinter.messagebox.askquestion('RALG','Do you want to Quit?')
    if result == 'yes':
        win.destroy()
        quit()

win=Tk()

while True:
    result = tkinter.messagebox.askquestion('RALG','Do you want to generate 3 Random Legends?')
    if result == 'yes':
        character_gen(ch, 3)   
              
    else:
        result = tkinter.messagebox.askquestion('RALG','Do you want to generate 1 Random Legend?')
        if result == 'yes':
            character_gen(ch, 1)           
            
        else:
            win.destroy()
            
win.mainloop()