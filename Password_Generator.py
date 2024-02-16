from tkinter import *
from tkinter import messagebox
import string, random

root = Tk()
root.geometry("500x500")
root.title("Password Generator")
root.config(bg="white")
root.resizable(False, False)
global entername
frame = Frame(root)
def password_generate():
    try:
        
        lengthpass = int(lenpass.get())
        
        small = string.ascii_lowercase
        capital = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation
        s = []
        s.extend(list(small))
        s.extend(list(capital))
        s.extend(list(digits))
        s.extend(list(special))
        random.shuffle(s)
        password.set("".join(s[0:lengthpass]))
    except:
        messagebox.askretrycancel("Please Try Again")

def clearFunc():
    entername.set("")

def accept():
    username =user_name.get()

    if username == "Shrishty":
        messagebox.showinfo("Accepted")
    else:
        messagebox.showerror("Invalid User")


Title = Label(root, text="Password Generator", bg="white", fg="royal blue", font=("futura", 15, "bold"))
Title.pack(anchor="center", pady="20px")

length1 = Label(root, text="Enter User Name:- ", fg="black", bg="white", font=("ubuntu", 12))
length1.place(x="20px", y="70px")
entername = StringVar()
user_name = Entry(root,textvariable=entername, bd=2, fg="black", font=("ubuntu", 15))
user_name.place(x="200px", y="70px")

length = Label(root, text=" Enter Password Length:- ", fg="black", bg="white", font=("ubuntu", 12))
length.place(x="17px", y="96px")
plen = IntVar()
lenpass = Entry(root, textvariable=plen,bd=2, fg="black", font=("ubuntu", 15))
lenpass.place(x="200px", y="96px")

def on_enter(e):
    btn['bg'] = "purple"
    btn['fg'] = "white"

def on_leave(e):
    btn['bg'] = "blue"
    btn['fg'] = "white"   

btn = Button(root, text="Generate Password", bg="royal blue", fg="white", font=("ubuntu", 15), cursor="hand2", command=password_generate)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)
btn.pack(anchor="center", pady="80px")
acc_btn = Button(root, text="Accept", bg="light grey", fg="black", font=("ubuntu", 15), cursor="hand1", command=accept )
acc_btn.pack(anchor="center", pady="10px")
res_btn = Button(root, text="Reset", bg="light grey", fg="black", font=("ubuntu", 15), cursor="hand1" ,command=clearFunc)
res_btn.pack(anchor="center")

result = Label(root, text="Generated Password  :- ", bg="white", fg="black", font=("ubuntu", 12))
result.place(x="20px", y="190px")

password = StringVar()
password1 = Entry(root, textvariable= password, state="readonly", fg="darkgreen", font=("ubuntu", 15))
password1.place(x="200px", y="190px")

root.mainloop()