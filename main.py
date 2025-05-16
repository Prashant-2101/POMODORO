from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    windows.after_cancel(timer)
    can.itemconfig(t,text="00:00")
    lb.config(text="TIMER")
    check.config(text="")
    reps=0
    
def stop():
    windows.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def time_mech():
    global reps
    reps+=1
    if reps%16==0:
        c(LONG_BREAK_MIN*60)
        lb.config(text="LONG BREAK ENJOY")
        
    elif reps % 2 == 0:
        c(SHORT_BREAK_MIN*60)
        lb.config(text="SHORT BREAK")
    else:
        c(WORK_MIN*60)
        lb.config(text="WORK TIME")
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def c(co):
    minu=math.floor(co/60)
    seco=co%60
    if minu<10:
        minu=f"0{minu}"
    if seco<10:
        seco=f"0{seco}"
    can.itemconfig(t,text=f"{minu}:{seco}")
    
    if co>0:
        global timer
        timer=windows.after(1000,c,co-1)
    else:
        time_mech()
        tet=""
        for i in range(math.floor(reps/2)):
            tet+="✓"
        check.config(text=tet)
# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("MY POMODORO")
windows.config(padx=100, pady=100,bg=GREEN)

lb = Label(text="TIMER", font=(FONT_NAME, 30, "bold"), bg=GREEN)
lb.grid(row=0, column=1)

can = Canvas(width=300, height=300, bg=GREEN, highlightthickness=0)
sritam = PhotoImage(file="tomato.png")
can.create_image(150, 125, image = sritam)
can.grid(row=1, column=1)
t=can.create_text(150,140,text="00:00",font=(FONT_NAME,25,"bold"),fill="white")

b1 = Button(text="START",bg=PINK,font=(FONT_NAME, 15,"bold"), highlightthickness=0,command=time_mech )
b2 = Button(text="RESET", bg=PINK, font=(FONT_NAME, 15,"bold"), highlightthickness=0, command=reset)
b1.grid(row=2,column=0)
b2.grid(row = 2, column = 2)

check = Label(bg=GREEN, fg=RED, font=(FONT_NAME,50))
check.grid(row=2, column=1)
b3=Button(text="STOP",bg=PINK,font=(FONT_NAME, 15,"bold"), highlightthickness=0,command=stop )
b3.grid(row=3,column=1)
windows.mainloop()
