from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import pymysql
import datetime
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
connection = pymysql.connect(host='localhost',user='root',passwd='kumawat',db='reg_python')
cursor=connection.cursor()

def registration():

    def update_submittion(root):
        def radio_update(rudata):
            return rudata

        def update(upi):
            rudata1=radio_update(var.get())
            if rudata1==1:
                now = datetime.datetime.now()
                current_date=now.strftime("%Y-%m-%d")
                cursor.execute("update submittion_details set Confirmed='Yes',Date_Of_Confirmation='%s' where upi='%s'"%(current_date,upi))
                connection.commit()
                Label(root,text="Update successfullY").place(x=500,y=210)
                update_submittion(root)
            
        def search(upi,root):
            cursor.execute("select Full_name ,clgid,Branch,payment_option,Amount from submittion_details where upi=%s",(upi))
            data=cursor.fetchall()
            if len(data)!=0:
                Label(root,text=" ",width=30).place(x=650,y=50)
                count=150
                for i in range(5):
                    count=count+150
                    Label(root,text=data[0][i],width=20).place(x=count,y=120)
                Radiobutton(root, text="Yes", variable=var ,value=1,command=lambda:(radio_update(var.get()))).place(x=1070,y=120)
                Radiobutton(root, text="No", variable=var ,value=2,command=lambda:(radio_update(var.get()))).place(x=1150,y=120)
            else:
                Label(root,text="Data Not found try again",fg='red').place(x=650,y=50)
            
        #root.destroy()
        root=Tk()
        root.state('zoomed')
        Label(root,text="Enter Transaction Id/Challan No",bg='silver').place(x=150,y=50)
        e=Entry(root,width=30)
        e.place(x=330,y=50)
        Button(root,text="Search",width=15,bg="silver",command=lambda:(search(e.get(),root))).place(x=510,y=50)
        list=['S No','Name','College Id','Branch','Payment Type','Amount','Confirm']
        count=0
        for i in list:
            count=count+150
            Label(root,text=i,width=20,bg='silver').place(x=count,y=100)
            w = Canvas(root, width=145, height=60)
            w.place(x=count,y=135)
            canvas_height=20
            canvas_width=200
            y = int(canvas_height / 2)
            w.create_line(0, y, canvas_width, y )
        list1=[1,'Rakesh','2016ucs033','c s','online payment',35550]
        var=IntVar()
        Radiobutton(root, text="Yes", variable=var ,value=1).place(x=1070,y=120)
        Radiobutton(root, text="No", variable=var ,value=2).place(x=1150,y=120)
        count=0
        for i in list1:
            count=count+150
            Label(root,text=i,width=20).place(x=count,y=120)
        Button(root,text="Update",width=20,command=lambda:(update(e.get()))).place(x=500,y=180)
        Button(root,text="Exit",width=20,command=quit).place(x=220,y=500)
        Button(root,text="Back",width=20,command=lambda:(adm_button(root))).place(x=370,y=500)
        root.mainloop()

    def adm_button():
        #root.destroy()
        root=Tk()
        root.state('zoomed')
        Label(root,text="Total Number of Students >>>>> 195",bg='yellow', font=("Helvetica", 15)).place(x=10,y=10)
        dept=['C S ','M E ','I T ','C E ','E E ','E C ']
        count=450
        for i in dept:
            count=count+50
            Label(root,text=i).place(x=count,y=10)
        totallist=[ 35 , 50 , 8 , 60 , 37 , 5 ]
        count=450
        for i in totallist:
            count=count+50
            Label(root,text=i).place(x=count,y=30)
        cursor.execute("select clgid  from submittion_details where Confirmed='yes'")
        rdstudents=cursor.fetchall()
        Label(root,text="Total Number of Registered Students>>>>> "+str(len(rdstudents)), font=("Helvetica", 15)).place(x=10,y=80)
        count=450
        for i in dept:
            count=count+50
            Label(root,text=i).place(x=count,y=80)
        count=450
        reglist=[ 5 , 5 , 5 , 5 , 5 , 5 ]
        for i in reglist:
            count=count+50
            Label(root,text=i).place(x=count,y=100)
        cursor.execute("select upi from submittion_details")
        reg=cursor.fetchall()
        Label(root,text="Panding Submitton >>>>> "+str(len(reg)-len(rdstudents)), font=("Helvetica", 15)).place(x=10,y=150)
        count=450
        for i in dept:
            count=count+50
            Label(root,text=i).place(x=count,y=150)
        panlist=[ 10 , 10 , 0 , 10 , 10 , 0 ]
        count=450
        for i in panlist:
            count=count+50
            Label(root,text=i).place(x=count,y=170)
        Label(root,text='Remaning Students Who are not fill registration form',font=('Helvetica',15)).place(x=10,y=220)
        count=450
        for i in dept:
            count=count+50
            Label(root,text=i).place(x=count,y=220)
        count=450
        total,total1,total2=(totallist[0]-(reglist[0]+panlist[0])),(totallist[1]-(reglist[1]+panlist[1])),(totallist[2]-(reglist[2]+panlist[2]))
        total3,total4,total5=(totallist[3]-(reglist[3]+panlist[3])),(totallist[4]-(reglist[4]+panlist[4])),(totallist[5]-(reglist[5]+panlist[5]))
        remlist=[ total , total1 , total2 , total3 , total4 , total5 ]
        for i in remlist:
            count=count+50
            Label(root,text=i).place(x=count,y=240) 
        Button(root,text="Update Submittion", height = 2,width=20,bg='gold',command=lambda:(update_submittion(root))).place(x=650,y=500)
        Button(root,text="Exit", height = 2,width=20,bg='gold',command=quit).place(x=250,y=500)
        Button(root,text="Back", height = 2,width=20,bg='gold',command=lambda:(root.destroy(),registration())).place(x=450,y=500)
        root.mainloop()
    def open_img(frame):
        filename = filedialog.askopenfilename(title='open')
        img = Image.open(filename)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(frame, image=img)
        panel.image = img
        panel.place(x=1000,y=190)

    def open_sig(frame1):
        filename = filedialog.askopenfilename(title='open')
        img = Image.open(filename)
        img = img.resize((120, 40), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(frame1, image=img)
        panel.image = img
        panel.place(x=930,y=450)

    def put_data_for_reg_next(root,rdata1,rdata2,d1,data1,data6,data10,data12,data18,data25,payment):
        if len(rdata1)!=0:
            if all(x.isdigit() or x=="." for x in rdata2) and len(rdata2)!=0:
                Label(root,text=" ",width=20,bg='#ff6600').place(x=900,y=143)
                submit_process(root,rdata1,data1,data6,data10,data12,data18,data25,payment)                                                                                            
            else:
                d1.delete(0,END)
                Label(root,text="Insert Rs in form 00000.00",fg='red',bg='#ff6600').place(x=900,y=143)

    def return_home(frame1):#For destroy last frame and going into main frame.
        frame1.destroy()
        registration()

    def submit_process(root,rdata1,data01,data6,data10,data12,data18,data25,payment):
        #data12=str(data12)
        root.destroy()
        frame1=Tk()  
        frame1.state('zoomed')#For full screen
        data6=str(data6)#Convert data into string 
        data18=str(data18)
        dataa25=str(data25)
        rdata1=str(rdata1)
        cursor.execute("insert into submittion_details(Contact_No,Full_name,Branch,clgid,Upi,Amount,Date_Of_Submittion,payment_option\
            ) value('%s','%s','%s','%s','%s','%s','%s','%s')"%(data6,data01,data10,data12,data18,data25,rdata1,payment))
        connection.commit()#Update data status into table .
        cursor.execute('select MAX(codsubid) from submittion_details')#Searching Max element into table for generating sequence Id.
        sid=cursor.fetchall()
        sid=int(sid[0][0]+1)
        uid='18GECJR'+str(sid)
        subid1=str(data01)+"Your Submittion ID="+ str(uid)
        Label(frame1,text=subid1,font = "Helvetica 25 bold italic").place(x=350,y=70)
        Label(frame1,text="You have to Wait for submittion ,When your amount is recived\n  you get a submittion message from your college .",fg='red',font ="Helvetica 18 bold italic").place(x=310,y=170)
        cursor.execute("update submittion_details set submittionid='%s' ,codsubid='%s' where clgid='%s'"%(uid,sid,data12))
        Button(frame1,text="Exit",width=15,bg='silver',command=quit).place(x=550,y=350)
        Button(frame1,text="Return Home",width=20,bg='silver',command=lambda:return_home(frame1)).place(x=700,y=350)
        connection.commit()
        frame1.mainloop()

    def reg_next(root,data1,data6,data10,data12,data18,data25,payment):
        root.destroy()
        root=Tk()
        root.state('zoomed')
        root.configure(background="#ff6600")
        Label(root,text="Government Engineering College Jhalawar ",width=95,fg = "yellow",bg = "blue",font = "Helvetica 25 bold italic").pack()
        cursor.execute(('select undertaking from about_college;'))
        data3=cursor.fetchall()
        Label(root,text="DECLARATION & UNDERTAKING BY THE STUDENT",bg="#ff6600",font = "Helvetica 16 bold italic").pack()
        Label(root,text=data3[0][0],font = "Helvetica 14 bold italic",bg="#ff6600").pack()
        Label(root,text="By Challan/Receipt No",bg="#ff6600",font = "Helvetica 12 bold italic").place(x=220,y=143)
        Label(root,text="Date",bg="#ff6600",font = "Helvetica 12 bold italic").place(x=550,y=143)
        Label(root,text="Rs",bg="#ff6600",font = "Helvetica 12 bold italic").place(x=720,y=143)
        Label(root,text="SIGNATURE OF STUDENT WITH DATE ",bg="#ff6600",font = "Helvetica 14 bold italic").place(x=550,y=450)
        Button(root, text='Update signature',width="15", command=lambda:open_sig(root)).place(x=930,y=500)
        ee14=Entry( root,width=17,bd=3).place(x=435,y=143)
        date= DateEntry(root, width=12, background='darkblue',foreground='white', borderwidth=2)
        date.place(x=610,y=143)
        ee1=Entry( root,width=17,bd=3)
        ee1.place(x=750,y=143)
        Button(root,text="Submit",width=15,bg="red",fg="blue",command=lambda  : put_data_for_reg_next(root,date.get(),ee1.get(),\
            ee1,data1,data6,data10,data12,data18,data25,payment)).place(x=800,y=550)
        
        root.mainloop()

    def payment_label(root,payment):
        if len(payment)!=6:
            Label(root,text=" ",width=30,bg="silver", font=("Helvetica", 7)).place(x=220,y=490)
            if len(payment)==4:
                Label(root,text="Enter challen Number:",width=25).place(x=430,y=470)
            elif len(payment)==2:
                Label(root,text="Enter DD Number",width=25).place(x=430,y=470)
            elif len(payment)==14:
                Label(root,text="Enter Transaction Id",width=25).place(x=430,y=470)
            elif len(payment)==5:
                Label(root,text="Enter Transaction proof",width=25).place(x=430,y=470)
        else:
            Label(root,text="Select payment option",fg='red',bg="silver", font=("Helvetica", 7)).place(x=220,y=490)


    def check_and_put_data_for_reg(data111,root,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,\
        data14,data15,data16,data17,payment,data18,data19,data20,data21,data22,data23,data24,data25,d1,d2,d3,d4,d6,d7,d12,d13,d14,\
        d15,d16,d17,d18,d20,d21,d22,d23,d24,d25):
        if all(x.isalpha() for x in data1) and len(data1)!=0:#for first name
            Label(root,text=" ",width=45,bg="silver", font=("Helvetica", 7)).place(x=220,y=172)
            if all(x.isalpha() for x in data2) and len(data2)!=0:#for last name
                Label(root,text=" ",width=45,bg="silver", font=("Helvetica", 7)).place(x=620,y=172)
                if all(x.isalpha() or x.isspace() for x in data3) and len(data3)!=0:#for f name
                    Label(root,text=" ",width=45,bg="silver", font=("Helvetica", 7)).place(x=220,y=212)
                    if all(x.isalpha() or x.isspace() for x in data4) and len(data4)!=0:#for m Name
                        Label(root,text=" ",width=45,bg="silver", font=("Helvetica", 7)).place(x=620,y=212)
                        if len(data5)!=0:#for dob
                            Label(root,text=" ",width=20,bg="silver", font=("Helvetica", 7)).place(x=220,y=252)
                            print(data5)
                            if all(x.isdigit() for x in data6) and len(data6)!=0 and len(data6)==10:
                                Label(root,text=" ",width=25,bg="silver", font=("Helvetica", 7)).place(x=450,y=252)
                                if all(x.isdigit() for x in data7) and len(data7)!=0 and len(data7)==10:
                                    Label(root,text=" ",width=25,bg="silver", font=("Helvetica", 7)).place(x=735,y=252)
                                    if len(data8)!=6:
                                        Label(root,text=" ",width=15,bg="silver", font=("Helvetica", 7)).place(x=220,y=292)
                                        if len(data9)!=6:
                                            Label(root,text=" ",width=12,bg="silver", font=("Helvetica", 7)).place(x=380,y=292)
                                            if len(data10)!=6:
                                                Label(root,text=" ",width=15,bg="silver", font=("Helvetica", 7)).place(x=510,y=292)
                                                if len(data11)!=6:
                                                    Label(root,text=" ",width=15,bg="silver", font=("Helvetica", 7)).place(x=810,y=292)
                                                    if len(data12)==10:
                                                        Label(root,text=" ",width=15,bg="silver", font=("Helvetica", 7)).place(x=220 ,y=332)
                                                        if len(data13)==10:
                                                            Label(root,text=" ",width=25,bg="silver", font=("Helvetica", 7)).place(x=440 ,y=332)
                                                            if len(data14)==15:
                                                                Label(root,text=" ",width=25,bg="silver", font=("Helvetica", 7)).place(x=730,y=332)
                                                                if len(data15)!=0:
                                                                    Label(root,text=" ",width=70,bg="silver", font=("Helvetica", 7)).place(x=440,y=372)
                                                                    if len(data16)!=0:
                                                                        Label(root,text=" ",width=70,bg="silver", font=("Helvetica", 7)).place(x=390,y=412)
                                                                        if len(data17)!=0:
                                                                            Label(root,text=" ",width=70,bg="silver", font=("Helvetica", 7)).place(x=520,y=452)
                                                                            
                                                                            if len(data18)!=0:
                                                                                Label(root,text=" ",width=30,bg="silver", font=("Helvetica", 7)).place(x=700,y=492)
                                                                        
                                                                                if len(data19)!=6:
                                                                                    Label(root,text=" ",width=15,bg="silver", font=("Helvetica", 7)).place(x=745,y=532)
                                                                                    if "@gmail.com" in data20 and len(data20)!=0 and len(data20)!=10:
                                                                                        Label(root,text=" ",width=37,bg="silver", font=("Helvetica", 7)).place(x=220,y=572)
                                                                                        if all(x.isalpha() or x.isspace() for x in data21 ) and len(data21)!=0:
                                                                                            Label(root,text=" ",width=19,bg="silver", font=("Helvetica", 7)).place(x=560,y=572)
                                                                                            if len(data22)!=0:
                                                                                                Label(root,text=" ",width=18,bg="silver", font=("Helvetica", 7)).place(x=790,y=572)
                                                                                                if all(x.isalpha() or x.isspace() for x in data23) and len(data23)!=0:
                                                                                                    Label(root,text=" ",width=15,bg="silver", font=("Helvetica", 7)).place(x=220,y=612)
                                                                                                    if all(x.isalpha() or x.isspace() for x in data24) and len(data24)!=0:
                                                                                                        Label(root,text=" ",width=17,bg="silver", font=("Helvetica", 7)).place(x=480,y=612)
                                                                                                        if all(x.isdigit() or x=="." for x in data25) and len(data25)!=0:
                                                                                                            Label(root,text=" ",width=20,bg="silver", font=("Helvetica", 7)).place(x=720,y=612)
                                                                                                            #root.destroy()
                                                                                                            gender=reciving(data111)
                                                                                                            cursor.execute("insert into student_detail(First_Name,Last_Name,Fathers_Name,\
                                                                                                                Mothers_Name,DOB,Contact_No_self,Contact_No_Parents,Semester,Course,Branch,\
                                                                                                                Year,College_Id,Roll_No,Enrollment_No,Adderss_Of_Correspondence,Permenent_Adderss,\
                                                                                                                Local_Gardain_In_Jhalawar_Jhalarapatan,Type_Of_Payment,Gender,Original_Category,Email,\
                                                                                                                Religon,Blood_Group,Marital_Status,Cast,Amount,upi_challen_No) value('%s','%s','%s','%s','%s','%s','%s',\
                                                                                                                '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',\
                                                                                                                '%s','%s')"%(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,\
                                                                                                                data14,data15,data16,data17,payment,gender,data19,data20,data21,data22,data23,data24,data25,data18))
                                                                                                            #cursor.execute("insert into submittion_details(clgid) value('%s')"%(data12))
                                                                                                            connection.commit()
                                                                                                            reg_next(root,data1,data6,data10,data12,data18,data25,payment)
                                                                                                            
                                                                                                        else:
                                                                                                            d25.delete(0,END)
                                                                                                            Label(root,text="Insert Rs in form 38550.00",fg="red",bg="silver", font=("Helvetica", 7)).place(x=720,y=612)
                                                                                                    else:
                                                                                                        d24.delete(0,END)
                                                                                                        Label(root,text='Insert  valid cast',fg="red",bg="silver", font=("Helvetica", 7)).place(x=480,y=612)
                                                                                                else:
                                                                                                    d23.delete(0,END)
                                                                                                    Label(root,text='Insert Valid Marital Status',fg="red",bg="silver", font=("Helvetica", 7)).place(x=220,y=612)
                                                                                            else:
                                                                                                d22.delete(0,END)
                                                                                                Label(root,text='Insert Blood Group',fg="red",bg="silver", font=("Helvetica", 7)).place(x=790,y=572)
                                                                                        else:
                                                                                            d21.delete(0,END)
                                                                                            Label(root,text='Insert Valid Religion',fg="red",bg="silver", font=("Helvetica", 7)).place(x=560,y=572)
                                                                                    else:
                                                                                        d20.delete(0,END)
                                                                                        Label(root,text='Insert Valid Email',fg="red",bg="silver", font=("Helvetica", 7)).place(x=220,y=572)
                                                                                else:
                                                                                    Label(root,text='select Category',fg="red",bg="silver", font=("Helvetica", 7)).place(x=745,y=532)  
                                                                            else:
                                                                                d18.delete(0,END)
                                                                                Label(root,text="Insert challen no",fg="red",bg="silver", font=("Helvetica", 7)).place(x=700,y=492) 
                                                                        else:
                                                                            d17.delete(0,END)
                                                                            Label(root,text="Insert address",fg="red",bg="silver", font=("Helvetica", 7)).place(x=520,y=452)
                                                                    else:
                                                                        d16.delete(0,END)
                                                                        Label(root,text="Insert address",fg="red",bg="silver", font=("Helvetica", 7)).place(x=390,y=412)
                                                                else:
                                                                    d15.delete(0,END)
                                                                    Label(root,text="Insert address",fg="red",bg="silver", font=("Helvetica", 7)).place(x=440,y=372)
                                                            else:
                                                                d14.delete(0,END)
                                                                Label(root,text="Insert Valid Enrollment Number",fg="red",bg="silver", font=("Helvetica", 7)).place(x=730,y=332)
                                                        else:
                                                            d13.delete(0,END)
                                                            Label(root,text="Insert Valid Roll Number",fg="red",bg="silver", font=("Helvetica", 7)).place(x=440,y=332)     
                                                    else:
                                                        d12.delete(0,END)
                                                        Label(root,text="Insert a Vaid Id",fg="red",bg="silver", font=("Helvetica", 7)).place(x=220,y=332)
                                                else:
                                                    Label(root,text="Select Year",fg="red",bg="silver", font=("Helvetica", 7)).place(x=810,y=292)
                                            else:
                                                Label(root,text="Select Branch",fg="red",bg="silver", font=("Helvetica", 7)).place(x=510,y=292)
                                        else:
                                            Label(root,text="Select Course",fg="red",bg="silver", font=("Helvetica", 7)).place(x=380,y=292)
                                    else:
                                        Label(root,text="Select Sem",fg="red",bg="silver", font=("Helvetica", 7)).place(x=220,y=292)
                                else:
                                    d7.delete(0,END)
                                    Label(root,text="Insert Valid Mobile Number",fg="red",bg="silver", font=("Helvetica", 7)).place(x=735,y=252)
                            else:
                                d6.delete(0,END)
                                Label(root,text="Insert Valid Mobile Number",fg="red",bg="silver", font=("Helvetica", 7)).place(x=450,y=252)
                        else:
                            
                            Label(root,text="Insert Valid date",fg="red",bg="silver", font=("Helvetica", 7)).place(x=220,y=252)
                    else:
                        d4.delete(0,END)
                        Label(root,text="Insert a Valid Name",fg="red",bg="silver", font=("Helvetica", 7)).place(x=620,y=212)
                else:
                    d3.delete(0,END)
                    Label(root,text="Insert a Valid Name",fg="red",bg="silver", font=("Helvetica", 7)).place(x=220,y=212)
            else:
                d2.delete(0,END)
                Label(root,text="Insert a valid Name",fg="red",bg="silver", font=("Helvetica", 7)).place(x=620,y=172)
        else:
            d1.delete(0,END)
            Label(root,text="Insert a Valid Name",fg="red",bg="silver", font=("Helvetica", 7)).place(x=220,y=172)

    def sel(data111):
        selection =data111
        if selection==1:
          selection="Male"
          return  selection
        elif selection==2:
          selection="Female"
          return selection
        elif selection==3:
          selection="Other"
          return selection
        else:
          Label(root,text="Select Gender").place(x=220,y=530)
    def reciving(data111):
        data112=sel(data111)
        return data112
    def labeltask(root):
        var = IntVar()
        Label(root,text="First name",width=15).place(x=100,y=150)
        Label(root,text="Last name",width=15).place(x=500,y=150)
        Label(root,text="Father name",width=15).place(x=100,y=190)
        Label(root,text="Mother's Name",width=15).place(x=500,y=190)
        Label(root,text="Date of Birth",width=15).place(x=100,y=230)
        Label(root,text="Contact no(self)",width=15).place(x=330,y=230)
        Label(root,text="Contact no(father)",width=15).place(x=615,y=230)
        Label(root,text="Samester",width=15).place(x=100,y=270)
        Label(root,text="course",width=10).place(x=295,y=270)
        Label(root,text="Branch",width=10).place(x=510,y=270)
        Label(root,text="Year",width=10).place(x=730,y=270)
        Label(root,text="College ID",width=15).place(x=100,y=310)
        Label(root,text="Roll No",width=15).place(x=320,y=310)
        Label(root,text="Enrollment No",width=15).place(x=610,y=310)
        Label(root,text="Address for correspondence(Also include Distt.,state,pincode)").place(x=100,y=350)
        Label(root,text="Permanent Adderss(Also include Distt.,state,pincode)").place(x=100,y=390)
        Label(root,text="Name and Address with Mobile No.of Local Guardian in Jhalawar/Jhalrapatan").place(x=100,y=430)
        Label(root,text="Challen/Recipe no/Other ").place(x=100,y=470)
        Label(root,text="Gender",width=15).place(x=100,y=510)
        Radiobutton(root, text="Male", variable=var,width=6 ,value=1,command=lambda:(sel(var.get()),reciving(var.get()))).place(x=220,y=510)
        Radiobutton(root, text="Female", variable=var,width=6, value=2,command=lambda:(sel(var.get()),reciving(var.get()))).place(x=300,y=510)
        Radiobutton(root, text="Other", variable=var,width=6, value=3,command=lambda:(sel(var.get()),reciving(var.get()))).place(x=390,y=510)
        Label(root,text="Original Category(Gen/SC/ST/OBC/SBC/Minority)").place(x=470,y=510)
        Label(root,text="Email",width=15).place(x=100,y=550)
        Label(root,text="Religion",width=10).place(x=475,y=550)
        Label(root,text="Blood Group",width=13).place(x=685,y=550)
        Label(root,text="Marital Status",width=15).place(x=100,y=590)
        Label(root,text="Cast",width=8).place(x=410,y=590)
        Label(root,text="Rs.",width=8).place(x=655,y=590)
        e1=Entry( root,width=45,bd=3)
        e1.place(x=220,y=150)
        e2=Entry( root,width=45,bd=3)
        e2.place(x=620,y=150)
        e3=Entry( root,width=45,bd=3)
        e3.place(x=220,y=190)
        e4=Entry( root,width=45,bd=3)
        e4.place(x=620,y=190)
        cal = DateEntry(root, width=12, background='darkblue',foreground='white', borderwidth=2)
        cal.place(x=220,y=230)
        e6=Entry( root,width=25,bd=3)
        e6.place(x=450,y=230)
        e7=Entry( root,width=25,bd=3)
        e7.place(x=735,y=230)
        variable = StringVar(root)
        variable1 = StringVar(root)
        variable2 = StringVar(root)
        variable3 = StringVar(root)
        variable4 = StringVar(root)
        variable5 = StringVar(root)
        variable.set("Select") # default value
        sem=OptionMenu(root, variable,"  1  ", "  2  ", "  3  ","  4  ","  5  ","  6  ","  7  ","  8  ")
        sem.config(font=('Helvetica',6))
        sem.place(x=220,y=270)
        variable1.set("Select") # default value
        b=OptionMenu(root, variable1," B.tech ")
        b.config(font=('Helvetica',6))
        b.place(x=380,y=270)
        variable2.set("Select") # default value
        b1=OptionMenu(root, variable2," C S "," I T "," M E "," C E "," E E "," E C " )
        b1.config(font=('Helvetica',6))
        b1.place(x=590,y=270)
        variable3.set("Select") # default value
        b2=OptionMenu(root, variable3," 2016"," 2017"," 2018"," 2019","2020")
        b2.config(font=('Helvetica',6))
        b2.place(x=810,y=270)
        variable4.set("Select") # default valueGen/SC/ST/OBC/SBC/Minority
        c=OptionMenu(root, variable4,"    Gen    ","    SC    ","    ST    ","OBC","    SBC    ","    Minority    ")
        c.config(font=('Helvetica',6))
        c.place(x=745,y=510)
        e12=Entry( root,width=15,bd=3)
        e12.place(x=220,y=310)
        e13=Entry( root,width=25,bd=3)
        e13.place(x=440,y=310)
        e14=Entry( root,width=26,bd=3)
        e14.place(x=730,y=310)
        e15=Entry( root,width=75,bd=3)
        e15.place(x=440,y=350)
        e16=Entry( root,width=84,bd=3)
        e16.place(x=390,y=390)
        e17=Entry( root,width=62,bd=3)
        e17.place(x=520,y=430)
        option=("Cash", "DD", "Online Payment","Other")
        variable5.set("Select") # default value
        c1=OptionMenu(root, variable5,*option,command=lambda x: payment_label(root,variable5.get()))
        c1.config(font=('Helvetica',6))
        c1.place(x=250,y=470)
        e18=Entry( root,width=32,bd=3)
        e18.place(x=700,y=470)
        e20=Entry( root,width=40,bd=3)
        e20.place(x=220,y=550)
        e21=Entry( root,width=18,bd=3)
        e21.place(x=560,y=550)
        e22=Entry( root,width=17,bd=3)
        e22.place(x=790,y=550)
        e23=Entry( root,width=29,bd=3)
        e23.place(x=220,y=590)
        e24=Entry( root,width=29,bd=3)
        e24.place(x=480,y=590)
        e25=Entry( root,width=29,bd=3)
        e25.place(x=720,y=590)
       
        Button(root, text='Update image',width="15", command=lambda : open_img(root)).place(x=1000,y=300)
        Button(root, text='Exit',bg="cyan2",fg='red',width=15,command=quit).place(x=390,y=650)
        Button(root, text='Back',bg="cyan2",fg='red',width=15,command=lambda:(root.destroy(),registration())).place(x=280,y=650)
        Button(root,text="Next",width=15,bg="black",fg="blue",command=lambda: check_and_put_data_for_reg(var.get(),root,e1.get(),\
            e2.get(),e3.get(),e4.get(),cal.get(),e6.get(),e7.get(),variable.get(),variable1.get(),variable2.get(),\
            variable3.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),variable5.get(),e18.get(),variable4.get(),\
            e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get(),e1,e2,e3,e4,e6,e7,e12,e13,e14,e15,e16,e17,\
            e18,e20,e21,e22,e23,e24,e25)).place(x=500,y=650)
        #Button(root, text='Administrator work',bg="cyan2",fg='red',command=lambda:adm_button(root)).place(x=990,y=150)
    def login():
        root=Tk()
        root.state('zoomed')
        root.title("Design and develop by RAKESH KUMAWAT")
        root.configure(background="silver")
        Label(root,text="Welcome to Government Engineering College Jhalawar",width=95,fg = "black",bg = "white",font = "Helvetica 25 bold italic").pack()
        Label(root,text="ACADEMIC SESSION : 2018-2019",font = "Helvetica 16 bold italic",bg="silver").pack()
        Label(root,text="STUDENT ONLINE REGISTRATION FORAM",font = "Helvetica 15 bold italic",fg="blue",bg="silver").pack()
        labeltask(root)
        root.mainloop()

    def next_reg2to8(root1,ndata,ndata1,d1,d2):
        print(ndata)
        if len(ndata)!= 0:
            Label(root1,text=" ",width=50,bg='silver').place(x=680,y=250)
            if len(ndata1)!= 0:
                Label(root1,text=" ",width=50,bg='silver').place(x=680,y=280)
                messagebox.showinfo("congrats","Registration successfull")
                root1.destroy()
                registration()
            else:
                d2.delete(0,END)
                Label(root1,fg="red",bg="silver",text="Enter payment success proof Id").place(x=680,y=280)
        else:
            d1.delete(0,END)
            Label(root1,fg="red",bg="silver",text="Enter paynet Type * online payment,DD,cach,other").place(x=680,y=250)
    def reg2to8():
        root1=Tk()
        root1.state('zoomed')
        root1.configure(background='silver')
        Label(root1,text="Enter payment type").place(x=300,y=250)
        Label(root1,text="Enter Transaction Id or Challen No.").place(x=300,y=280)
        e=Entry(root1,bd=3)
        e.place(x=530,y=250)
        e1=Entry(root1,bd=3)
        e1.place(x=530,y=280)
        Button(root1,text="Exit",width=15,command=quit).place(x=430,y=370)
        Button(root1,text="Next",width=15,command=lambda:(next_reg2to8(root1,e.get(),e1.get(),e,e1))).place(x=530,y=370)
   

    def search_student_details(root,data):
        cursor.execute("select First_Name,Last_Name,Fathers_Name,Contact_No_self,Semester,Branch,Email,Semester from student_detail where College_Id=%s",(data))
        data1=cursor.fetchall()
        if len(data1)!=0:
            Label(root,text=" ",width=30,bg='silver').place(x=450,y=30)
            canvas_width=1000
            canvas_height=40
            w=Canvas(root,width=canvas_width,height=canvas_height,bg='silver')
            w.place(x=150,y=100)
            y=int(canvas_height/2)
            w.create_line(0,y,canvas_width,y,fill='#476042')
            Label(root,text=" ",width=100,bg='silver',font=('Helvetica 15')).place(x=150,y=88)
            Label(root,text=" ",width=100,bg='silver',font=('Helvetica 15')).place(x=150,y=123)
            Label(root,text="Government Engineering College Jhalawar",width=95,fg = "black",bg = "silver",font="Helveltica 20 bold italic").place(x=-250,y=160)
            Label(root,text="Name : ").place(x=260,y=250)
            Label(root,text="Father's Name : ").place(x=630,y=250)
            Label(root,text="Contact_No_Self : ").place(x=260,y=280)
            Label(root,text="Previous Semester : ").place(x=630,y=280)
            Label(root,text="Branch : ").place(x=260,y=310)
            Label(root,text="Email : ").place(x=630,y=310)

            Label(root,text=str(data1[0][0]) + " "+str(data1[0][1]),bg='silver').place(x=340,y=250)
            Label(root,text=data1[0][2],bg='silver').place(x=730,y=250)
            Label(root,text=data1[0][3],bg='silver').place(x=380,y=280)
            Label(root,text=data1[0][4],bg='silver').place(x=730,y=280)
            Label(root,text=data1[0][5],bg='silver').place(x=340,y=310)
            Label(root,text=data1[0][6],bg='silver').place(x=730,y=310)
            string1="Register "+ str(data1[0][7]+1) + " Semester"
            Button(root,text=string1,width=20,command=lambda:(root.destroy(),reg2to8())).place(x=500,y=400)
            #print(str(data1[0][0]) + " "+str(data1[0][1]))
            #print(data1[0][1])
        else:
            Label(root,fg="red",bg="silver",text="Data Not Found First Register It").place(x=450,y=30)
        

    def sem2_to_8sem():#For student who are in 2nd to 8 sem
        root=Tk()
        root.state('zoomed')
        root.configure(background='silver')
        root.title('G E C J Home Page>2 sem To 8 sem')
        Label(root,text='Enter College Id',font=('Helvetica 13 bold'),bg='silver').place(x=50,y=30)
        e1=Entry(root,bd=3)
        e1.place(x=190,y=30)
        Button(root,text='Search',width=10,fg='white',bg='black',font=('Helveltica 11 bold'),command=lambda:(search_student_details(root,e1.get()))).place(x=330,y=30)
        Button(root,text="Back",width=20,fg='blue').place(x=170,y=650)
        Button(root,text="Exit",width=20,command=quit).place(x=20,y=650)
        root.mainloop()
    root=Tk()
    root.state('zoomed')
    root.configure(background="silver")
    root.title("G E C J Home page")
    Label(root,text="Welcome to Government Engineering College Jhalawar",width=95,fg = "black",bg = "silver",font = "Helvetica 25 bold italic").pack()
    Button(root,text="1 Year",width=30,command=lambda:(root.destroy(),login())).place(x=400,y=250)
    Button(root,text="2 Year To 8 Year",width=30,command=lambda:(root.destroy(),sem2_to_8sem())).place(x=520,y=280)
    Button(root,text="Exit",width=20,command=quit).place(x=20,y=650)
    Button(root, text='Administrator work',bg="cyan2",fg='red',width=30,command=lambda:(root.destroy(),adm_button())).place(x=640,y=310)
    Label(root,text="Powered & Maintained By: Department of Computer Science & Engineering, GECJ\n\
                     Govt. Engineering College Jhalawar\n\
                     Design And Develop By Rakesh Kumawat Contact No.:8503875941\n\
                     www.gecj.ac.in | Contacts \n\
            Sunel Road, Village: Chandlai,Tehsil-Jhalrapatan, Jhalawar-326023, Rajasthan, India\n\
                    Email-gecj.web@gmail.com ,Contact No.: 07432-242812",font="Helveltica 10 bold italic",bg='silver').place(x=750,y=550)
    root.mainloop()
    #login() 
if __name__ == "__main__":
    registration()
