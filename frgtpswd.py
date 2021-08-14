from tkinter import *
import pymysql
from tkinter import messagebox,ttk

def forget_password_window():
    def reset_password():
        if txt_email.get() == "" or cmb_quest.get() == "" or txt_answer.get() == "" or txt_new_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!!")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="pass@123", database="durgesh_db")
                cur = con.cursor()
                cur.execute("select * from register_user where user_email=%s and user_sec_ques=%s and user_sec_ans=%s",(txt_email.get(), cmb_quest.get(), txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Email ID or Please Select the Correct Security Question/Answer", parent=root)
                else:
                    cur.execute("update register_user set user_password=%s,user_cpassword=%s where user_email=%s",(txt_new_pass.get(),txt_new_pass.get(), txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your Password has been Reset,Please login with New Password",parent=root)
                    reset()
                    root.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=root)

    def reset():
        cmb_quest.current(0)
        txt_new_pass.delete(0, END)
        txt_answer.delete(0, END)
        txt_new_pass.delete(0, END)
        txt_email.delete(0, END)
    try:
        root = Tk()
        root.title("Forget Password")
        root.geometry("350x400+495+150")
        root.config(bg="white")
        root.focus_force()
        root.grab_set()

        root.t = Label(root, text="Forget Password", font=("book antiqua", 20, "bold"), bg="white",fg="red").place(x=0, y=0, relwidth=1)

        ##--For Email--##
        root.email = Label(root, text="Email", font=("times new roman", 16, "bold"), bg="white",fg="gray").place(x=50,y=40)
        txt_email = Entry(root, font=("times new roman", 15), bg="lightgray")
        txt_email.place(x=50, y=70, width=250)

        ##--Forget Password--##
        root.Question = Label(root, text="Sequrity Question", font=("book antiqua", 15, "bold"), bg="white",fg="gray").place(x=50, y=100)
        cmb_quest = ttk.Combobox(root, font=("book antiqua", 13), state='readonly', justify=CENTER)
        cmb_quest['values'] = ("Select", "Your Country Name?", "Your Birth Place?", "Your Fther's Name?", "Your Best Friend Name?")
        cmb_quest.place(x=50, y=130, width=250)
        cmb_quest.current(0)

        Answer = Label(root, text="Answer", font=("book antiqua", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
        txt_answer = Entry(root, text=Answer, font=("book antiqua", 15), bg="lightgray")
        txt_answer.place(x=50, y=210, width=250)

        root.new_password = Label(root, text="New Password", font=("book antiqua", 15, "bold"), bg="white",fg="gray").place(x=50, y=260)
        txt_new_pass = Entry(root,show='*', font=("book antiqua", 15), bg="lightgray")
        txt_new_pass.place(x=50, y=290, width=250)

        root.btn_change_password = Button(root, text="Reset Password", command=reset_password, bg="green",cursor="hand2", fg="white", font=("book antiqua", 15, "bold")).place(x=90, y=340)

    except Exception as es:
        messagebox.showerror("Error", f"Error Due to: {str(es)}")  # , parent=root)
