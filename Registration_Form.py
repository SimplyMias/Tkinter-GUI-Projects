import tkinter as tk
import tkinter.messagebox as msg

def submit():
    name = enter_name.get()
    mail = enter_mail.get()
    gender = gender_var.get()   



    print(f"Name: {name}")
    print(f"Mail: {mail}")
    print(f"Gender: {gender}")
   

    msg.showinfo("Submitted",f"Name: {name}\nMail: {mail}\nGender: {gender}")
    

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x400")

label_name = tk.Label(root, text="Enter Name" )
label_name.pack(pady=5)

enter_name = tk.Entry(root)
enter_name.pack(pady=5)

label_mail = tk.Label(root, text="Enter E-mail")
label_mail.pack(pady=5)

enter_mail = tk.Entry(root)
enter_mail.pack(pady=5)

label_gender = tk.Label(root,text="Gender")
label_gender.pack(pady=5)

gender_var = tk.StringVar()
gender_var.set("Male")

radio_male = tk.Radiobutton(root, text="Male",variable=gender_var, value="Male")
radio_female = tk.Radiobutton(root, text="Female",variable=gender_var, value="Female")
radio_other = tk.Radiobutton(root, text="Other",variable=gender_var, value="Other")

radio_male.pack()
radio_female.pack()
radio_other.pack()

submit_button = tk.Button(root, text="submit",command=submit)
submit_button.pack(pady=10)

root.mainloop()