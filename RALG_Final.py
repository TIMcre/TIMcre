from tkinter import *
import random

al = []
ch = ["Bloodhound", "Gibraltar", "Lifeline", "Pathfinder", "Wraith", "Bangalore", "Caustic", "Mirage",
    "Octane", "Wattson", "Crypto", "Revenant", "Loba", "Rampart", "Horizon", "Fuse", "Valkyrie", "Seer", "Ash"]

def character_gen(al,ch,t,f,h):
    for i in al:
        i.destroy()
    chs = random.sample(ch, t)
    for i in chs:
        label = Label(win,text=i,font=("device", f))        
        label.pack(pady=h)
        al.append(label)        

win=Tk()
win.title(string="RALG")
win.geometry("250x330")

but1 = Button(win, text="Generate 3", font=("device", 25), command= lambda: character_gen(al,ch, 3,30,3))
but2 = Button(win, text="Generate 1", font=("device", 25), command= lambda: character_gen(al,ch, 1,35,30))

but1.pack(pady=3)
but2.pack(pady=3)

win.mainloop()