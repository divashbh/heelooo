from tkinter import*
import sqlite3
from tkinter import ttk,messagebox
import tkinter.font as font

root=Tk()

font1= font.Font(family="Helvetica", size =16)
com=sqlite3.connect('facebook.db')
c=com.cursor()
c.execute
# c.execute(''' Create table user(
#     firstName text,
#     lastName text,
#     age text,
#     adress text,
#     city text,
#     Zipcode text,
#     password text, 
#     gender text
# )
# ''')

fb=Label(root,text='FACEBOOK',fg='blue',font= font1)
fb.grid(row=0,column=0,columnspan=2)

#commands
def submit():
    conn= sqlite3.connect('facebook.db')

    c=conn.cursor()
    c.execute('''insert into user values(:firstName, :lastName,:age,:adress,:city,:Zipcode,:password,:gender)''',{'firstName':firstname.get(),'lastName':lastname.get(),'age':age.get(), 'adress':address.get(),'city':city.get(),'Zipcode':zipcode.get(),'password':password.get(),'gender':gender.get()}
    )
    messagebox.showinfo('success','Inserted sucessfully')
    firstname.delete(0,END)
    lastname.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    password.delete(0,END)
    
    conn.commit()
    conn.close()




def show():
    conn= sqlite3.connect('facebook.db')

    c=conn.cursor()
    c.execute('select *,oid from user')
    
    records=c.fetchall()
    print_records=""
    for record in records:
        print_records+=str(record[0]) + " " +str(record[1]) + "" + "\t" + str(record[8]) + "\n"
    show_label=Label(root,text=print_records)
    show_label.grid(row=13,column=0,columnspan=2)
    messagebox.showinfo('success','showed')
    conn.commit()
    conn.close()




def delete():
    conn= sqlite3.connect('facebook.db')

    c=conn.cursor()
    c.execute('delete from user where oid ='+delete_entry.get())
    print('success','deleted')
    conn.commit()
    conn.close()

def update():
    co=sqlite3.connect("Facebook.db")
    c=co.cursor()
    record_id=delete_entry.get()
    
    c.execute(""" UPDATE User SET
    FirstName=:first,
    LastName=:last,
    age=:age,
    adress=:address,
    city=:city,
    zipcode=:zipcode,
    password=:password,
    gender=:gender
    WHERE oid=:oid""",
    {"first":f_name_editor.get(),
    "last":l_name_editor.get(),
    "age":age_editor.get(),
    "address":address_editor.get(),
    "city":city_editor.get(),
    "zipcode":zipcode_editor.get(),
    "password":password_editor.get(),
    "gender":gender_editor.get(),
    "oid":record_id
    }
    )
    messagebox.showinfo("user","Upadted Successfully")
    co.commit()
    co.close()
    editor.destroy()






def edit():
    global editor 
    editor=Toplevel()
    editor.title("Update Data")
    editor.geometry("300x400")

    conn=sqlite3.connect("Facebook.db")
    c=conn.cursor()
    record_id=delete_entry.get()
    c.execute("SELECT * FROM User WHERE oid=" + record_id)
    records=c.fetchall()
    global f_name_editor
    global l_name_editor
    global age_editor
    global address_editor
    global city_editor
    global zipcode_editor  
    global password_editor
    global gender_editor


    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1)

    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)

    age_editor=Entry(editor,width=30)
    age_editor.grid(row=2,column=1)

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=3,column=1)

    city_editor=Entry(editor,width=30)
    city_editor.grid(row=4,column=1)

    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1)

    password_editor=Entry(editor,width=30)
    password_editor.grid(row=6,column=1)

    gender_editor=Entry(editor,width=30)
    gender_editor.grid(row=7,column=1)

    f_name_label=Label(editor,text="First Name")
    f_name_label.grid(row=0,column=0)

    l_name_label=Label(editor,text="Last Name")
    l_name_label.grid(row=1,column=0)

    age_label=Label(editor,text="age")
    age_label.grid(row=2,column=0)

    address_label=Label(editor,text="Address")
    address_label.grid(row=3,column=0)

    city_label=Label(editor,text="City")
    city_label.grid(row=4,column=0)

    zipcode_label=Label(editor,text="zipcode")
    zipcode_label.grid(row=5,column=0)

    password_label=Label(editor,text="password")
    password_label.grid(row=6,column=0)

    gender_label=Label(editor,text="gender")
    gender_label.grid(row=7,column=0)

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        age_editor.insert(0,record[2])
        address_editor.insert(0,record[3])
        city_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])
        password_editor.insert(0,record[6])
        gender_editor.insert(0,record[7])

    edit_btn=Button(editor,text="Save",command=update)
    edit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=110)




firstname= Entry(root, width=30, font=font1)
firstname.grid(row=1,column=1,padx=20,pady=5)

lastname=Entry(root,width=30, font=font1)
lastname.grid(row=2,column=1,pady=5)

age=Entry(root,width=30, font=font1)
age.grid(row=3,column=1,pady=5)

address=Entry(root,width=30, font=font1)
address.grid(row=4,column=1,pady=5)

city=Entry(root,width=30, font=font1)
city.grid(row=5,column=1,pady=5)

zipcode=Entry(root,width=30, font=font1)
zipcode.grid(row=6,column=1,pady=5)

password=Entry(root,width=30, font=font1, show= "* ")
password.grid(row=7,column=1,pady=5)

gender=Entry(root,width=30, font=font1)
gender.grid(row=8,column=1,pady=5)

fnamelabel= Label(root,text="firstname", font=font1)
fnamelabel.grid(row=1,column=0)

lastnamelabel= Label(root,text="lastname", font=font1)
lastnamelabel.grid(row=2,column=0)

agelabel= Label(root,text="age", font=font1)
agelabel.grid(row=3,column=0)

addresslabel= Label(root,text="address", font=font1)
addresslabel.grid(row=4,column=0)

citylabel= Label(root,text="city", font=font1)
citylabel.grid(row=5,column=0)

zipcodelabel= Label(root,text="zipcode", font=font1)
zipcodelabel.grid(row=6,column=0)

passwordlabel= Label(root,text="password", font=font1)
passwordlabel.grid(row=7,column=0)

genderlabel= Label(root,text="gender", font=font1)
genderlabel.grid(row=8,column=0)

deletelabel= Label(root,text="delete", font=font1)
deletelabel.grid(row=10,column=0)

sub_btn=Button(root,text='Submit',command=submit, font=font1)
sub_btn.grid(row=9,column=0,columnspan=2,pady=20)

delete_entry=Entry(root,width=30, font=font1)
delete_entry.grid(row=10,column=1,pady=5)


sub_btn=Button(root,text='delete',command=delete, font=font1)
sub_btn.grid(row=11,column=0,pady=10)
sub_btn=Button(root,text='show',command=show, font=font1)
sub_btn.grid(row=11,column=1,columnspan=1,pady=5)
sub_btn=Button(root,text='edit',command=edit, font=font1,pady=10)
sub_btn.grid(row=11,column=2)



com.commit()
com.close()

root.mainloop()