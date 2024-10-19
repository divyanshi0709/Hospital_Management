from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import time
import datetime


from tkinter import messagebox
import mysql.connector

class hospital :
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.namoftab=StringVar()
        self.dis=StringVar()
        self.refno=StringVar()
        self.patname=StringVar()
        self.dob=StringVar()
        self.patadd=StringVar()
        self.issuedate=StringVar()
        self.exdate=StringVar()
        self.sidef=StringVar()
        self.blpress=StringVar()
        self.patid=StringVar()
        self.nooftab=StringVar()
        self.dailydos=StringVar()
        self.furthinfo=StringVar()
        self.med=StringVar()
        self.nhs=StringVar()
        self.cont=StringVar()
        self.bldgrp=StringVar()
    # def reset():


# ******************************************functionality declaration*************************
        self.conn=mysql.connector.connect(host="localhost",user="root")
        self.cur=self.conn.cursor()
        self.cur.execute("use hospital")
# try:
#     cur.execute("use save")
# except:
#     cur.execute("create database save")
#     cur.execute("use save")


# def save():
#     cur.execute("insert into patient(Name_Of_Tablet,Disease,Reference_No,Patient's Name,Date Of Birth,Patient's Address,Issue Date,Expiry Date,Side Effects,Blood Pressure,Patient's Id,No. Of Tablets,Daily Dose,Further Information,Medicine,NHS No,Contact No,Blood Group)values('{Combonametab.get()}','{txtdis.get()}','{txtref.get()}','{txtpatname.get()}','{txtdob.get()}','{txtadd.get()}','{txtissue.get()}','{txtexpdate.get()}','{txtsideeff.get()}','{txtbloodpress.get()}','{txtpatid.get()}','{txtnotab.get()}','{txtdailydos.get()}','{txtfurtherinfo.get()}','{txtmed.get()}','{txtNHS.get()}','{txtnum.get()}','{txtbloodgrp.get()}')")
#     conn.comit() 
      


        lbltitle=Label(self.root,bd=15,relief=RIDGE,text="Hospital Management System",fg="white",bg="blue",font=("times new roman",30,"bold"))
        lbltitle.pack(side=TOP,fill=X)

            # ****************************dataframe*****************************
        Dataframe=Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=85,width=1530,height=360)

        dfleft=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10,font=("arial",10,"bold"),text='Patient Information',fg='grey')
        dfleft.place(x=2,y=5,width=900,height=330)

        dfright=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10,font=("arial",10,"bold"),text='Prescreption',fg="grey")
        dfright.place(x=905,y=5,width=352,height=330)

            # ****************buttonframe**************************
        buttonframe=Frame(self.root,bd=10,relief=RIDGE)
        buttonframe.place(x=0,y=445,width=1530,height=48)

            # ****************detailframe**************************
            
        detailframe=Frame(self.root,bd=10,relief=RIDGE)
        detailframe.place(x=0,y=490,width=1270,height=150)


            # *********************dataframeleft********************************
        lblnametablet=Label(dfleft,text="Name Of Tablet",font=("arial",12),padx=1,pady=6)
        lblnametablet.grid(row=0,column=0)

        self.combonametab=ttk.Combobox(dfleft,textvariable=self.namoftab,font=("arial",12,"bold"),width=30)
        self.combonametab["values"]=('Nice','Corona Vacacine','Citrazin','PCM','Discprine','Meftal Spac','Brofin','Azithromicin','Amg=500','Lipvas-20','Levocitrazin','Evomine','cip-Jox')
        self.combonametab.grid(row=0,column=1)


        lbldis=Label(dfleft,font=("arial",12),text="Disease:",padx=2,pady=6)
        lbldis.grid(row=1,column=0)
        self.txtdis=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.dis,width=30)
        self.txtdis.grid(row=1,column=1)


        lblref=Label(dfleft,font=("arial",12),text="Reference No.",padx=2,pady=6)
        lblref.grid(row=2,column=0)
        self.txtref=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.refno,width=30)
        self.txtref.grid(row=2,column=1)


        lblpatname=Label(dfleft,font=("arial",12),text="Patient's Name:",padx=2,pady=6)
        lblpatname.grid(row=3,column=0)
        self.txtpatname=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.patname,width=30)
        self.txtpatname.grid(row=3,column=1)

        lbldob=Label(dfleft,font=("arial",12),text="Date Of Birth:",padx=2,pady=6)
        lbldob.grid(row=4,column=0)
        self.txtdob=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.dob,width=30)
        self.txtdob.grid(row=4,column=1)

        lbladd=Label(dfleft,font=("arial",12),text="Patient's Address:",padx=2,pady=6)
        lbladd.grid(row=5,column=0)
        self.txtadd=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.patadd,width=30)
        self.txtadd.grid(row=5,column=1)

        lblissue=Label(dfleft,font=("arial",12),text="Issue Date",padx=2,pady=6)
        lblissue.grid(row=6,column=0)
        self.txtissue=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.issuedate,width=30)
        self.txtissue.grid(row=6,column=1)

        lblexpdate=Label(dfleft,font=("arial",12),text="Expiry Date:",padx=2,pady=6)
        lblexpdate.grid(row=7,column=0)
        self.txtexpdate=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.exdate,width=30)
        self.txtexpdate.grid(row=7,column=1)

        lblsideeff=Label(dfleft,font=("arial",12),text="Side Effects:",padx=2,pady=6)
        lblsideeff.grid(row=8,column=0)
        self.txtsideeff=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.sidef,width=30)
        self.txtsideeff.grid(row=8,column=1)

        lblbloodpress=Label(dfleft,font=("arial",12),text="Blood Pressure",padx=2,pady=6)
        lblbloodpress.grid(row=0,column=2)
        self.txtbloodpress=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.blpress,width=30)
        self.txtbloodpress.grid(row=0,column=3)


        lblpatid=Label(dfleft,font=("arial",12),text="Patient's Id:",padx=2,pady=6)
        lblpatid.grid(row=1,column=2)
        self.txtpatid=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.patid,width=30)
        self.txtpatid.grid(row=1,column=3)


        lblnotab=Label(dfleft,font=("arial",12),text="No. Of Tablets:",padx=2,pady=6)
        lblnotab.grid(row=2,column=2)
        self.txtnotab=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.nooftab,width=30)
        self.txtnotab.grid(row=2,column=3)

        lbldailydos=Label(dfleft,font=("arial",12),text="Daily Dose:",padx=2,pady=6)
        lbldailydos.grid(row=3,column=2)
        self.txtdailydos=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.dailydos,width=30)
        self.txtdailydos.grid(row=3,column=3)

        lblfurtherinfo=Label(dfleft,font=("arial",12),text="Further Information:",padx=2,pady=6)
        lblfurtherinfo.grid(row=4,column=2)
        self.txtfurtherinfo=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.furthinfo,width=30)
        self.txtfurtherinfo.grid(row=4,column=3)

        lblmed=Label(dfleft,font=("arial",12),text="Medicine:",padx=2,pady=6)
        lblmed.grid(row=5,column=2)
        self.txtmed=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.med,width=30)
        self.txtmed.grid(row=5,column=3)

        lblNHS=Label(dfleft,font=("arial",12),text="NHS No.:",padx=2,pady=6)
        lblNHS.grid(row=6,column=2)
        self.txtNHS=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.nhs,width=30)
        self.txtNHS.grid(row=6,column=3)
            
        lblnum=Label(dfleft,font=("arial",12),text="Contact No:",padx=2,pady=6)
        lblnum.grid(row=7,column=2)
        self.txtnum=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.cont,width=30)
        self.txtnum.grid(row=7,column=3)

        lblbloodgrp=Label(dfleft,font=("arial",12),text="Blood Group:",padx=2,pady=6)
        lblbloodgrp.grid(row=8,column=2)
        self.txtbloodgrp=Entry(dfleft,font=("arial",12,"bold"),textvariable=self.bldgrp,width=30)
        self.txtbloodgrp.grid(row=8,column=3)

            # *******************************dataframeryt*******************************

        # prec=Text(dfright,font=("arial",12),width=45,height=16,padx=2,pady=6)
        # prec.grid(row=0,column=0)

        img=Image.open("doctor.jpg").resize((170,70))
        bck_img=ImageTk.PhotoImage(img)
        pic=Label(dfright,image=bck_img)
        pic.grid(row=0,column=0)

            #*********************************buttons in Buttonframe********************************

        buttprec=Button(buttonframe,text="Prescription",bg="blue",fg="white",relief="raised",font=("arial",10,"bold"),width=30,padx=2,pady=6)
        buttprec.grid(row=0,column=0)

        buttprecdata=Button(buttonframe,text="Prescription Data",bg="blue",fg="white",relief="raised",font=("arial",10,"bold"),
                            width=30,padx=2,pady=6,command=self.store_prescription)
        buttprecdata.grid(row=0,column=1)

        buttupdate=Button(buttonframe,text="Update",bg="blue",fg="white",relief="raised",font=("arial",10,"bold"),width=30,padx=2,pady=6)
        buttupdate.grid(row=0,column=2)

        buttdelete=Button(buttonframe,text="Reset",bg="blue",fg="white",relief="raised",font=("arial",10,"bold"),width=30,padx=2,pady=6)
        buttdelete.grid(row=0,column=3)

        buttclear=Button(buttonframe,text="Clear",bg="blue",fg="white",relief="raised",font=("arial",10,"bold"),width=30,padx=2,pady=6)
        buttclear.grid(row=0,column=4)

        buttexit=Button(buttonframe,text="Exit",bg="blue",fg="white",relief="raised",font=("arial",10,"bold"),width=30,padx=2,pady=6)
        buttexit.grid(row=0,column=5)

            # ***************************table scrollbar*********************************
        scrol_x=ttk.Scrollbar(detailframe,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(detailframe,orient=VERTICAL)

        self.hospital_table=ttk.Treeview(detailframe,column=("namoftab","dis","refno","patname","dob","patadd","issuedate","exdate","sideff","blpress","patid","nooftab","dailydos","furthinfo","med","nhs","cont","bldgrp"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)


        self.hospital_table.heading("namoftab",text="Name Of Tablets")
        self.hospital_table.heading("dis",text="Disease")
        self.hospital_table.heading("refno",text="Reference No.")
        self.hospital_table.heading("patname",text="Patient's Name")
        self.hospital_table.heading("dob",text="Date Of Birth")
        self.hospital_table.heading("patadd",text="Patient's Address")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("exdate",text="Expiry Date")
        self.hospital_table.heading("sideff",text="Side Effects")
        self.hospital_table.heading("blpress",text="Blood Pressure")
        self.hospital_table.heading("patid",text="Patient's Id")
        self.hospital_table.heading("nooftab",text="No. Of Tablets")
        self.hospital_table.heading("dailydos",text="Daily Dose")
        self.hospital_table.heading("furthinfo",text="Further Information")
        self.hospital_table.heading("med",text="Medicine")
        self.hospital_table.heading("nhs",text="NHS No.")
        self.hospital_table.heading("cont",text="Contact No.")
        self.hospital_table.heading("bldgrp",text="Blood Group")
            
        self.hospital_table['show']="headings"

        
        scrol_x.config(command=self.hospital_table.xview)
        scrol_y.config(command=self.hospital_table.yview)                                 #to move the scroll
            
            
        self.hospital_table.pack(fill=BOTH,expand=1)
        
    def store_prescription(self):
        user_combonametab = self.combonametab.get() 
        user_txtdis = self.txtdis.get()
        user_txtref= self.txtref.get()
        user_txtpatname = self.txtpatname.get()
        user_txtdob= self.txtdob.get()
        user_txtadd = self.txtadd.get()
        user_txtissue= self.txtissue.get()
        user_txtexpdate= self.txtexpdate.get()
        user_txtsideeff = self.txtsideeff.get()
        user_txtbloodpress = self.txtbloodpress.get()
        user_txtpatid = self.txtpatid.get()
        user_txtnotab = self.txtnotab.get()
        user_txtdailydos =  self.txtdailydos.get()
        user_txtfurtherinfo = self.txtfurtherinfo.get()
        user_txtmed = self.txtmed.get()
        user_txtNHS = self.txtNHS.get()
        user_txtnum = self.txtnum.get()
        user_txtbloodgrp = self.txtbloodgrp.get()
        self.cur.execute(f"""insert into patient(Name_Of_Tablet,Disease,Reference_No,Patients_Name,Date_Of_Birth,Patients_Address,
                         Issue_Date,Expiry_Date,Side_Effects,Blood_Pressure,Patients_Id,No_of_Tablets,Daily_Dose,Further_Information,
                         Medicine,NHS_No,Contact_No,Blood_Group) values
                         ('{user_combonametab}','{user_txtdis}','{user_txtref}',
                         '{user_txtpatname}','{user_txtdob}','{user_txtadd}','{user_txtissue}','{user_txtexpdate}',
                         '{user_txtsideeff}','{user_txtbloodpress}','{user_txtpatid}','{user_txtnotab}','{user_txtdailydos}',
                         '{user_txtfurtherinfo}','{user_txtmed}','{user_txtNHS}','{user_txtnum}','{user_txtbloodgrp}')""")
        self.show_prescription()
        self.conn.commit() 
    
    def show_prescription(self):
        query2 = "select * from patient"
  
        # executing cursor 
        self.cur.execute(query2) 
        
        # display all records 
        table = self.cur.fetchall() 
        for combonametab,txtdis,txtref,txtpatname,xtdob,txtadd,txtissue,txtexpdate,txtsideeff,txtbloodpress,txtpatid,txtnotab,txtdailydos,txtfurtherinfo,txtmed,txtNHS,txtnum,txtbloodgrp in table: 

            self.hospital_table.insert("", 'end', values=(combonametab,txtdis,txtref,txtpatname,xtdob,txtadd,txtissue,txtexpdate,txtsideeff,txtbloodpress,txtpatid,txtnotab,txtdailydos,txtfurtherinfo,txtmed,txtNHS,txtnum,txtbloodgrp))


root=Tk()
obj=hospital(root)
root.mainloop()
