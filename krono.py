# coding: utf-8
from tkinter import *
from threading import Thread
from tkinter.messagebox import showinfo
import time,tkinter.messagebox
import pygame

class Timer(Thread):
    over=False
    pause=False
    def __init__(self,func):
        Thread.__init__(self)
        self.func=func
        #self.setDaemon(True)
    def run(self):
        global t,root
        time.sleep(1)
        finish=False
        while not self.over and not finish:
            if not self.pause:
                finish=self.func()
            time.sleep(1)
        if finish:
            #root.focus_force()
            root.event_generate('<<pop>>',when='tail')
        t=None
    def kill(self): self.over=True
    def paus(self): self.pause=True
    def cont(self): self.pause=False

t=None
sec=None
root=Tk()
root.bind('<<pop>>',lambda event=None: showinfo('Oh!','Time is over!'))
e1=StringVar()
e2=StringVar()

def show():
    global e1,e2,sec
    e1.set('%.2d'%(sec/60))
    e2.set('%.2d'%(sec%60))
def down():
    global sec
    if sec: 
        sec-=1;show()
        return False
    else: return True
def up():
    global sec
    sec+=1;show()
    return False
    
def st():
    global sec,t
    if t:t.cont();return
    sec=0;show()
    t=Timer(up)
    t.start()

def cd():
    global sec,t
    if t:t.cont();return
    sec=0
    try: sec=int(e1.get())*60
    except Exception:pass
    try: sec+=int(e2.get())
    except Exception:pass
    if not sec: return
    show()
    t=Timer(down)
    t.start()

    pass
def pus():
    global t
    t.paus()

def stp():
    global t,sec
    sec=0;show()
    if t: t.kill()
    t=None
def msc():
    pygame.init()
    pygame.mixer.music.load('biromuryetmez.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)

en1 = Entry (root, textvariable = e1 ,width=10 ,justify=RIGHT)
en2 = Entry (root, textvariable = e2 ,width=10)
lb = Label (root, text = ':' )
stbtn = Button(root ,width=10,text= 'start',command =st)
cdbtn = Button(root ,width=10,text= 'countdown',command =cd)
pusbtn = Button(root ,width=10,text= 'pause',command =pus)
stpbtn = Button(root ,width=10,text= 'stop',command =stp)
mscbtn = Button(root ,width=10,text= 'music',command =msc)


en1.grid(row = 0 ,column = 0,)
lb .grid(row = 0 ,column = 1)
en2.grid(row = 0 ,column = 2)
stbtn.grid(row = 1 ,column = 0)
cdbtn.grid(row = 1 ,column = 2)
pusbtn.grid(row = 2 ,column = 0)
stpbtn.grid(row = 2 ,column = 2)
mscbtn.grid(row = 3 ,column = 3)

root.geometry('+500+400')
root.mainloop ()