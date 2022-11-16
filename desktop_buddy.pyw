from tkinter import *
from tkinter import ttk
import random
ib = 0
itr = 0
dist = 0
root = Tk()
frm = ttk.Frame(root, padding=10)

#frm.grid()
fileurl = "C:\\Users\\james\\source\\repos\\desktop buddy\\desktop buddy\\"
frames = [PhotoImage(file=fileurl+"idle.gif",format = 'gif -index %i' %(i)) for i in range(5)]
walking_left = [PhotoImage(file=fileurl+"walking_negative.gif",format = 'gif -index %i' %(i)) for i in range(8)]
walking_right = [PhotoImage(file=fileurl+"walking_positive.gif",format = 'gif -index %i' %(i)) for i in range(8)]
idle_to_sleep = [PhotoImage(file=fileurl+"idle_to_sleep.gif",format = 'gif -index %i' %(i)) for i in range(8)]
idle = [PhotoImage(file=fileurl+"idle.gif",format = 'gif -index %i' %(i)) for i in range(5)]
sleep = [PhotoImage(file=fileurl+"sleep.gif",format = 'gif -index %i' %(i)) for i in range(3)]
tb = [idle, walking_left,sleep, walking_right]
x = 300
ind = 0
y = root.winfo_screenheight()-150
def update():
    global ind
    global dist
    global frames
    #print(str(ind) +"/" + str(len(frames)+1))
    #print(frames)
    frame = frames[ind]
    ind += 1
    if ind >= len(frames):
        #if(dist == 2):
        #    frames = [PhotoImage(file=fileurl+"sleep.gif",format = 'gif -index %i' %(i)) for i in range(3)]
        ind = 0
    label.configure(image=frame)
    root.after(400, update)
label = Label(root,bd=0,bg='black')
label.pack()
root.after(0, update)
def stay_on_top():
   root.lift()
   root.after(1, stay_on_top)
root.overrideredirect(True)
root.wm_attributes('-transparentcolor','black')
root.config(highlightbackground='black')
t = str(root.winfo_screenheight()-150)

#root.geometry(f"+200+{t}")

def moveAround():
    global itr
    global ib
    global dist
    global frames
    global td
    global ind
    frames = tb[0]
    ind = 0
    dist = random.randint(-1,2)
    frames = tb[dist]
    ind = 0
    ib = 0
    itr = random.randint(100,500)
    
    move()
    root.after(random.randint(10000,10000), moveAround)


def move():
    global ib
    global itr
    global dist
    global ind
    global x
    global frames
    global td
    ib+=1
    frames = tb[dist]
    if(dist > 1):
        x += 0
    else:
        x += dist
    root.geometry(f"+{str(x)}+{str(y)}")
    if(ib>itr):
        frames = tb[0]
        ind = 0
        return
    else:
        root.after(10, move)

def byebye():
    root.destroy()

m = Menu(root, tearoff=0)


m.add_command(label="bye bye little guy", command=byebye)
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()
root.bind("<Button-3>", do_popup)




moveAround()
stay_on_top()
root.mainloop()