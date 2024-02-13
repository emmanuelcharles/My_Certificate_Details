from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from datetime import datetime

connect = MongoClient("localhost",27017)
db_n = connect.project_db_test
coll_n = db_n.Sample01
coll_l = db_n.log_test
############################################################ Operation 04_1

def search_oper_4_1():
    found = 0
    a = search_04_1_e2.get()
    for i in coll_n.find({},{'_id':0, 'id':1 }):
        if a == str(i['id']):
            found += 1

    if found > 0:
        for i in coll_n.find({},{'_id':0}):
            a = str(i['Certificate'])
            b = str(i['id'])
            c = str(i['Date'])
            c1 = str(i['Month'])
            c2 = str(i['Year'])
            d = str(i['Mode'])
            e = str(i['More Details'])
        messagebox.showinfo(title="Details", message=a+", "+b+", "+c+c1+c2+" "+d+", "+e)
    else:
        messagebox.showinfo(title="Error", message = "Id not match.." )

def search_clr_oper_4_1():
    a = str(search_04_1_e2.get())
    if len(a)>0:
        search_04_1_e2.delete(0,END)

def Operation_04_1():
    global search_04_1_e2
    win_search = Tk()
    win_search.title("Search Details")
    win_search.geometry("450x400+450+150")
    win_search.config(background="white")

    search_04_1_l1 = Label(win_search, text='Search Details', bg = 'white', font=('serif', 25 , 'bold'))

    search_04_1_l2 = Label(win_search , text='Enter the ID :', bg = 'white', font=('serif', 10, 'bold'))
    search_04_1_e2 = Entry(win_search , width = 49, bg = 'white')

    search_04_1_b1 = Button(win_search, text="Search" , width = 25, height = 3, font=('serif', 9 ,'bold'), command = search_oper_4_1)
    search_04_1_b2 = Button(win_search, text="Clear" , width =25 , height = 3, font=('serif', 9 ,'bold'), command = search_clr_oper_4_1)

    search_04_1_l1.place(x = 115 , y = 35)
    search_04_1_l2.place(x = 20 , y = 150)
    search_04_1_e2.place(x = 120 , y = 150)

    search_04_1_b1.place(x = 25 , y = 250)
    search_04_1_b2.place(x = 235 , y = 250)

                       
    win_search.mainloop()

############################################################ Operation 04_2

def Operation_04_2():
    Oper_04_1_y1 = 70
    w1 = Tk()
    for  i in coll_n.find({},{"_id" : 0}):
        a = str(i['id'])
        b = str(i['Mode'].encode('utf-8').decode('utf-8'))
        c = (str(i['Date'])+" "+str(i['Month'])+" "+str(i['Year']))
        d = str(i['Certificate'].encode('utf-8').decode('utf-8'))
        e = str(i['More Details'].encode('utf-8').decode('utf-8'))

        la = Label(w1, text = a, font=('serif', 10), bg ='white')
        lb = Label(w1, text = b, font=('serif', 10), bg ='white')
        lc = Label(w1, text = c, font=('serif', 10), bg ='white')
        ld = Label(w1, text = d, font=('serif', 10), bg='white')
        le = Label(w1, text = e, font=('serif', 10), bg ='white')

        la.place(x= 25 , y = Oper_04_1_y1)
        lb.place(x= 135 , y = Oper_04_1_y1)
        lc.place(x= 200, y = Oper_04_1_y1)
        ld.place(x = 370 , y = Oper_04_1_y1)
        le.place(x = 510 , y = Oper_04_1_y1)
        Oper_04_1_y1+=25
    w1.title("Certificate details")
    w1.geometry("1050x380+200+220")
    w1.resizable(width="false", height="false")
    w1.config(background="white")
    
    l1 = Label(w1, text="ID", bg = "white", fg ="red", font=('serif', 15, 'bold'))
    l2 = Label(w1, text="Mode", bg = "white", fg ='red', font=('serif', 15 , 'bold'))
    l3 = Label(w1, text="Completed Date", bg = "white", fg ="red", font=('serif', 15, 'bold'))
    l4 = Label(w1, text="Certificate" , bg = 'white', fg = 'red', font=('serif', 15, 'bold'))
    l5 = Label(w1, text="More Details" , bg = 'white', fg = 'red', font=('serif', 15, 'bold'))

    l1.place(x = 60 , y = 20)
    l2.place(x = 130 , y = 20)
    l3.place(x = 200 , y = 20)
    l4.place(x = 370 , y = 20)
    l5.place(x = 520 , y = 20)

    w1.mainloop()


############################################################ Operation 04
def view_option_01():
    view_option_win = Tk()
    view_option_win.geometry("360x380+520+200")
    view_option_win.title("View Details")
    view_option_win.config(background ="white")
    view_option_win.resizable(width = 'false' , height = 'false')

    b1 = Button(view_option_win, text = 'Search' , width = 30 , height = 3, font=('serif', 10 ), command = Operation_04_1 )
    b2 = Button(view_option_win, text = 'View All Details' , width = 30 , height = 3, font=('serif', 10 ), command = Operation_04_2)

    b1.place(x = 55 , y = 100)
    b2.place(x = 55 , y = 200)

    view_option_win.mainloop()


############################################################ Operation 02

def Up_oper():
    a = str(Up_e1.get())
    b = str(Up_e2.get())
    c = Up_e3.get()
    up_found =0
    
    for i in coll_n.find({},{'_id' : 0, 'id' :1}):
        if a == str(i['id']):
            up_found +=1
        
    if up_found > 0:
        coll_n.update_one({'id' :a}, {'$set':{b : c}})
        messagebox.showinfo(title="Updated", message="Updated successfully")
    else:
        messagebox.showinfo(title="Error", message="You id"+a+" is not match.")
    
def Up_clear():
    a = Up_e1.get()
    b = Up_e2.get()
    c = Up_e3.get()

    if len(a)>0 or len(b)>0 or len(c)>0:
        Up_e1.delete(0 , END)
        Up_e2.delete(0 , END)
        Up_e3.delete(0 , END)
                    
def oper_02():
    global Up_e1
    global Up_e2
    global Up_e3
    
    win_up = Tk()
    win_up. geometry("490x600+500+70")
    win_up.config(background = "white")
    win_up.title("Update details")
    win_up.resizable(width = "false", height="false")
    l1 = Label(win_up, text="Update your Details", font=('serif', 23 , 'bold'), bg = 'white', fg = 'black')

    Up_l1 = Label(win_up, text = "Enter the ID", font=('serif', 10, 'bold' ), bg= 'white', fg = 'black')
    Up_l2 = Label(win_up, text = "Select the field", font=('serif', 10 ,'bold'), bg= 'white', fg= 'black')
    Up_l3 = Label(win_up, text = "Update the data", font=('serif', 10 , 'bold'), bg = 'white', fg = 'black') 

    Up_e1 = Entry(win_up, width = 40, bg = 'white' , fg = 'black' ) 
    Up_e3 = Entry(win_up, width = 40 , bg = 'white', fg = 'black')
    Up_e2 = ttk.Combobox(win_up, width = 37, values =['Certificate', 'Date', 'Month', 'Year', 'Mode'])

    Up_b1 = Button(win_up, text="Submit", width = 25, height = 2 , font=('serif',10, 'bold'), bg = 'black' , fg = 'white', command = Up_oper)
    Up_b2 = Button(win_up, text="Clear", width = 25, height = 2 , font=('serif',10, 'bold'), bg = 'black' , fg = 'white', command = Up_clear)

    l1.place(x= 90 , y = 40)

    Up_l1.place(x = 40 , y = 150)
    Up_l2.place(x = 40 , y = 230)
    Up_l3.place(x = 40 , y = 310)

    Up_e1.place(x = 170 , y = 150)
    Up_e2.place(x = 170 , y = 230)
    Up_e3.place(x = 170 , y = 310)

    Up_b1.place(x = 30 , y = 430)
    Up_b2.place(x = 250 , y = 430)
    win_up.mainloop()


############################################################ Operation 01

def add_clear():
    a = ADD_e1.get()
    b = ADD_e2.get()
    d = ADD_e4.get(0.1, END)
    f = ADD_e22.get()

    if len(a)>0 or len(b)>0 or len(d)>0 or len(f)>0:
        ADD_e1.delete(0, END)
        ADD_e2.delete(0, END)
        ADD_e21.delete(0, END)
        ADD_e22.delete(0, END)
        ADD_e3.delete(0, END)
        ADD_e4.delete(0.1, END)
        
def add_details():
    a = ADD_e1.get()
    b = ADD_e2.get()
    c = ADD_e3.get()
    d = ADD_e4.get(0.1 , END)
    e = ADD_e21.get()
    f = ADD_e22.get()

    t = datetime.now()
    td = str(t.day)
    tm = str(t.month)
    ty = str(t.year)
    th = str(t.hour)
    tmi = str(t.minute)
    ts = str(t.second)

    check = str(th+ty+tmi+tm+ts+td)
    print(check)
    
    addfind = 0
    if len(a)<0 or len(b)<0 or len(c)<0 or len(d)<0 or len(e)<0 or len(f)<0:
        messagebox.showinfo(title ="Error", message="Please fill the form")
    else:
        for i in coll_n.find({},{'_id' : 0, 'id':1}):
            if check == str(i['id']):
                print("id found")
                addfind += 1

    if addfind == 0:
        coll_n.insert_one({'id' : check, 'Certificate' : a , 'Date' : b, 'Month' :e, 'Year': f, 'Mode': c , 'More Details' : d})
        messagebox.showinfo(title = "Message", message = "Your new details is inserted")
    else:
        messagebox.showinfo(title ="Message" , message = "Sorry your id alread exist...")
        
               
def oper_01():
    wadd = Tk()
    wadd.title("Add new details")
    wadd.geometry("490x640+500+70")
    wadd.config(background="white")
    wadd.resizable(width="false", height="false")

    l1 = Label(wadd, text="Add New Details", font=("serif", 28, "bold"), bg="white", fg="black")
    l2 = Label(wadd, text="Enter the completion date below", font= ("serif", 10), bg = "white", fg ="red")

    el1 = Label(wadd, text="Certificate Name", font=("serif", 10), bg="white")
    el2 = Label(wadd, text="Date", font=("serif", 10), bg="white")
    el21 = Label(wadd, text="Month", font=("serif", 10), bg="white")
    el22 = Label(wadd, text="Year", font=("serif", 10), bg="white")
    el3 = Label(wadd, text="Mode", font=("serif", 10), bg="white")
    el4 = Label(wadd, text="More details", font=("serif", 10), bg="white")

    global ADD_e1, ADD_e2, ADD_e21, ADD_e22, ADD_e3, ADD_e4
    
    ADD_e1 = Entry(wadd, width= 45, bg="white")
    ADD_e2 = Entry(wadd, width = 45, bg = "white")
    ADD_e21 = ttk.Combobox(wadd , width = 42 ,
                           values=['January', 'February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December' ])   
    ADD_e22 = Entry(wadd , width = 45 , bg ="white")
    ADD_e3 = ttk.Combobox(wadd, values=['Online', 'Offline'], width=42)
    ADD_e4 = Text(wadd, width= 34, height= 6, bg="white")

    b1 = Button(wadd, text="Submit", font=('serif', 10), width = 20 , height= 2, bg="black", fg='white' ,command = add_details )
    b2 = Button(wadd, text="Clear", font=('serif', 10), command= add_clear, width = 20 , height= 2, bg="black", fg='white')
    l1.place(x = 100 , y = 40)
    l2.place( x= 150 , y = 170)

    el1.place(x= 25 , y = 130)
    el2.place(x= 25 , y = 220)
    el21.place(x= 25 , y = 260)
    el22.place(x= 25 , y = 305)
    el3.place(x= 25 , y = 350)
    el4.place(x= 25 , y = 395)

    ADD_e1.place(x= 150, y = 130)
    ADD_e2.place(x= 150, y = 220)
    ADD_e21.place(x = 150 , y = 260)
    ADD_e22.place(x= 150 , y = 305)
    ADD_e3.place(x= 150, y = 350)
    ADD_e4.place(x= 150, y = 395)

    b1.place(x= 60 , y = 530)
    b2.place(x= 250 , y = 530)

    wadd.mainloop()


################################################################### Operation 03

def op_03_clear():
    a = dele1.get()
    if len(a)>0:
        dele1.delete(0, END)

def op_03_check():
    a = str(dele1.get())
    f = 0
    for i in coll_n.find({},{'id' : 1}):
        if (a == str(i['id']).encode('utf-8').decode('utf-8')):
            f+=1
            #print(str(i['id']).encode('utf-8').decode('utf-8'))
    if(f == 1):
        messagebox.showinfo(title = "Successfully Executed", message = "ID "+a+" is found successfully...")
    else:
        messagebox.showinfo(title = "Warning", message = "ID "+a+" is not matched...")

def op_03_del():
    a = str(dele1.get())
    f = 0
    coll_n.delete_one({'id' : a})        
    for i in coll_n.find({},{'id' : 1}):
        if (a == str(i['id']).encode('utf-8').decode('utf-8')):
            f+=1
            #print(str(i['id']).encode('utf-8').decode('utf-8'))            
    if(f == 0):
        messagebox.showinfo(title = "Message", message = "ID "+a+" is deleted successfully...")
    else:
        messagebox.showinfo(title = "Warning", message = "ID "+a+" is not deleted try again...")

def oper_03():
    global dele1
    windel = Tk()
    windel.title("Delete operation")
    windel.geometry("720x350+390+190")
    windel.resizable(width = "false", height = "false")
    windel.config(background="white")

    l1 = Label(windel,text="Delete Details", font=("san-serif",30, "bold"), bg="white")
    l2 = Label(windel, text="Enter the ID", font=("san-serif",10, 'bold'), bg="white")

    dele1 = Entry(windel , width = 85, bg= "white")

    b1 = Button(windel , text="Delete", width = 25, height = 3, command = op_03_del)
    b2 = Button(windel , text="Search", width = 25, height = 3, command = op_03_check)
    b3 = Button(windel , text="Clear", width = 25, height = 3, command = op_03_clear)

    l1.place(x= 230 , y = 20)
    l2.place(x= 60 , y = 120)

    dele1. place(x = 150 , y = 120)

    b1.place(x= 50 , y = 200)
    b2.place(x= 270 , y = 200)
    b3.place(x= 490 , y = 200)

    windel.mainloop()

####################################################################### admin 

def view_admin():

    tcount = 0
    oncount = 0
    offcount = 0
    for i in coll_n.find({}):
        tcount +=1
    for i in coll_n.find({'Mode' : 'Online'}):
        oncount +=1
    for i in coll_n.find({'Mode' : 'Offline'}):
        offcount +=1

    window = Tk()
    window.geometry("800x450+390+200")
    window.title("My Certification Details")
    window.config(background="white")
    window.resizable(width= "false", height = "false")

    b1 = Button(window, text="Add New Details", width = 25, height = 3 , command = oper_01)
    b2 = Button(window, text="Update Details", width = 25, height = 3, command = oper_02)
    b3 = Button(window, text="Delete Details", width = 25, height = 3 , command = oper_03)
    b4 = Button(window, text="View Details", width = 25, height = 3, command = view_option_01)

    l1 = Label(window, text= tcount, font=("serif", 80, "bold"), bg= "white", fg = "red")
    l2 = Label(window, text="Total certificate earned:", font=("serif",11), fg="black", bg="white")
    l4 = Label(window, text= oncount, font=("serif", 50), bg= "white", fg = "black")
    l5 = Label(window, text="Online Certificates", font=("serif", 14), bg= "white", fg = "black")
    l6 = Label(window, text= offcount, font=("serif", 50), bg= "white", fg = "black")
    l7 = Label(window, text="Other Certificates", font=("serif", 14), bg= "white", fg = "black")
 
    b1.place(x=20 , y = 30)
    b2.place(x=210 , y = 30)
    b3.place(x=400 , y = 30)
    b4.place(x=590, y = 30)

    l1.place(x= 140 , y = 200)
    l2.place(x= 100 , y = 180)
    l4.place(x= 570, y = 145)
    l5.place(x = 395, y = 170)
    l6.place(x = 570, y = 270)
    l7.place(x = 395, y = 290)
    window.mainloop()
    
    
######################################################################## main           
def view():
    vw = Tk()
    vw.title("Certificate details")
    vw.geometry("820x450+360+180")
    vw.config(background="white")
    vw.resizable('true', 'false') 

    h1 = Label(vw, text="Certification Details", bg="white", fg="orange", font="serif 30 bold")
    h1.place(x= 240 , y = 30)
    y_ax = 105
    for i in coll_n.find({},{'_id':0}):
        l1 = Label(vw,text = i, bg = 'white', font='Serif 9')
        l1.place(x = 20 , y = y_ax)
        y_ax+=25
    vw.mainloop()

def check():
    us1 = usE.get()
    pass1 = passE.get()
    usf =0
    passf =0
    if len(us1) == 0 or len(pass1) == 0:
        messagebox.showinfo(title="Message", message="Please fill the username and password...")
    else:
        print(us1 +" "+ pass1)
        for i in coll_l.find({},{'_id':0, 'user': 1}):
            a = str(i['user'].encode('utf-8').decode('utf-8'))
            if a == us1:
                usf += 1
        for i in coll_l.find({},{'_id':0, 'password': 1}):
            b = str(i['password'].encode('utf-8').decode('utf-8'))
            if b == pass1:
                passf += 1
        if usf > 0 and passf > 0:
            print("successfully executed")
            view_admin()
        else:
            print("try again")

def log_clear():
    a = usE.get()
    b = passE.get()
    if len(a)>0 | len(b)>0:
        usE.delete(0, END)
        passE.delete(0, END)
            
def log():
    global usE, passE
    w2 = Tk()
    w2.title("Login")
    w2.geometry("410x340+500+190")
    w2.resizable(False, False)
    w2.config(background="white")
    f1 = Frame(w2, background = "white")
    ml = Label(w2,
               text= "Login",
               font ="Serif 27 bold",
               bg="white"
               )
               
    usl = Label(w2,text="Username",
               font ="Serif 9",
                bg="white"
               )
    passl = Label(w2,text="Password",
               font ="Serif 9",
                  bg="white"
               )
    usE = Entry(w2,
                font="Serif 9",
                bg="white"
                )
    passE = Entry(w2,
                font="Serif 9",
                show = "*",
                bg="white"
                )
    okB = Button(w2,
                 text="Submit",
                 font="Serif 9",
                 state = "active",
                 bg="white",
                 activebackground ="white",
                 width = 10,
                 command = check
                 )
    clB = Button(w2,
                 text="Clear",
                 font="Serif 9",
                 state = "active",
                 width = 10,
                 bg="white",
                 activebackground ="white",
                 command = log_clear
                 )
    gtext = Label(f1, text="If you don't have account click the below button", font="Serif 8 bold", fg="red", bg="white")
    
    guestB = Button(f1, text="Guest", font="Serif 9 bold", state = "active", bg= "white", activebackground= "white", width = 18, pady = 5, command= view)
    
    
    ml.place(x = 150 , y = 10)
    usl.place(x = 60 , y = 90)
    usE.place(x = 150 , y = 90)
    passl.place(x = 60 , y = 130)
    passE.place(x = 150 , y = 130)
    okB.place(x = 135 , y = 180)
    clB.place(x = 220 , y = 180)
    f1.place(x = 70 , y = 240)
    gtext.pack()
    guestB.pack()
    w1.destroy()


w1 = Tk()
w1.geometry("620x380+500+190")
w1.resizable(False, False)
w1.title("My certification details")
w1.config(background ="white")
l1= Label(text="Welcome to Certification Details", bg="white", fg="black", font = "Serif 23 bold")
l2= Label(text="Click the below button to start", bg="white", fg= "indigo", font="Serif 10")
b1 = Button(w1, text ="Click here", state = "active", bg = "black", fg = "white", activebackground = "black", activeforeground = "white",
        padx =20, pady = 3, font = "Serif 12 bold",command = log)
b1.place(x=250, y= 214)
l1.place(x=75 ,y=124,)
l2.place(x =225 , y=174)

w1.mainloop()
    


