import pygame, sys, pygame.mixer
import time
from pygame.locals import *
from Tkinter import *
pygame.init()
screen = pygame.display.set_mode((1300,715))
pygame.display.set_caption('Tic Tac Toe')
bg = pygame.image.load('/home/surya/Downloads/rsz_suc.jpg')
bd = pygame.image.load('/home/surya/Downloads/rsz_p.jpg')

endim = pygame.image.load('/home/surya/Downloads/rsz_tttcong.png')
pygame.mixer.music.load('/home/surya/Downloads/[No Copyright Music] Flying High - FREDJI.mp3')
pygame.mixer.music.play(-1)
bri_blue = (0,0,255)
bri_g = (0,255,0)
g = (0,150,0)
r = (150,0,0)
bri_r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
blue = (0,0,150)

def message_to_screen(text, colour, x, y, fsize):
  font_obj = pygame.font.SysFont(None, fsize)
  msg = font_obj.render(text, True, colour)
  screen.blit(msg, [x, y])
  
def intro():
  done=False
  while not done:
    screen.blit(bg,(0,0))
    screen.fill(g,[550,141.25,200,50])
    screen.fill(r,[550,332.50,200,50])
    screen.fill(blue,[550,523.75,200,50])
    message_to_screen('Play Game', w, 575, 146.25,45)
    message_to_screen('Quit', w, 620, 337.50, 45)
    message_to_screen('Instructions', w, 560, 528.75, 45)
    
    mousepos = pygame.mouse.get_pos()
    if 550<mousepos[0]<750 and 141.25<mousepos[1]<191.25:
      screen.fill(bri_g,[550,141.25,200,50])
      message_to_screen('Play Game', w, 575, 146.25,45)
    if 550<mousepos[0]<750 and 332.50<mousepos[1]<382.50:
      screen.fill(bri_r,[550,332.50,200,50])
      message_to_screen('Quit', w, 620, 337.50, 45)
    if 550<mousepos[0]<750 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_blue,[550,523.75,200,50])
      message_to_screen('Instructions', w, 560, 528.75, 45)

    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        done=True
      if event.type==pygame.MOUSEBUTTONDOWN:
        if 550<mousepos[0]<750 and 332.50<mousepos[1]<382.50 and event.button ==1:
          done=True 
        if 550<mousepos[0]<750 and 141.25<mousepos[1]<191.25 and event.button ==1:
          select()
        if 550<mousepos[0]<750 and 523.75<mousepos[1]<573.75 and event.button == 1:
          instr()
    pygame.display.update()
  pygame.quit()
  quit()
        
t=1
def gameloop10():
  window=Tk()
  window.title("TIC-TIC-TOE")
  window.geometry("1300x715+0+0")
  r=Label(window,text="Start by clicking any button ->>",font=('Helvetica','20'))
  r.grid(row=1,column=0) 
  l=Label(window,text="TIC-TAC-TAC",font=('Helvetica','50'))
  l.grid(row=0,column=0)
  def clic1():
    global t
    if bt1["text"]==" ":
      if t==1:
        t=2
        bt1["text"]="1"
      elif t==2:
        t=1
        bt1["text"]="0"
      ch()
  def clic1():
    global t
    if bt1["text"]==" ":
      if t==1:
        t=2
        bt1["text"]="1"
      elif t==2:
        t=1
        bt1["text"]="0"
      ch()
  def clic2():
    global t
    if bt2["text"]==" ":
      if t==1:
        t=2
        bt2["text"]="1"
      elif t==2:
        t=1
        bt2["text"]="0"
      ch()
  def clic3():
    global t
    if bt3["text"]==" ":
      if t==1:
        t=2
        bt3["text"]="1"
      elif t==2:
        t=1
        bt3["text"]="0"
      ch()
  def clic4():
    global t
    if bt4["text"]==" ":
      if t==1:
        t=2
        bt4["text"]="1"
      elif t==2:
        t=1;
        bt4["text"]="0"
      ch()
  def clic5():
    global t
    if bt5["text"]==" ":
      if t==1:
        t=2
        bt5["text"]="1"
      elif t==2:
        t=1
        bt5["text"]="0"
      ch()
  def clic6():
    global t
    if bt6["text"]==" ":
      if t==1:
        t=2
        bt6["text"]="1"
      elif t==2:
        t=1
        bt6["text"]="0"
      ch()
  def clic7():
    global t
    if bt7["text"]==" ":
      if t==1:
        t=2
        bt7["text"]="1"
      elif t==2:
        t=1
        bt7["text"]="0"
      ch()
  def clic8():
    global t
    if bt8["text"]==" ":
      if t==1:
        t=2
        bt8["text"]="1"
      elif t==2:
        t=1
        bt8["text"]="0"
      ch()
  def clic9():
    global t
    if bt9["text"]==" ":
      if t==1:
        t=2
        bt9["text"]="1"
      elif t==2:
        t=1
        bt9["text"]="0"
      ch()
  def clic10():
    global t
    if bt10["text"]==" ":
      if t==1:
        t=2
        bt10["text"]="1"
      elif t==2:
        t=1
        bt10["text"]="0"
      ch()
  def clic11():
    global t
    if bt11["text"]==" ":
      if t==1:
        t=2
        bt11["text"]="1"
      elif t==2:
        t=1
        bt11["text"]="0"
      ch()
  def clic12():
    global t
    if bt12["text"]==" ":
      if t==1:
        t=2;
        bt12["text"]="1"
      elif t==2:
        t=1;
        bt12["text"]="0"
      ch()
  def clic13():
    global t
    if bt13["text"]==" ":
      if t==1:
        t=2;
        bt13["text"]="1"
      elif t==2:
        t=1;
        bt13["text"]="0"
      ch()
  def clic14():
    global t
    if bt14["text"]==" ":
      if t==1:
        t=2;
        bt14["text"]="1"
      elif t==2:
        t=1;
        bt14["text"]="0"
      ch()
  def clic15():
    global t
    if bt15["text"]==" ":
      if t==1:
        t=2;
        bt15["text"]="1"
      elif t==2:
        t=1;
        bt15["text"]="0"
      ch()
  def clic16():
    global t
    if bt16["text"]==" ":
      if t==1:
        t=2;
        bt16["text"]="1"
      elif t==2:
        t=1;
        bt16["text"]="0"
      ch()
  def clic17():
    global t
    if bt17["text"]==" ":
      if t==1:
        t=2;
        bt17["text"]="1"
      elif t==2:
        t=1;
        bt17["text"]="0"
      ch()
  def clic18():
    global t
    if bt18["text"]==" ":
      if t==1:
        t=2;
        bt18["text"]="1"
      elif t==2:
        t=1;
        bt18["text"]="0"
      ch()
  def clic19():
    global t
    if bt19["text"]==" ":
      if t==1:
        t=2;
        bt19["text"]="1"
      elif t==2:
        t=1;
        bt19["text"]="0"
      ch()
  def clic20():
    global t
    if bt20["text"]==" ":
      if t==1:
        t=2;
        bt20["text"]="1"
      elif t==2:
        t=1;
        bt20["text"]="0"
      ch()
  def clic21():
    global t
    if bt21["text"]==" ":
      if t==1:
        t=2;
        bt21["text"]="1"
      elif t==2:
        t=1;
        bt21["text"]="0"
      ch()
  def clic22():
    global t
    if bt22["text"]==" ":
      if t==1:
        t=2;
        bt22["text"]="1"
      elif t==2:
        t=1;
        bt22["text"]="0"
      ch()
  def clic23():
    global t
    if bt23["text"]==" ":
      if t==1:
        t=2;
        bt23["text"]="1"
      elif t==2:
        t=1;
        bt23["text"]="0"
      ch()
  def clic24():
    global t
    if bt24["text"]==" ":
      if t==1:
        t=2;
        bt24["text"]="1"
      elif t==2:
        t=1;
        bt24["text"]="0"
      ch()
  def clic25():
    global t
    if bt25["text"]==" ":
      if t==1:
        t=2;
        bt25["text"]="1"
      elif t==2:
        t=1;
        bt25["text"]="0"
      ch()
  def ch():
    b1=bt1["text"]
    b2=bt2["text"]
    b3=bt3["text"]
    b4=bt4["text"]
    b5=bt5["text"]
    b6=bt6["text"]
    b7=bt7["text"]
    b8=bt8["text"]
    b9=bt9["text"]
    b10=bt10["text"]
    b11=bt11["text"]
    b12=bt12["text"]
    b13=bt13["text"]
    b14=bt14["text"]
    b15=bt15["text"]
    b16=bt16["text"]
    b17=bt17["text"]
    b18=bt18["text"]
    b19=bt19["text"]
    b20=bt20["text"]
    b21=bt21["text"]
    b22=bt22["text"]
    b23=bt23["text"]
    b24=bt24["text"]
    b25=bt25["text"]
    
    if(b1==b2==b3==b4==b5=="1"):
      window.destroy()
      victory1()
    elif (b1==b2==b3==b4==b5=="0"):
      window.destroy()
      victory0()
    elif(b6==b7==b8==b9==b10=="1"):
      window.destroy()
      victory1()
    elif (b6==b7==b8==b9==b10=="0"):
      window.destroy()
      victory0()
    elif(b11==b12==b13==b14==b15=="1"):
      window.destroy()
      victory1()
    elif (b11==b12==b13==b14==b15=="0"):
      window.destroy()
      victory0()
    elif(b16==b17==b18==b19==b20=="1"):
      window.destroy()
      victory1()
    elif (b16==b17==b18==b19==b20=="0"):
      window.destroy()
      victory0()
    elif(b21==b22==b23==b24==b25=="1"):
      window.destroy()
      victory1()
    elif (b21==b22==b23==b24==b25=="0"):
      window.destroy()
      victory0()
    elif(b1==b6==b11==b16==b21=="1"):
      window.destroy()
      victory1()
    elif (b1==b6==b11==b16==b21=="0"):
      window.destroy()
      victory0()
    elif(b2==b7==b12==b17==b22=="1"):
      window.destroy()
      victory1()
    elif (b2==b7==b12==b17==b22=="0"):
      window.destroy()
      victory0()
    elif(b3==b8==b13==b18==b23=="1"):
      window.destroy()
      victory1()
    elif (b3==b8==b13==b18==b23=="0"):
      window.destroy()
      victory0()
    elif(b4==b9==b14==b19==b24=="1"):
      window.destroy()
      victory1()
    elif (b4==b9==b14==b19==b24=="0"):
      window.destroy()
      victory0()
    elif(b5==b10==b15==b20==b25=="1"):
      window.destroy()
      victory1()
    elif (b5==b10==b15==b20==b25=="0"):
      window.destroy()
      victory0()
    elif(b1==b7==b13==b19==b25=="1"):
      window.destroy()
      victory1()
    elif (b1==b7==b13==b19==b25=="0"):
      window.destroy()
      victory0()
    elif(b5==b9==b13==b17==b21=="1"):
      window.destroy()
      victory1()
    elif (b5==b9==b13==b17==b21=="0"):
      window.destroy()
      victory0()
    elif((b1=="0" or b1=="1") and (b2=="1" or b2=="0") and (b3=="0" or b3=="1") and (b4=="0" or b4=="1") and (b5=="0" or b5=="1") and (b6=="0" or b6=="1") and (b7=="0" or b7=="1") and (b8=="0" or b8=="1") and (b9=="0" or b9=="1") and (b10=="0" or b10=="1") and (b11=="0" or b11=="1") and (b12=="0" or b12=="1") and (b13=="0" or b13=="1") and (b14=="0" or b14=="1") and (b15=="0" or b15=="1") and (b16=="0" or b16=="1") and (b17=="0" or b17=="1") and (b18=="0" or b18=="1") and (b19=="0" or b19=="1") and (b20=="1" or b20=="0") and (b21=="0" or b21=="1") and (b22=="0" or b22=="1") and (b23=="0" or b23=="1") and (b24=="0" or b24=="1") and (b25=="0" or b25=="1")):
        window.destroy()
        draw()
  bt1 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic1)
  bt1.grid(column=1, row=1)
  bt2 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic2)
  bt2.grid(column=2, row=1)
  bt3 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic3)
  bt3.grid(column=3, row=1)
  bt4 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic4)
  bt4.grid(column=4, row=1)
  bt5 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic5)
  bt5.grid(column=5, row=1)
  bt6 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic6)
  bt6.grid(column=1, row=2)
  bt7 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic7)
  bt7.grid(column=2, row=2)
  bt8 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic8)
  bt8.grid(column=3, row=2)
  bt9 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic9)
  bt9.grid(column=4, row=2)
  bt10 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic10)
  bt10.grid(column=5, row=2)
  bt11 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic11)
  bt11.grid(column=1, row=3)
  bt12 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic12)
  bt12.grid(column=2, row=3)
  bt13 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic13)
  bt13.grid(column=3, row=3)
  bt14 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic14)
  bt14.grid(column=4, row=3)
  bt15 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic15)
  bt15.grid(column=5, row=3)
  bt16 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic16)
  bt16.grid(column=1, row=4)
  bt17 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic17)
  bt17.grid(column=2, row=4)
  bt18 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic18)
  bt18.grid(column=3, row=4)
  bt19 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic19)
  bt19.grid(column=4, row=4)
  bt20 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic20)
  bt20.grid(column=5, row=4)
  bt21 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic21)
  bt21.grid(column=1, row=5)
  bt22 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic22)
  bt22.grid(column=2, row=5)
  bt23 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic23)
  bt23.grid(column=3, row=5)
  bt24 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic24)
  bt24.grid(column=4, row=5)
  bt25 = Button(window, text=" ",bg="green", fg="Black",width=5,height=3,font=('Helvetica','20'),command=clic25)
  bt25.grid(column=5, row=5)

  window.mainloop()

tn=1 
def gameloopxo():
  window=Tk()
  
  window.title("TIC TAC TOE")
  window.geometry("1300x715+0+0")
  r=Label(window,text="Start by clicking any button ->>",font=('Helvetica','20'))
  r.grid(row=1,column=0)
  l=Label(window,text="TIC-TAC-TOE",font=('Hevetica','50'))
  l.grid(row=0,column=0)
  def c1():
    global tn
    if bto1["text"]==" ":
      if tn==1:
        tn=2
        bto1["text"]="X"
      elif tn==2:
        tn=1
        bto1["text"]="O"
      chk()
  def c2():
    global tn
    if bto2["text"]==" ":
      if tn==1:
        tn=2
        bto2["text"]="X"
      elif tn==2:
        tn=1
        bto2["text"]="O"
      chk()
  def c3():
    global tn
    if bto3["text"]==" ":
      if tn==1:
        tn=2
        bto3["text"]="X"
      elif tn==2:
        tn=1
        bto3["text"]="O"
      chk()
  def c4():
    global tn
    if bto4["text"]==" ":
      if tn==1:
        tn=2
        bto4["text"]="X"
      elif tn==2:
        tn=1
        bto4["text"]="O"
      chk()
  def c5():
    global tn
    if bto5["text"]==" ":
      if tn==1:
        tn=2
        bto5["text"]="X"
      elif tn==2:
        tn=1
        bto5["text"]="O"
      chk()
  def c6():
    global tn
    if bto6["text"]==" ":
      if tn==1:
        tn=2
        bto6["text"]="X"
      elif tn==2:
        tn=1
        bto6["text"]="O"
      chk()
  def c7():
    global tn
    if bto7["text"]==" ":
      if tn==1:
        tn=2
        bto7["text"]="X"
      elif tn==2:
        tn=1
        bto7["text"]="O"
      chk()
  def c8():
    global tn
    if bto8["text"]==" ":
      if tn==1:
        tn=2
        bto8["text"]="X"
      elif tn==2:
        tn=1
        bto8["text"]="O"
      chk()
  def c9():
    global tn
    if bto9["text"]==" ":
      if tn==1:
        tn=2
        bto9["text"]="X"
      elif tn==2:
        tn=1
        bto9["text"]="O"
      chk()
  def c10():
    global tn
    if bto10["text"]==" ":
      if tn==1:
        tn=2;
        bto10["text"]="X"
      elif tn==2:
        tn=1;
        bto10["text"]="O"
      chk()
  def c11():
    global tn
    if bto11["text"]==" ":
      if tn==1:
        tn=2;
        bto11["text"]="X"
      elif tn==2:
        tn=1;
        bto11["text"]="O"
      chk()
  def c12():
    global tn
    if bto12["text"]==" ":
      if tn==1:
        tn=2;
        bto12["text"]="X"
      elif tn==2:
        tn=1;
        bto12["text"]="O"
      chk()
  def c13():
    global tn
    if bto13["text"]==" ":
      if tn==1:
        tn=2;
        bto13["text"]="X"
      elif tn==2:
        tn=1;
        bto13["text"]="O"
      chk()
  def c14():
    global tn
    if bto14["text"]==" ":
      if tn==1:
        tn=2;
        bto14["text"]="X"
      elif tn==2:
        tn=1;
        bto14["text"]="O"
      chk()
  def c15():
    global tn
    if bto15["text"]==" ":
      if tn==1:
        tn=2;
        bto15["text"]="X"
      elif tn==2:
        tn=1;
        bto15["text"]="O"
      chk()
  def c16():
    global tn
    if bto16["text"]==" ":
      if tn==1:
        tn=2;
        bto16["text"]="X"
      elif tn==2:
        tn=1;
        bto16["text"]="O"
      chk()
  def c17():
    global tn
    if bto17["text"]==" ":
      if tn==1:
        tn=2;
        bto17["text"]="X"
      elif tn==2:
        tn=1;
        bto17["text"]="O"
      chk()
  def c18():
    global tn
    if bto18["text"]==" ":
      if tn==1:
        tn=2;
        bto18["text"]="X"
      elif tn==2:
        tn=1;
        bto18["text"]="O"
      chk()
  def c19():
    global tn
    if bto19["text"]==" ":
      if tn==1:
        tn=2;
        bto19["text"]="X"
      elif tn==2:
        tn=1;
        bto19["text"]="O"
      chk()
  def c20():
    global tn
    if bto20["text"]==" ":
      if tn==1:
        tn=2;
        bto20["text"]="X"
      elif tn==2:
        tn=1;
        bto20["text"]="O"
      chk()
  def c21():
    global tn
    if bto21["text"]==" ":
      if tn==1:
        tn=2;
        bto21["text"]="X"
      elif tn==2:
        tn=1;
        bto21["text"]="O"
      chk()
  def c22():
    global tn
    if bto22["text"]==" ":
      if tn==1:
        tn=2;
        bto22["text"]="X"
      elif tn==2:
        tn=1;
        bto22["text"]="O"
      chk()
  def c23():
    global tn
    if bto23["text"]==" ":
      if tn==1:
        tn=2;
        bto23["text"]="X"
      elif tn==2:
        tn=1;
        bto23["text"]="O"
      chk()
  def c24():
    global tn
    if bto24["text"]==" ":
      if tn==1:
        tn=2;
        bto24["text"]="X"
      elif tn==2:
        tn=1;
        bto24["text"]="O"
      chk()
  def c25():
    global tn
    if bto25["text"]==" ":
      if tn==1:
        tn=2;
        bto25["text"]="X"
      elif tn==2:
        tn=1;
        bto25["text"]="O"
      chk()
  
  def chk():
    b1=bto1["text"]
    b2=bto2["text"]
    b3=bto3["text"]
    b4=bto4["text"]
    b5=bto5["text"]
    b6=bto6["text"]
    b7=bto7["text"]
    b8=bto8["text"]
    b9=bto9["text"]
    b10=bto10["text"]
    b11=bto11["text"]
    b12=bto12["text"]
    b13=bto13["text"]
    b14=bto14["text"]
    b15=bto15["text"]
    b16=bto16["text"]
    b17=bto17["text"]
    b18=bto18["text"]
    b19=bto19["text"]
    b20=bto20["text"]
    b21=bto21["text"]
    b22=bto22["text"]
    b23=bto23["text"]
    b24=bto24["text"]
    b25=bto25["text"]
    

    if (b1==b2==b3==b4==b5=="O"):
      window.destroy()
      victoryo()
    elif (b1==b2==b3==b4==b5=="X"):
      window.destroy()
      victoryx()
    elif (b6==b7==b8==b9==b10=="O"):
      window.destroy()
      victoryo()
    elif (b6==b7==b8==b9==b10=="X"):
      window.destroy()
      victoryx()
    elif (b11==b12==b13==b14==b15=="O"):
      window.destroy()
      victoryo() 
    elif (b11==b12==b13==b14==b15=="X"):
      window.destroy()
      victoryx()
    elif (b16==b17==b18==b19==b20=="O"):
      window.destroy()
      victoryo() 
    elif(b16==b17==b18==b19==b20=="X"):
      window.destroy()
      victoryx()
    elif (b21==b22==b23==b24==b25=="O"):
      window.destroy()
      victoryo()
    elif (b21==b22==b23==b24==b25=="X"):
      window.destroy()
      victoryx()
    elif (b1==b6==b11==b16==b21=="O"):
      window.destroy()
      victoryo()
    elif (b1==b6==b11==b16==b21=="X"):
      window.destroy()
      victoryx()
    elif (b2==b7==b12==b17==b22=="O"):
      window.destroy()
      victoryo() 
    elif (b2==b7==b12==b17==b22=="X"):
      window.destroy()
      victoryx()
    elif (b3==b8==b13==b18==b23=="O"):
      window.destroy()
      victoryo()
    elif (b3==b8==b13==b18==b23=="X"):
      window.destroy()
      victoryx()
    elif (b4==b9==b14==b19==b24=="O"):
      window.destroy()
      victoryo()
    elif (b4==b9==b14==b19==b24=="X"):
      window.destroy()
      victoryx()
    elif (b5==b10==b15==b20==b25=="O"):
      window.destroy()
      victoryo()
    elif (b5==b10==b15==b20==b25=="X"):
      window.destroy()
      victoryx()
    elif (b1==b7==b13==b19==b25=="O"):
      window.destroy()
      victoryo()
    elif (b1==b7==b13==b19==b25=="X"):
      window.destroy()
      victoryx()
    elif (b5==b9==b13==b17==b21=="O") :
      window.destroy()
      victoryo()
    elif (b5==b9==b13==b17==b21=="X"):
      window.destroy()
      victoryx()
     
    elif((b1=="O" or b1=="X") and (b2=="O" or b2=="X") and (b3=="O" or b3=="X") and (b4=="O" or b4=="X") and (b5=="O" or b5=="X") and (b6=="O" or b6=="X") and (b7=="O" or b7=="X") and (b8=="O" or b8=="X") and (b9=="O" or b9=="X") and (b10=="O" or b10=="X") and (b11=="O" or b11=="X") and (b12=="O" or b12=="X") and (b13=="O" or b13=="X") and (b14=="O" or b14=="X") and (b15=="O" or b15=="X") and (b16=="O" or b16=="X") and (b17=="O" or b17=="X") and (b18=="O" or b18=="X") and (b19=="O" or b19=="X") and (b20=="O" or b20=="X") and (b21=="O" or b21=="X") and (b22=="O" or b22=="X") and (b23=="O" or b23=="X") and (b24=="O" or b24=="X") and (b25=="O" or b25=="X")):
        window.destroy()
        draw()

  bto1=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c1)
  bto1.grid(column=1,row=1)
  bto2=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c2)
  bto2.grid(column=2,row=1)
  bto3=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c3)
  bto3.grid(column=3,row=1)
  bto4=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c4)
  bto4.grid(column=4,row=1)
  bto5=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c5)
  bto5.grid(column=5,row=1)
  bto6=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c6)
  bto6.grid(column=1,row=2)
  bto7=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c7)
  bto7.grid(column=2,row=2)
  bto8=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c8)
  bto8.grid(column=3,row=2)
  bto9=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c9)
  bto9.grid(column=4,row=2)
  bto10=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c10)
  bto10.grid(column=5,row=2)
  bto11=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c11)
  bto11.grid(column=1,row=3)
  bto12=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c12)
  bto12.grid(column=2,row=3)
  bto13=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c13)
  bto13.grid(column=3,row=3)
  bto14=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c14)
  bto14.grid(column=4,row=3)
  bto15=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c15)
  bto15.grid(column=5,row=3)
  bto16=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c16)
  bto16.grid(column=1,row=4)
  bto17=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c17)
  bto17.grid(column=2,row=4)
  bto18=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c18)
  bto18.grid(column=3,row=4)
  bto19=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c19)
  bto19.grid(column=4,row=4)
  bto20=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c20)
  bto20.grid(column=5,row=4)
  bto21=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c21)
  bto21.grid(column=1,row=5)
  bto22=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c22)
  bto22.grid(column=2,row=5)
  bto23=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c23)
  bto23.grid(column=3,row=5)
  bto24=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c24)
  bto24.grid(column=4,row=5)
  bto25=Button(window,text=" ",bg="blue",fg="yellow",width=5,height=3,font=('Helvetica','20'),command=c25)
  bto25.grid(column=5,row=5)

  window.mainloop()
  
def instr():
  done = False
  while not done:
    instrsc = pygame.display.set_mode((1300,715))
    instrsc.blit(bg,(0,0)) 
    message_to_screen('Instructions', g, 540, 30, 60)
    message_to_screen('1. This is a multiplier game played by two players.', w, 40,100, 40)
    message_to_screen('2. You have to select the boxes by clicking on them using mouse alternatively. This places your desired charecter in the box.', w, 40, 140, 40)
    message_to_screen('    desired charecter in the box.', w, 40, 180, 40)
    message_to_screen('3. The player who manages to get his charecters alligned consecutively in a row, column or a ', w, 40, 220, 40)
    message_to_screen('    diagonal wins.', w, 40, 260, 40)
    message_to_screen('4. If no player manages to get his charecters alligned as said in the previous instruction then,', w, 40, 300, 40)
    message_to_screen('    the match is said to have tied.', w, 40, 340, 40)
    screen.fill(r,[100,615,200,50])
    message_to_screen('Back', w, 150, 620, 45)

    mousepos = pygame.mouse.get_pos()
    if 100<mousepos[0]<300 and 615<mousepos[1]<665:
      screen.fill(bri_r,[100,615,200,50])
      message_to_screen('Back', w, 150, 620, 45)
    
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        done=True
      if event.type == MOUSEBUTTONDOWN:
        if 100<mousepos[0]<300 and 615<mousepos[1]<665 and event.button == 1:
          intro()
         
    pygame.display.update()
  pygame.quit()
  quit()
def select():
  done = False
  while not done:
    selscr = pygame.display.set_mode((1300,715))
    selscr.blit(bg,(0,0))
    message_to_screen('Please select the elements you want to play with from below',r,200,122.50,50) 
    selscr.fill(blue,[300,225,200,50])
    selscr.fill(blue,[800,225,200,50])
    message_to_screen('X or O', w, 370, 230, 45)
    message_to_screen('0 or 1', w, 865, 230, 45)
    screen.fill(r,[100,615,200,50])
    message_to_screen('Back', w, 150, 620, 45)
    
    mousepos = pygame.mouse.get_pos()
    if 300<mousepos[0]<500 and 225<mousepos[1]<275:
      screen.fill(bri_blue,[300,225,200,50])
      message_to_screen('X or O', w, 370, 230, 45)
    if 800<mousepos[0]<1000 and 225<mousepos[1]<275:
      screen.fill(bri_blue,[800,225,200,50])
      message_to_screen('0 or 1', w, 865, 230, 45)
    if 100<mousepos[0]<300 and 615<mousepos[1]<665:
      screen.fill(bri_r,[100,615,200,50])
      message_to_screen('Back', w, 150, 620, 45)

    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if 100<mousepos[0]<300 and 615<mousepos[1]<665 and event.button == 1:
          intro()
        if 300<mousepos[0]<500 and 225<mousepos[1]<275 and event.button == 1:
          gameloopxo()
        if 800<mousepos[0]<1000 and 225<mousepos[1]<275 and event.button ==1:
          gameloop10()
    #pygame.display.update()
#  done = False
#  while not done:
 #   message_to_screen('Please select a charecter from below',r,200,357.50,50) 
  #  selscr.fill(blue,[300,460,200,50])
   # selscr.fill(blue,[800,460,200,50])
  #  message_to_screen('X', w, 400, 465, 45)
   # message_to_screen('O', w, 900, 465, 45)
  #  screen.fill(r,[100,615,200,50])
  #  message_to_screen('Back', w, 150, 620, 45)
     
  #  mouseposnew = pygame.mouse.get_pos()
    #if 300<mouseposnew[0]<500 and 460<mouseposnew[1]<510:
    #  screen.fill(bri_blue,[300,460,200,50])
   #   message_to_screen('X', w, 400, 465, 45)
    #if 800<mouseposnew[0]<1000 and 460<mouseposnew[1]<510:
     # screen.fill(bri_blue,[800,460,200,50])
     # message_to_screen('O', w, 900, 465, 45)
  #  if 100<mouseposnew[0]<300 and 615<mouseposnew[1]<665:
  #    screen.fill(bri_r,[100,615,200,50])
  #    message_to_screen('Back', w, 150, 620, 45)

    #for event in pygame.event.get():
    #  if event.type==pygame.QUIT:
    #    done=True
    #  if event.type == MOUSEBUTTONDOWN:
    #    if 100<mouseposnew[0]<300 and 615<mouseposnew[1]<665 and event.button == 1:
    #      intro()
    pygame.display.update()
  pygame.quit()
  quit()
    
# Victory when the player playing with x wins.
def victoryx():
  done = False
  while not done:
    endscr = pygame.display.set_mode((1300,715)) 
    endscr.blit(endim,(0,0))
    message_to_screen('Player X wins!', w, 530, 70, 60)
    screen.fill(g,[300,523.75,200,50])
    screen.fill(r,[800,523.75,200,50])
    message_to_screen('Play Again', w, 324, 528.75, 45)
    message_to_screen('Quit', w, 870, 528.75, 45)

    mousepos = pygame.mouse.get_pos()
    if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_g,[300,523.75,200,50])
      message_to_screen('Play Again', w, 324, 528.75, 45)
    if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_r,[800,523.75,200,50])
      message_to_screen('Quit', w, 870, 528.75, 45)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75 and event.button == 1:
          done = True
        if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75 and event.button == 1:
          select()
    pygame.display.update() 
  pygame.quit()
  quit()

def victoryo():
  done = False
  while not done:
    endscr = pygame.display.set_mode((1300,715)) 
    endscr.blit(endim,(0,0))
    message_to_screen('Player O wins!', w, 530, 70, 60)
    screen.fill(g,[300,523.75,200,50])
    screen.fill(r,[800,523.75,200,50])
    message_to_screen('Play Again', w, 324, 528.75, 45)
    message_to_screen('Quit', w, 870, 528.75, 45)

    mousepos = pygame.mouse.get_pos()
    if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_g,[300,523.75,200,50])
      message_to_screen('Play Again', w, 324, 528.75, 45)
    if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_r,[800,523.75,200,50])
      message_to_screen('Quit', w, 870, 528.75, 45)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75 and event.button == 1:
          done = True
        if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75 and event.button == 1:
          select()
    pygame.display.update() 
  pygame.quit()
  quit()

def victory0():
  done = False
  while not done:
    endscr = pygame.display.set_mode((1300,715)) 
    endscr.blit(endim,(0,0))
    message_to_screen('Player 0 wins!', w, 530, 70, 60)
    screen.fill(g,[300,523.75,200,50])
    screen.fill(r,[800,523.75,200,50])
    message_to_screen('Play Again', w, 324, 528.75, 45)
    message_to_screen('Quit', w, 870, 528.75, 45)

    mousepos = pygame.mouse.get_pos()
    if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_g,[300,523.75,200,50])
      message_to_screen('Play Again', w, 324, 528.75, 45)
    if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_r,[800,523.75,200,50])
      message_to_screen('Quit', w, 870, 528.75, 45)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75 and event.button == 1:
          done = True
        if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75 and event.button == 1:
          select()
    pygame.display.update() 
  pygame.quit()
  quit()

# This victory is when the player who plays with 1 wins.
def victory1():
  done = False
  while not done:
    endscr = pygame.display.set_mode((1300,715)) 
    endscr.blit(endim,(0,0))
    message_to_screen('Player 1 wins!', w, 530, 70, 60)
    screen.fill(g,[300,523.75,200,50])
    screen.fill(r,[800,523.75,200,50])
    message_to_screen('Play Again', w, 324, 528.75, 45)
    message_to_screen('Quit', w, 870, 528.75, 45)

    mousepos = pygame.mouse.get_pos()
    if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_g,[300,523.75,200,50])
      message_to_screen('Play Again', w, 324, 528.75, 45)
    if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_r,[800,523.75,200,50])
      message_to_screen('Quit', w, 870, 528.75, 45)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75 and event.button == 1:
          done = True
        if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75 and event.button == 1:
          select()
    pygame.display.update() 
  pygame.quit()
  quit()

def draw():
  done = False
  while not done:
    drscr = pygame.display.set_mode((1300,715))  
    drscr.blit(bd,(0,0))
    message_to_screen('GAME DRAWN', w, 490, 150, 60)
    screen.fill(g,[300,523.75,200,50])
    screen.fill(r,[800,523.75,200,50])
    message_to_screen('Play Again', w, 324, 528.75, 45)
    message_to_screen('Quit', w, 870, 528.75, 45)
    mousepos = pygame.mouse.get_pos()
    if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_g,[300,523.75,200,50])
      message_to_screen('Play Again', w, 324, 528.75, 45)
    if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75:
      screen.fill(bri_r,[800,523.75,200,50])
      message_to_screen('Quit', w, 870, 528.75, 45)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if 800<mousepos[0]<1000 and 523.75<mousepos[1]<573.75 and event.button == 1:
          done = True
        if 300<mousepos[0]<500 and 523.75<mousepos[1]<573.75 and event.button == 1:
          select()
    pygame.display.update() 
  pygame.quit()
  quit() 
#select()
intro()
#victory()



