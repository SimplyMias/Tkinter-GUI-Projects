from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Form")
root.geometry("350x450")

gender_var = StringVar()
gender_var.set("Male")

swim_var = IntVar()
ride_var = IntVar()
race_var = IntVar()

def submit():
    user_name = enter_name.get()
    user_mail = enter_mail.get()
    user_pass = enter_pass.get()
    hobies = []
    if swim_var.get():
       hobies.append("Swimming")
    if ride_var.get():
       hobies.append("Riding")
    if race_var.get():
       hobies.append("Racing")

    gender = gender_var.get()
    messagebox.showinfo("Form Data", f"Name: {user_name}\nEmail: {user_mail}\nPassword: {user_pass}\nHobbies: {', '.join(hobies)}\nGender: {gender}")


Label(root,text="Username").grid(row=0,column=1,padx=5,pady=5)
enter_name = Entry(root)
enter_name.grid(row=0,column=2,pady=10)

Label(root,text="E-mail").grid(row=1,column=1,padx=5,pady=5)
enter_mail = Entry(root)
enter_mail.grid(row=1,column=2,pady=10)

Label(root,text="Password").grid(row=2,column=1,padx=5,pady=5)
enter_pass= Entry(root,show="*")
enter_pass.grid(row=2,column=2,pady=10)

Label(root,text="Hobies").grid(row=3,column=0,pady=5,padx=5)
Checkbutton(root,text="Swimming",variable=swim_var).grid(row=3,column=1)
Checkbutton(root,text="Riding",variable=ride_var).grid(row=3,column=2)
Checkbutton(root,text="Racing",variable=race_var).grid(row=3,column=3)

Label(root,text="Gender").grid(row=4,column=0,pady=5,padx=5)
Radiobutton(root,text="Male",value="Male",variable=gender_var).grid(row=4,column=1)
Radiobutton(root,text="Female",value="Female",variable=gender_var).grid(row=4,column=2)
Radiobutton(root,text="Other",value="Other",variable=gender_var).grid(row=4,column=3)

Button(root,text="Submit",command=submit).grid(row=5,column=2,padx=10,pady=10)

root.mainloop()