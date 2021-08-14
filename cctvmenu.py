from tkinter import *
from PIL import Image, ImageTk
from in_out import in_out
from motion import noise
from record import record
from attendance import attendance
from monitor import monitor
from see_attendance import see_attendance
from about import ab
from contact import co

def d():
    window = Tk()
    window.title("Smart cctv")
    # window.iconphoto(False, PhotoImage(file='icons/recording.png'))
    window.iconphoto(False, PhotoImage(file='icons/main.png'))
    # window.wm_iconbitmap('a.ico')

    l0 = Label(window, text="")
    l0.grid(row=0, column=0)

    label1_title = Label(window, text="Smart Cctv", font=('Helvetica', 45, 'bold'), fg='purple')
    label1_title.grid(row=0, column=1)

    image = Image.open('icons/a.jpg')
    image = image.resize((250, 250))
    image = ImageTk.PhotoImage(image)
    label2_image = Label(window, image=image)
    label2_image.grid(row=1, column=1)

    btn1_image = Image.open('icons/incognito.png')
    btn1_image = btn1_image.resize((50, 50))
    btn1_image = ImageTk.PhotoImage(btn1_image)
    btn1 = Button(window, text='Monitor', font=('normal', 25,), height=110, width=340, fg='green', image=btn1_image,
                  command=monitor, compound='left')
    btn1.grid(row=2, column=0, padx=40, pady=10)

    btn2_image = Image.open('icons/rectangle-of-cutted-line.png')
    btn2_image = btn2_image.resize((50, 50))
    btn2_image = ImageTk.PhotoImage(btn2_image)
    btn2 = Button(window, text='Face Recognition\n&\nAttendence', font=('normal', 20,), height=110, width=340,
                  fg='orange', command=attendance, compound='left', image=btn2_image)
    btn2.grid(row=3, column=0, padx=40, pady=10)

    btn3_image = Image.open('icons/security-camera.png')
    btn3_image = btn3_image.resize((50, 50))
    btn3_image = ImageTk.PhotoImage(btn3_image)
    btn3 = Button(window, text='Motion', font=('normal', 25,), height=110, width=340, fg='green', command=noise,
                  image=btn3_image, compound='left')
    btn3.grid(row=4, column=0, padx=40, pady=30)

    btn4_image = Image.open('icons/recording.png')
    btn4_image = btn4_image.resize((50, 50))
    btn4_image = ImageTk.PhotoImage(btn4_image)
    btn4 = Button(window, text='Record', font=('normal', 25,), height=110, width=340, fg='orange', command=record,
                  image=btn4_image, compound='left')
    btn4.grid(row=2, column=2, padx=40, pady=10)

    btn5_image = Image.open('icons/incognito.png')
    btn5_image = btn5_image.resize((50, 50))
    btn5_image = ImageTk.PhotoImage(btn5_image)
    btn5 = Button(window, text='In Out', font=('normal', 25,), height=110, width=340, fg='green', command=in_out,
                  image=btn5_image, compound='left')
    btn5.grid(row=3, column=2, padx=40, pady=10)

    btn6_image = Image.open('icons/exit.png')
    btn6_image = btn6_image.resize((50, 50))
    btn6_image = ImageTk.PhotoImage(btn6_image)
    btn6 = Button(window, text='Attendance\nSheet', font=('normal', 25,), height=110, width=340, fg='red',
                  command=see_attendance, image=btn6_image, compound='left')
    btn6.grid(row=4, column=2, padx=40, pady=30)

    btn7 = Button(window,text='About us', font=('normal',10,),height=1, width=6, fg='red', command=ab)
    btn7.grid(row=3,column=1,padx=1,pady=1)

    btn8 = Button(window, text='Contact', font=('normal', 10,), height=1, width=6, fg='red', command=co)
    btn8.grid(row=4, column=1, padx=1, pady=1)

    window.mainloop()

