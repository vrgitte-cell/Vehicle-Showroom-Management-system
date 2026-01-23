import tkinter
from tkinter import *
# from sam1 import *
# from sales import *

def on_enter(e):
    e.widget['background'] = 'blue'
    e.widget['foreground'] = 'white'
def on_leave(e):
    e.widget['background'] = '#1E88E5'
    e.widget['foreground'] = 'white'











def cust():
    cust_page=Toplevel()
    cust_page.title('👤Customer Page')
    cust_page.state('zoomed')
    cust_page.config(bg='#f0f8ff')


    def cust_new():
    # Main Frame
        frame = Frame(cust_page, bg="white", bd=2, relief=RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=550, height=500)

    # Title
        Label(frame, text="Customer Details Form",
          font=("Segoe UI", 16, "bold"),
          bg="#2c3e50", fg="white", pady=10).pack(fill=X)

        form = Frame(frame, bg="white", padx=30, pady=20)
        form.pack(fill=BOTH, expand=True)

    # Labels & Entries
        fields = ["Full Name", "Phone Number", "City", "Vehicle Interested"]

        for i, field in enumerate(fields):
            Label(form, text=field, font=("Segoe UI", 16),
              bg="white", anchor=W).grid(row=i, column=0, sticky=W, pady=8)


        name_entry=Entry(form, font="cambria 15 bold", width=20,bg='#fffaf0')
        name_entry.grid(row=0, column=1, pady=8, padx=10)

        phone_entry=Entry(form, font="cambria 15 bold", width=20,bg='#fffaf0')
        phone_entry.grid(row=1, column=1, pady=8, padx=10)

        city_entry = Entry(form, font="cambria 15 bold", width=20, bg='#fffaf0')
        city_entry.grid(row=2, column=1, pady=8, padx=10)

        vi_entry= Entry(form, font="cambria 15 bold", width=20, bg='#fffaf0')
        vi_entry.grid(row=3, column=1, pady=8, padx=10)



        Button(form,text="Save",font="cambria 12 bold",cursor="hand2",bg='green',fg='white',
               width=10).grid(row=8,column=1,)
        Button(form,text="Clear",font="cambria 12 bold",cursor="hand2",bg="#27ae60",
               fg='white',width=10).grid(row=10,column=2,sticky='s')

        Button(form, text="BACK", fg="red", command=frame.destroy, font="arial 10 bold", relief="groove", bd=5,
           cursor="hand2").place(relx=0.9, rely=0.9)

    # Buttons

    def cust_view():
        frame = Frame(cust_page, bg="white", bd=2, relief=RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=550, height=500)

        form = Frame(frame, bg="white", padx=30, pady=20)
        form.pack(fill=BOTH, expand=True)


        form = Frame(frame, bg="white", padx=30, pady=20)
        form.pack(fill=BOTH, expand=True)

        Button(form, text="BACK", fg="red", command=frame.destroy, font="arial 10 bold", relief="groove", bd=5,
               cursor="hand2").place(x=450,y=0)

    def cust_update():
        frame = Frame(cust_page, bg="white", bd=2, relief=RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=550, height=500)

        form = Frame(frame, bg="white", padx=30, pady=20)
        form.pack(fill=BOTH, expand=True)

        form = Frame(frame, bg="white", padx=30, pady=20)
        form.pack(fill=BOTH, expand=True)

        Label(form, text="Name", font=("Segoe UI", 16),
              bg="white", anchor=W).grid(row=0, column=0, sticky=W, pady=8)
        Entry(form, font="cambria 15 bold", width=20, bg='#fffaf0').grid(row=0, column=1, pady=8, padx=10)

        Button(form, text="BACK", fg="red", command=frame.destroy, font="arial 10 bold", relief="groove", bd=5,
               cursor="hand2").place(relx=0.9, rely=0.9)

    def cust_del():
        frame = Frame(cust_page, bg="white", bd=2, relief=RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=550, height=500)

        form = Frame(frame, bg="white", padx=30, pady=20)
        form.pack(fill=BOTH, expand=True)

        form = Frame(frame, bg="white", padx=30, pady=20)
        form.pack(fill=BOTH, expand=True)

        Label(form, text="Name", font=("Segoe UI", 16),
              bg="white", anchor=W).grid(row=0, column=0, sticky=W, pady=8)
        name_entry=Entry(form, font="cambria 15 bold", width=20, bg='#fffaf0')
        name_entry.grid(row=0, column=1, pady=8, padx=10)

    Button(cust_page, text="Add", bg="#27ae60", fg="white",
           font=("Segoe UI", 16, "bold"),command=cust_new, width=10).grid(row=2, column=0, padx=5)

    Button(cust_page, text="Update", bg="#2980b9", fg="white",
           font=("Segoe UI", 16, "bold"), width=10,command=cust_update).grid(row=2, column=1, padx=5)

    Button(cust_page, text="Delete", bg="#c0392b", fg="white",
           font=("Segoe UI", 16, "bold"), width=10,command=cust_view).grid(row=2, column=2, padx=5)

    Button(cust_page, text="View All", bg="#7f8c8d", fg="white",
           font=("Segoe UI", 16, "bold"), width=10,command=cust_view).grid(row=2, column=3, padx=5)

    Button(cust_page, text="BACK", fg="red", command=cust_page.destroy, font="arial 10 bold", relief="groove", bd=5,
           cursor="hand2").place(relx=0.9, rely=0.9)

    cust_page.mainloop()





























m=Tk()
m.state('zoomed')
m.title('Main Page')
img=PhotoImage(file=r"C:\Users\vrgit\Downloads\vsms.png")
Label(m,image=img).pack()
Label(m,text='Vehicle Showroom Management System',font=("Segoe UI", 26, "bold"),
    bg="#F4F6F8",
    fg="#FF9800",width=200,
      border=1,bd=2,relief='solid').place(x=620,y=60,anchor='center',bordermode='outside')

btn_style = {
    "font": ("Segoe UI", 18, "bold"),
    "bg": "#1E88E5",
    "fg": "white",
    "width": 18,
    "height": 1,
    "bd": 2,
    "cursor": "hand2",

}

btn1=Button(m,text='🚗 Vehicle',**btn_style,pady=5)
btn1.place(x=550,y=150)
btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)
btn2=Button(m,text='👤 Customer',**btn_style,pady=5,command=cust)
btn2.place(x=550,y=250)
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)
btn3=Button(m,text='💰 Sales',**btn_style,relief='raised',pady=5)
btn3.place(x=550,y=350)
btn3.bind("<Enter>", on_enter)
btn3.bind("<Leave>", on_leave)

btn4=Button(m,text='📊 Report',**btn_style,relief='raised',pady=5)
btn4.place(x=550,y=450)
btn4.bind("<Enter>", on_enter)
btn4.bind("<Leave>", on_leave)
btn5=Button(m,text='❌ Exit',**btn_style,relief='raised',pady=5,command=m.destroy)
btn5.place(x=550,y=550)
btn5.bind("<Enter>", on_enter)
btn5.bind("<Leave>", on_leave)






m.mainloop()