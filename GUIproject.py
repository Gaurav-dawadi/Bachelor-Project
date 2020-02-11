from tkinter import *
import webbrowser
#from tkinter imoort messagebox
#import os
from select import *


# For Admin to Add Data
def database():
    master = Toplevel()
    master.geometry('800x450')

    frm = Frame(master, bg='#80c1ff')
    frm.place(relwidth=0.94, relheight=0.92, relx=0.02, rely=0.02)

    b1 = Button(frm, text="Register", command=get_at,  width=12, height=2, fg='green', font=4)
    b1.place(x=330, y=50)

    b1 = Button(frm, command=search1, text="Student Profile", width=12, height=2, fg='green', font=4)
    b1.place(x=330, y=130)

    b1 = Button(frm, command=search2, text="Teacher Profile", width=12, height=2, fg='green', font=4)
    b1.place(x=330, y=210)

    b1 = Button(frm, command=master.destroy, text="Back", width=12, height=2, fg='red', font=5)
    b1.place(x=330, y=290)


# For Teacher's Info Display
def search2():
    master5 = Toplevel()
    master5.geometry('800x500')

    topFrame = Frame(master5, bg='#80c1ff')
    topFrame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.1)
    bottomFrame = Frame(master5, bg="red")
    bottomFrame.pack()

    l1 = Label(topFrame, text="Name")
    l1.place(x=100, y=10, height=30)
    e1 = Entry(topFrame, bd=5)
    e1.place(x=200, y=10)

#For getting Teachers info After Searched
    def send():
        ename = e1.get()
        print("the name is:", ename)

        ename= str()
        #mEntry=Entry(mGui,textvariable=Ename)
        data = getTeachersData(ename)

        if (len(data) <= 0):
            label_0 = Label(master5, text="Data not found", width=15, font=("bold", 20))
            label_0.place(x=90, y=53)
        else:
            name = data[0][1]
            contact = data[0][2]
            address = data[0][3]
            department = data[0][4]
            email = data[0][5]

            label1_0 = Label(master5, text="Name", width=10, font=("bold", 20))
            label1_0.place(x=90, y=53)

            label1_1 = Label(master5, text=name, width=20, font=("bold", 20))
            label1_1.place(x=280, y=53)

            label2_0 = Label(master5, text="Contact", width=10, font=("bold", 20))
            label2_0.place(x=90, y=103)

            label2_1 = Label(master5, text=contact, width=20, font=("bold", 20))
            label2_1.place(x=280, y=103)

            label3_0 = Label(master5, text="Address", width=10, font=("bold", 20))
            label3_0.place(x=90, y=153)

            label3_1 = Label(master5, text=address, width=20, font=("bold", 20))
            label3_1.place(x=280, y=153)

            label4_0 = Label(master5, text="Department", width=10, font=("bold", 20))
            label4_0.place(x=90, y=203)

            label4_1 = Label(master5, text=department, width=20, font=("bold", 20))
            label4_1.place(x=280, y=203)

            label5_0 = Label(master5, text="Email", width=10, font=("bold", 20))
            label5_0.place(x=90, y=253)

            label5_1 = Label(master5, text=email, width=30, font=("bold", 20))
            label5_1.place(x=280, y=253)

    b1 = Button(topFrame, command=send, text="Enter", fg='blue', font=5)
    b1.place(x=380, y=10)

    master5.mainloop()


# For Student's Info Display
def search1():

    master6 = Toplevel()
    master6.geometry('800x500')

    topFrame = Frame(master6, bg='#80c1ff')
    topFrame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.1)
    bottomFrame = Frame(master6, bg="red")
    bottomFrame.pack()

    l1 = Label(topFrame, text="Name")
    l1.place(x=100, y=10, height=30)
    e1 = Entry(topFrame, bd=5)
    e1.place(x=200, y=10)

    # For getting Students info After Searched
    def send1():
        ename = e1.get()
        print("the name is:", ename)

        ename = str()
        # mEntry=Entry(mGui,textvariable=Ename)
        data = getStudentsData(ename)

        if (len(data) <= 0):
            label_0 = Label(master6, text="Data not found", width=15, font=("bold", 20))
            label_0.place(x=90, y=53)
        else:
            name = data[0][1]
            contact = data[0][2]
            address = data[0][3]
            department = data[0][4]
            email = data[0][5]

            label1_0 = Label(master6, text="Name", width=10, font=("bold", 20))
            label1_0.place(x=90, y=53)

            label1_1 = Label(master6, text=name, width=20, font=("bold", 20))
            label1_1.place(x=280, y=53)

            label2_0 = Label(master6, text="Contact", width=10, font=("bold", 20))
            label2_0.place(x=90, y=103)

            label2_1 = Label(master6, text=contact, width=20, font=("bold", 20))
            label2_1.place(x=280, y=103)

            label3_0 = Label(master6, text="Address", width=10, font=("bold", 20))
            label3_0.place(x=90, y=153)

            label3_1 = Label(master6, text=address, width=20, font=("bold", 20))
            label3_1.place(x=280, y=153)

            #label4_0 = Label(master6, text="Department", width=10, font=("bold", 20))
            #label4_0.place(x=90, y=203)

            #label4_1 = Label(master6, text=department, width=20, font=("bold", 20))
            #label4_1.place(x=280, y=203)

            label5_0 = Label(master6, text="Email", width=10, font=("bold", 20))
            label5_0.place(x=90, y=253)

            label5_1 = Label(master6, text=email, width=30, font=("bold", 20))
            label5_1.place(x=280, y=253)

    b1 = Button(topFrame, command=send1, text="Enter", fg='blue', font=5)
    b1.place(x=380, y=10)

    master6.mainloop()


# For Storing Teachers attendance in Database
def attend():
    id=2
    data = getTeachersData(id)

    if (len(data)<=0):
        print("Unregistered")
    else:
        if(isTeacherAttend(id)):
            if(teacherIsExiting(id)):
                print("You have exited")
            else:
                print("Error. Have you already exited? If not server error")
        else:
            if(teacherIsEntering(id)):
                print("Attendance Done")
            else:
                print("Attendance not done. Error!")


def nav():
    master = Toplevel()
    master.geometry('800x400')

    frm = Frame(master, bg='#80c1ff')
    frm.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    id = 2
    data = getTeachersData(id)

    if(len(data)<=0):
        label_0 = Label(master, text="Data not found", width=15, font=("bold", 20))
        label_0.place(x=90, y=53)
    else:
        name = data[0][1]
        contact = data[0][2]
        address = data[0][3]
        department = data[0][4]
        email = data[0][5]

        label1_0 = Label(master, text="Name", width=10, font=("bold", 20))
        label1_0.place(x=90, y=53)

        label1_1 = Label(master, text=name, width=20, font=("bold", 20))
        label1_1.place(x=280, y=53)

        label2_0 = Label(master, text="Contact", width=10, font=("bold", 20))
        label2_0.place(x=90, y=103)

        label2_1 = Label(master, text=contact, width=20, font=("bold", 20))
        label2_1.place(x=280, y=103)

        label3_0 = Label(master, text="Address", width=10, font=("bold", 20))
        label3_0.place(x=90, y=153)

        label3_1 = Label(master, text=address, width=20, font=("bold", 20))
        label3_1.place(x=280, y=153)

        label4_0 = Label(master, text="Department", width=10, font=("bold", 20))
        label4_0.place(x=90, y=203)

        label4_1 = Label(master, text=department, width=20, font=("bold", 20))
        label4_1.place(x=280, y=203)

        label5_0 = Label(master, text="Email", width=10, font=("bold", 20))
        label5_0.place(x=90, y=253)

        label5_1 = Label(master, text=email, width=30, font=("bold", 20))
        label5_1.place(x=280, y=253)

    master.mainloop()


def get_at():

    master1 = Toplevel()
    master1.geometry('800x500')

    frame = Frame(master1, bg='#80c1ff')
    frame.place(relwidth=0.94, relheight=0.92, relx=0.02, rely=0.02)

    label_0 = Label(frame, text="Sign In Page", width=20, font=("bold", 20))
    label_0.place(x=150, y=30)

    label_1 = Label(frame, text="FullName", width=10, font=("bold", 12))
    label_1.place(x=70, y=100)

    entry_1 = Entry(frame)
    entry_1.place(x=200, y=100, width=300)

    label_2 = Label(frame, text="Ph Num", width=10, font=("bold", 12))
    label_2.place(x=70, y=150)

    entry_2 = Entry(frame)
    entry_2.place(x=200, y=150, width=300)

    label_3 = Label(frame, text="Address", width=10, font=("bold", 12))
    label_3.place(x=70, y=200)

    entry_3 = Entry(frame)
    entry_3.place(x=200, y=200, width=300)

    label_4 = Label(frame, text="Department", width=10, font=("bold", 12))
    label_4.place(x=70, y=250)

    entry_4 = Entry(frame)
    entry_4.place(x=200, y=250, width=300)

    label_5 = Label(frame, text="Email", width=10, font=("bold", 12))
    label_5.place(x=70, y=300)

    entry_5 = Entry(frame)
    entry_5.place(x=200, y=300, width=300)

# Database connection
    def dataget():
        name = entry_1.get()

        phone = entry_2.get()

        address = entry_3.get()

        department = entry_4.get()

        email = entry_5.get()

        if name == "" or email == "" or address == "" or phone == "" or department == "":
            error()

        else:
            print('your account is created')

            print('Full name is: ', name)

            print('Phone number  is: ', phone)

            print('Address is: ', address)

            print('department is: ', department)

            print('email is: ', email)

            success = dataentry(name, phone, address, department, email)
            if (success):
                Label(frame, text="User has been registered successfully.").pack()
            else:
                Label(frame, text="Error in server.").pack()

            # validation process

    def error():

        master3 = Toplevel()
        master3.geometry('500x400')
        master3.title("Warning!")
        Label(master3, text="All fields required", font='courier 20 bold', fg="red").pack()

    Button(frame, text='Sign In', command=dataget, width=18, bg='green', fg='white').place(x=280, y=370)
    Button(frame, text='Back', command=master1.destroy, width=18, bg='red', fg='white').place(x=120, y=370)

    master1.mainloop()


# For Admin to Login
def access():

    master2 = Toplevel()
    master2.geometry('500x400')

    frame = Frame(master2, bg='#80c1ff')
    frame.place(relwidth=0.94, relheight=0.92, relx=0.02, rely=0.02)

    label_0 = Label(frame, text="Login Page", width=10, font=("bold", 20))
    label_0.place(x=175, y=35)

    label_1 = Label(frame, text="Password", width=9, font=("bold", 14))
    label_1.place(x=67, y=130)

    entry_1 = Entry(frame,  font=("bold", 12))
    entry_1.place(x=200, y=131)

    # Database connection

    def check():
        password = entry_1.get()

        if password == "" or password !="5599":
            error()

        else:
            print('Access Granted')
            database()

    def error():
        master3 = Toplevel()
        master3.geometry('400x100')
        master3.title("Warning!")
        Label(master3, text="Check Your Password", font='courier 22 bold', fg="red").pack()
        #tkMessageBox.showinfo("ERROR!!", "Check Your Password")
        #B1 = Button(, text="Say Hello", command=hello)
        #B1.pack()

    Button(frame, text='Enter', width=12, command=check, bg='green', fg='white').place(x=340, y=250)
    Button(frame, text='Back', command=master2.destroy, width=12, bg='red', fg='white').place(x=120, y=250)


# For Attendance
def img_at():

    master4 = Toplevel()
    master4.geometry('800x400')
    Label(master4, text="LOOK INTO THE CAMERA", font='courier 20 bold', fg="red").pack()


# For Visitor
def colz_info():

    master5 = Toplevel()
    master5.geometry('800x400')

    frame = Frame(master5, bg='#80c1ff')
    frame.place(relwidth=0.94, relheight=0.92, relx=0.02, rely=0.02)

    Button(frame, command=info, text='Web page', width=12, height=2, fg='green', font=10).place(x=320, y=20)
    Button(frame, text='General info', width=12, height=2, fg='green', font=10).place(x=320, y=110)
    Button(frame, text='Navigate', width=12, height=2, fg='green', font=10).place(x=320, y=210)
    Button(frame, text='Back', command=master5.destroy, width=12, height=2, fg='red', font=10).place(x=320, y=300)

# Web page opening for Visitor
def info():

    url = "http://sagarmatha.edu.np/home/about/introduction"
    webbrowser.open(url, new=2)

# Video opening for Visitor
#def vid():
    #os.system(C:\\Users\\rojina\\Downloads\\MV_Agusta_Brutale.mp4)


# MAIN WINDOW
root = Tk()

canvas = Canvas(width=800, height=400, bg='#80c1ff')
canvas.pack()

#frame = Frame(root, bg='#80c1ff')
#frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

label = Label(root, text="WELCOME TO SEC", fg='blue',  font="verdana 25 bold")
label.place(relwidth=0.7, relheight=0.1, relx=0.15, rely=0.05)

button = Button(root, command=access, text="ADMIN", width=12, height=2, fg='green', font=10)
button.place(x=350, y=100)

button = Button(root, command=img_at, text="ATTENDANCE", width=12, height=2, fg='green', font=10)
button.place(x=350, y=200)

button = Button(root, command=colz_info, text="VISITOR", width=12, height=2, fg='green', font=10)
button.place(x=350, y=300)

#button = Button(frame, command=choose, text="ENTER", width=10, height=2, fg='green', font=10)
#button = Button(frame, command=nav, text="ENTER", width=10, height=2, fg='green', font=10)

#photo = PhotoImage(file='C:\\Users\\rojina\\PycharmProjects\\untitled\\SEC.png‪‪')
#canvas.create_image(0, 0, image=photo, anchor=NW)

root.mainloop()


