from tkinter import *

root = Tk()
root.title("Feedback Form")
root.geometry("300x300")

def submit():
    print("Name: ",name_var.get())
    print("Course: ",course_var.get())
    print("Satisfaction: ",satisfaction_var.get())
    print("Comments: ",comment_box.get("1.0", END).strip())
     
    

name_var = StringVar()
course_var = StringVar()
satisfaction_var = IntVar()



Label(root,text="Name").grid(row=0,column=0)
Entry(root,textvariable=name_var).grid(row=0,column=1)

Label(root,text="Courses").grid(row=1,column=0)
Spinbox(root, values=("Maths","Physics","BEE","EVS"),textvariable=course_var).grid(row=1,column=1)

Label(root,text="Satisfaction").grid(row=2,column=0)
Scale(root, from_= 0, to_=7, orient=HORIZONTAL,variable=satisfaction_var).grid(row=2,column=1)

Label(root,text="Comment").grid(row=4,column=0)
comment_box = Text(root, height=4, width=25)
comment_box.grid(row=5, column=1)

Button(root, text="Submit",command=submit).grid(row=7,column=1)
root.mainloop()