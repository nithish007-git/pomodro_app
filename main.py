import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFC0D3"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 0.5
reps=1
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_1,text="00:00")
    label1.config(text="")
    global reps
    reps=0

def focus_window(option):
    if option == "on":
            window.deiconify()
            window.focus_force()
            window.attributes('-topmost', 1)
    elif option == "off":
            window.attributes('-topmost', 0)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps


    work_sec=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long=LONG_BREAK_MIN*60

    print(reps)
    if reps%8==0:
        count_down(LONG_BREAK_MIN)
        label.config(text="longbreak",fg="#FBF8F1",bg=PINK)
    elif reps%2==0:
        count_down(short_break)
        label.config(text=" break",fg="#FBF8F1",bg=PINK)
        focus_window("on")
    elif reps>8:
        reset()
    else:
        count_down(work_sec)
        label.config(text="Hustle Mode",fg="#FBF8F1",bg=PINK)
        focus_window("on")

    reps += 1
def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_1,text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        workk=math.floor(reps/2)
        for i in range(workk):
            marks+="✓"
        label1.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("pomdoroapp")
window.config(width=500,height=500,bg="#FFC0D3")

canvas=Canvas(width=400,height=300,bg="#FFC0D3",highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(180,112,image=tomato_img)
timer_1=canvas.create_text(180,130,text="00:00",fill="white",font=(FONT_NAME,40,"bold"))
canvas.grid(column=2,row=2)

#timer
label=Label(text="Timer",font=(FONT_NAME,40,"bold"),fg="#FBF8F1",bg=PINK)
label.grid(column=2,row=1)

#start button
button=Button(text="Start",height=2,width=10,highlightthickness=0,command=start_timer)
button.grid(column=1,row=3,padx=60,pady=60)
#end button
button=Button(text="Reset",height=2,width=10,highlightthickness=0,command=reset)
button.grid(column=3,row=3,padx=60,pady=60)
#tick
label1 = Label(text="✓", bg="#FFC0D3")
label1.grid(column=2, row=3)

window.mainloop()