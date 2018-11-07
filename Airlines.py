from tkinter import *
from tkinter.messagebox import *
import sqlite3
root=Tk()
root.title("intro")
con=sqlite3.Connection('flight_db')
cur=con.cursor()
cur.execute("create table if not exists airlines(user_name varchar(20) primary key,first_name varchar(20),last_name varchar(20),phone_number number(10),email varchar(30),passw varchar(20))")

fr2=Frame()
fr2.pack(side=LEFT,expand=1)
Label(fr2,text="Project Submitted By:-",font=("algerian",38),compound="center",fg="Orange").pack()
Label(fr2,text="Aayush Agarwal (RA1611008010048)",font=("Bauhaus 93",14),fg="Red",compound="center").pack()

def airline():
    root.destroy()
    root1=Tk()
    root1.title("Booking Portal")
    b=PhotoImage(file="airoplane.gif")
    Label(root1,image=b).grid(row=0,column=0,columnspan=4)
    Label(root1,text="Welcome to Airline Booking System",font=("Bauhaus 93",17),fg="Red",width=46,bg="White").grid(row=0,column=0,columnspan=4)
    Label(root1,text="Flights Availability",font=("Bauhaus 93",17),fg="White",width=46,bg="red").grid(row=1,column=0,columnspan=4)
    Label(root1,text="Select Pick Up Point",font=("Bauhaus 93",14),fg="Blue").grid(row=2,column=1)
    variable = StringVar(root1)
    variable.set("Select Source") # default value
    w = OptionMenu(root1, variable, "Delhi", "Kolkata", "Mumbai","U.S.A","Canada")
    w.grid(row=2,column=2)
    Label(root1,text="Select Boarding Point",font=("Bauhaus 93",14),fg="Blue").grid(row=3,column=1)
    variable1 = StringVar(root1)
    variable1.set("Select Destination") # default value
    w = OptionMenu(root1, variable1, "Delhi", "Kolkata", "Mumbai","U.S.A","Canada")
    w.grid(row=3,column=2)
    #Sign In
    def signup():
                 def success():
                    user = user_name.get()
                    cur.execute("select user_name from airlines where user_name=(?)", (user,))
                    a = cur.fetchall()
                    if a != []:
                          showerror('Error',"Username Already Exists")
                    else:
                          l = (user_name.get(), first_name.get(), last_name.get(),phone_number.get(),email.get(), passw.get())
                          cur.execute("insert into airlines values(?,?,?,?,?,?)",l)
                          showinfo('Signed Up',"Congratulation You are Successfully Signed Up")
                          con.commit()
                          user_name.delete(0,20)
                          
                          first_name.delete(0,20)
                          last_name.delete(0,20)
                          phone_number.delete(0,10)
                          email.delete(0,30)
                          passw.delete(0,20)
                 root1.destroy()
                 root=Tk()
                 root.title("Sign Up")
                 d=PhotoImage(file="airoplane.gif")
                 Label(root,image=d).grid(row=0,column=0,columnspan=4)
                 Label(root,text="Welcome to Airline Booking Systems",font=("Bauhaus 93",17),fg="Red",width=46,bg="White").grid(row=0,column=0,columnspan=4)
                 Label(root,text="Sign Up",font=("Bauhaus 93",17),fg="White",width=46,bg="red").grid(row=1,column=0,columnspan=4)
                 Label(root,text="Username*",font=("Bauhaus 93",14),fg="blue").grid(row=2,column=1)
                 user_name=Entry()
                 user_name.grid(row=2,column=2)
                 Label(root,text="First Name",font=("Bauhaus 93",14),fg="blue").grid(row=3,column=1)
                 first_name=Entry()
                 first_name.grid(row=3,column=2)
                 Label(root,text="Last Name",font=("Bauhaus 93",14),fg="blue").grid(row=4,column=1)
                 last_name=Entry()
                 last_name.grid(row=4,column=2)
                 Label(root,text="Phone Number",font=("Bauhaus 93",14),fg="blue").grid(row=5,column=1)
                 phone_number=Entry()
                 phone_number.grid(row=5,column=2)
                 Label(root,text="Email",font=("Bauhaus 93",14),fg="blue").grid(row=6,column=1)
                 email=Entry(width=30)
                 email.grid(row=6,column=2)
                 Label(root,text="Password*",font=("Bauhaus 93",14),fg="Blue").grid(row=7,column=1)
                 passw=Entry(root,show="*")
                 passw.grid(row=7,column=2)   
                 Button(root,text="Sign up",fg="white",bg="red",font=("algerian",10),command=lambda: success()).grid(row=8,columnspan=5)
                 def signin():
                     root.destroy()
                     root2=Tk()
                     root2.title("Sign In")
                     b=PhotoImage(file="airoplane.gif")
                     Label(root2,image=b).grid(row=0,column=0,columnspan=4)
                     Label(root2,text="Welcome to Airplane Booking System",font=("Bauhaus 93",17),fg="Red",width=46,bg="White").grid(row=0,column=0,columnspan=4)
                     Label(root2,text="Sign In",font=("Bauhaus 93",17),fg="White",width=46,bg="red").grid(row=1,column=0,columnspan=4)
                     Label(root2,text="Username*",font=("Bauhaus 93",14),fg="blue").grid(row=2,column=1)
                     user_name=Entry()
                     user_name.grid(row=2,column=2)
                     Label(root2,text="Password*",font=("Bauhaus 93",14),fg="Blue").grid(row=3,column=1)
                     passw=Entry(root2,show="*")
                     passw.grid(row=3,column=2)
                     def bookingportal():
                          usr = user_name.get()
                          passs = passw.get()
                          cur.execute("select * from airlines where user_name=(?) and passw=(?)", (usr, passs,))
                          a = cur.fetchall()
                          if a==[]:
                                   showerror('Log In Failed', "Invalid Username or Password")
                          else:
                                root2.destroy()
                                root4=Tk()
                                root4.title("Booking Portal")
                                Label(root4,text="Welcome to Airplane Booking System",font=("Bauhaus 93",17),fg="Red",width=46,bg="White").grid(row=0,column=0,columnspan=4)
                                Label(root4,text="Booking Portal",font=("Bauhaus 93",17),fg="White",width=46,bg="red").grid(row=1,column=0,columnspan=4)
                                Label(root4,text="Enter Your Details",font=("Bauhaus 93",14),fg="Blue",width=46).grid(row=2,column=0,columnspan=4)
                                Label(root4,text="Full Name",font=("Bauhaus 93",14),fg="blue").grid(row=3,column=1)
                                name=Entry()
                                name.grid(row=3,column=2)
                                Label(root4,text="Enter Your age",font=("Bauhaus 93",14),fg="Blue").grid(row=4,column=1)
                                age=Entry(width=4)
                                age.grid(row=4,column=2)
                                Label(root4,text="Select Gender",font=("Bauhaus 93",14),fg="blue").grid(row=5,column=1)
                                a=IntVar()
                                Radiobutton(root4,text="Male",variable=a,value=0,fg="red").grid(row=5,column=2)
                                Radiobutton(root4,text="Female",variable=a,value=1,fg="Pink").grid(row=5,column=3)
                                Label(root4,text="Seat Class",font=("Bauhaus 93",14),fg="blue").grid(row=6,column=1)
                                v= StringVar(root4)
                                v.set("Select class") # default value
                                w = OptionMenu(root4, v, "First Class", "Business Class", "Economy Class")
                                w.grid(row=6,column=2)
                                Label(root4,text="Additional Passengers Details",font=("Bauhaus 93",14),fg="Blue",width=46).grid(row=7,column=0,columnspan=4)
                                Label(root4,text="Passenger 1",font=("Bauhaus 93",14),fg="Blue").grid(row=8,column=1)
                                name1=Entry()
                                name1.grid(row=8,column=2)
                                Label(root4,text="Enter age",font=("Bauhaus 93",14),fg="Blue").grid(row=9,column=1)
                                age1=Entry(width=4)
                                age1.grid(row=9,column=2)
                                Label(root4,text="Seat Class",font=("Bauhaus 93",14),fg="blue").grid(row=10,column=1)
                                v1= StringVar(root4)
                                v1.set("Select class") # default value
                                w1 = OptionMenu(root4, v1, "First Class", "Business Class", "Economy Class")
                                w1.grid(row=10,column=2)
                                Label(root4,text="Passenger 2",font=("Bauhaus 93",14),fg="Blue").grid(row=11,column=1)
                                name2=Entry()
                                name2.grid(row=11,column=2)
                                Label(root4,text="Enter age",font=("Bauhaus 93",14),fg="Blue").grid(row=12,column=1)
                                age2=Entry(width=4)
                                age2.grid(row=12,column=2)
                                Label(root4,text="Seat Class",font=("Bauhaus 93",14),fg="blue").grid(row=13,column=1)
                                v2= StringVar(root4)
                                v2.set("Select class") # default value
                                w2 = OptionMenu(root4, v2, "First Class", "Business Class", "Economy Class")
                                w2.grid(row=13,column=2)
                                Label(root4,text="Passenger 3",font=("Bauhaus 93",14),fg="Blue").grid(row=14,column=1)
                                name3=Entry()
                                name3.grid(row=14,column=2)
                                Label(root4,text="Enter age",font=("Bauhaus 93",14),fg="Blue").grid(row=15,column=1)
                                age3=Entry(width=4)
                                age3.grid(row=15,column=2)
                                Label(root4,text="Seat Class",font=("Bauhaus 93",14),fg="blue").grid(row=16,column=1)
                                v3= StringVar(root4)
                                v3.set("Select class") # default value
                                w3 = OptionMenu(root4, v3, "First Class", "Business Class", "Economy Class")
                                w3.grid(row=16,column=2)
                                Label(root4, text="Journey Date:",font=("Bauhaus 93",14),fg="blue").grid(row=17,column=1)
                                date = Entry(root4, width=15, font=("Bauhaus 93", 14),fg="Blue")
                                date.grid(row=17, column=2)
                                date.insert(0,"DD/MM/YYYY")
                                Label(root4,text="Number of Passengers",font=("Bauhaus 93",14),fg="blue").grid(row=18,column=1)
                                v4= StringVar(root4)
                                v4.set("0") # default value
                                w4 = OptionMenu(root4, v4, "1", "2", "3","4")
                                w4.grid(row=18,column=2)
                                def data():
                                        root5=Tk()
                                        root5.title("Ticket Details")
                                        Label(root5,text="Thanks For Choosing Airplane Booking System",font=("Bauhaus 93",17),fg="White",bg="red",width=46).grid(row=0,column=0,columnspan=4)
                                        Label(root5,text="Ticket Details",font=("Bauhaus 93",17),fg="Blue",width=46).grid(row=1,column=0,columnspan=4)
                                        Label(root5,text="Passenger Name",font=("Arial",14),fg="Blue").grid(row=2,column=1)
                                        Label(root5,text=name.get(),font=("Arial",14),fg="Blue").grid(row=2,column=2)
                                        Label(root5,text="Age",font=("Arial",14),fg="Blue").grid(row=3,column=1)
                                        Label(root5,text=age.get(),font=("Arial",14),fg="Blue").grid(row=3,column=2)
                                        Label(root5,text="Gender",font=("Arial",14),fg="Blue").grid(row=4,column=1)
                                        if(a.get()==0):
                                                Label(root5,text="Male",font=("Arial",14),fg="Blue").grid(row=4,column=2)
                                        else:
                                                Label(root5,text="Female",font=("Arial",14),fg="Blue").grid(row=4,column=2)
                                        Label(root5,text="Class",font=("Arial",14),fg="Blue").grid(row=5,column=1)
                                        Label(root5,text=v.get(),font=("Arial",14),fg="Blue").grid(row=5,column=2)
                                        Label(root5,text="Date",font=("Arial",14),fg="Blue").grid(row=6,column=1)
                                        Label(root5,text=date.get(),font=("Arial",14),fg="Blue").grid(row=6,column=2)
                                        Label(root5,text="Additional Passenger Details",font=("Bauhaus 93",17),fg="Blue",width=46).grid(row=7,column=0,columnspan=4)
                                        Label(root5,text="Passenger Name",font=("Arial",14),fg="Blue").grid(row=8,column=1)
                                        Label(root5,text=name1.get(),font=("Arial",14),fg="Blue").grid(row=8,column=2)
                                        Label(root5,text="Class",font=("Arial",14),fg="Blue").grid(row=9,column=1)
                                        Label(root5,text=v1.get(),font=("Arial",14),fg="Blue").grid(row=9,column=2)
                                        Label(root5,text="Passenger Name",font=("Arial",14),fg="Blue").grid(row=10,column=1)
                                        Label(root5,text=name2.get(),font=("Arial",14),fg="Blue").grid(row=10,column=2)
                                        Label(root5,text="Class",font=("Arial",14),fg="Blue").grid(row=11,column=1)
                                        Label(root5,text=v2.get(),font=("Arial",14),fg="Blue").grid(row=11,column=2)
                                        Label(root5,text="Passenger Name",font=("Arial",14),fg="Blue").grid(row=12,column=1)
                                        Label(root5,text=name3.get(),font=("Arial",14),fg="Blue").grid(row=12,column=2)
                                        Label(root5,text="Class",font=("Arial",14),fg="Blue").grid(row=13,column=1)
                                        Label(root5,text=v3.get(),font=("Arial",14),fg="Blue").grid(row=13,column=2)
                                        Label(root5,text="Amount Per Passsenger",font=("Bauhaus 93",17),fg="Blue",width=46).grid(row=14,column=0,columnspan=4)
                                        Label(root5,text="Ticket From " + variable.get() + "<-> to <->" + variable1.get(),fg="White",bg="green",font=("LCD",10),width=46).grid(row=15,column=0,columnspan=4)
                                        def amount(price):
                                                
                                                if (int(v4.get())==1):
                                                     print (v.get())
                                                     if(v.get()=="First Class"):
                                                        price=10000
                                                        
                                                     elif (v.get()=="Business Class"):
                                                        price=6000
                                                     elif(v.get()=="Econoy Class"):
                                                        price=3800
                                                elif int(v4.get())==2:
                                                    if(v.get()=="First Class" and v1.get()=="First Class"):
                                                        price=20000
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class"):
                                                        price=16000
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class"):
                                                        price=13800
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class"):
                                                        price=16000
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class"):
                                                        price=12000
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class"):
                                                        price=9800
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class"):
                                                        price=13800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class"):
                                                        price=9800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class"):
                                                        price=7600
                                                elif (int(v4.get())==3):
                                                    if(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class"):
                                                        price=30000
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class"):
                                                        price=26000
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class"):
                                                         price=23800
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class"):
                                                        price=30000
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class"):
                                                        price=26000
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class"):
                                                         price=23800
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class"):
                                                        price=30000
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class"):
                                                        price=26000
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class"):
                                                         price=23800
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class"):
                                                        price=26000
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class"):
                                                        price=22000
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class"):
                                                         price=19800
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class"):
                                                        price=22000
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class"):
                                                         price=18000
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class"):
                                                         price=15800
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class"):
                                                         price=19800
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class"):
                                                        price=15800
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class"):
                                                         price=13600
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class"):
                                                        price=23800
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class"):
                                                        price=19800
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class"):
                                                         price=17600
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class"):
                                                        price=19800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class"):
                                                        price=15800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class"):
                                                         price=13600
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class"):
                                                        price=17600
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class"):
                                                        price=13600
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class"):
                                                         price=11400
                                                         Label(root5,text="Price",font=("Arial",14),fg="Blue").grid(row=16,column=1)
                                                         Label(root5,text=price,font=("Arial",14),fg="Blue").grid(row=16,column=2)
                                                         Label(root5,text="Total Amount",font=("Arial",14),fg="Blue").grid(row=18,column=1)
                                                         Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Blue").grid(row=18,column=2)
                                                elif (int(v4.get())==4):
                                                    if(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000 
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000 
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000 
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000 
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000 
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000 
                                                    elif(v.get()=="First Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000 
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000 
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000 
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000 
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000 
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000 
                                                    elif(v.get()=="First Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000 
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000 
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000 
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000 
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="First Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000 
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000 
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Business Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Business Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Business Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Economy Class" and v1.get()=="First Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Business Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="First Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Business Class" and v3.get()=="Economy Class"):
                                                        price=33800
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="First Class"):
                                                        price=40000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Business Class"):
                                                        price=36000
                                                    elif(v.get()=="Economy Class" and v1.get()=="Economy Class" and v2.get()=="Economy Class" and v3.get()=="Economy Class"):
                                                        price=33800 
                                                Label(root5,text="Price",font=("Arial",14),fg="Blue").grid(row=16,column=1)
                                                Label(root5,text=price,font=("Arial",14),fg="Blue").grid(row=16,column=2)
                                                Label(root5,text="Total Amount",font=("Arial",14),fg="Blue").grid(row=18,column=1)
                                                Label(root5,text=price*int(v4.get()),font=("Arial",14),fg="Blue").grid(row=18,column=2)
                                        Button(root5,text="Price",font=("algerian"),fg="white",bg="red",command=amount(0)).grid(row=20,columnspan=5)
                                        Label(root5,text="Number of Passengers",font=("Arial",14),fg="Blue").grid(row=17,column=1)
                                        Label(root5,text=v4.get(),font=("Arial",14),fg="Blue").grid(row=17,column=2)
                                        def exitw():
                                            root4.destroy()
                                            root5.destroy()
                                        Button(root5,text="Done",font=("algerian"),fg="white",bg="red",command=exitw).grid(row=19,columnspan=5)
                    
                    
                          Button(root4,text="Confirm Booking",fg="white",font=("algerian"),bg="red",command=data).grid(row=19,columnspan=5)
                     Button(root2,text="Sign In",fg="white",bg="red",font=("algerian",10),command=lambda: bookingportal()).grid(row=4,columnspan=5)
                 Button(root,text="Sign in",fg="white",bg="red",font=("algerian",10),command=signin).grid(row=9,columnspan=5)
                   
    def flights():
        if variable.get()=="Delhi" and variable1.get()=="Kolkata":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="100",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Delhi" and variable1.get()=="Mumbai":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="250",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Delhi" and variable1.get()=="U.S.A":
            showerror('Oops!',"Sorry No direct flights available for this root")
        if variable.get()=="Delhi" and variable1.get()=="Canada":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="201",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=4,columnspan=5,column=2)
        if variable.get()=="Kolkata" and variable1.get()=="Delhi":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="100",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Kolkata" and variable1.get()=="Mumbai":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="150",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Kolkata" and variable1.get()=="U.S.A":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="115",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Kolkata" and variable1.get()=="Canada":
            showerror('Oops!',"Sorry No direct flights available for this root")
        if variable.get()=="Mumbai" and variable1.get()=="Delhi":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="250",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Mumbai" and variable1.get()=="Kolkata":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="150",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Mumbai" and variable1.get()=="U.S.A":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="167",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Mumbai" and variable1.get()=="Canada":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="160",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="U.S.A" and variable1.get()=="Delhi":
            showerror('Oops!',"Sorry No direct flights available for this root")
        if variable.get()=="U.S.A" and variable1.get()=="Mumbai":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="167",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="U.S.A" and variable1.get()=="Kolkata":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="115",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="U.S.A" and variable1.get()=="Canada":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="168",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Canada" and variable1.get()=="Delhi":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="201",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Canada" and variable1.get()=="Mumbai":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="160",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        if variable.get()=="Canada" and variable1.get()=="Kolkata":
           showerror('Oops!',"Sorry No direct flights available for this root")
        if variable.get()=="Canada" and variable1.get()=="U.S.A":
            Label(root1,text="Number of Seats Available are:",font=("Bauhaus 93",14),fg="white",bg="orange").grid(row=5,columnspan=4)
            Label(root1,text="168",font=("Bauhaus 93",14),fg="white",bg="green").grid(row=5,columnspan=4,column=2)
        Button(root1,text="Signup to Book",fg="white",bg="orange",font=("algerian",10),command=signup).grid(row=7,columnspan=5)  
    Button(root1,text="Show Flights",font=("algerian",10),fg="white",bg="Orange",compound="center",command=flights).grid(row=6,columnspan=1)
    root1.mainloop()
Button(fr2,text="Proceed to Project",compound="center",bg="Yellow",font=("algerian"),fg="blue",command=airline).pack()
root.mainloop()
