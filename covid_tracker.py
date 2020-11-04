from covid import Covid
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk
def country():
    covid = Covid()
    nme=entt.get()
    entt.set("")
    data=covid.get_status_by_country_name(nme)

    # print(data)
    remove=['id', 'country', 'latitude', 'longitude', 'last_update']
    for i in remove:
        data.pop(i)
    all=data.pop('confirmed')

    id=list(data.keys())
    value=[str(i) for i in data.values()]
    plt.pie(value,labels=id,colors=['r','y','g','b'],autopct="%1.1f%%")

    plt.title("COUNTRY: "+nme.upper()+"\n TOTAL CASES : "+str(all))
    plt.legend()
    plt.show()

root=Tk()
root.title("COVID TRACKER ")

entt=StringVar()
# p1=PhotoImage(file='covidd.png')
# root.iconphoto(False,p1)
p2='map.png'
img=ImageTk.PhotoImage(Image.open(p2))

x=root.winfo_x()
y=root.winfo_x()
root.geometry("+%d+%d" % (x+150,y+50))

main_frame=Frame(root)
main_frame.pack()
lb=Label(main_frame,image=img)
lb.pack()
top_frm=Frame(lb)
top_frm.pack()

lb1=Label(lb,text="COVID TRACKER",font=("arial",20),anchor="center",bg="black",fg="white")
lb1.pack(pady=50)

label=Label(lb)
label.pack(padx=50,pady=50)

label1=Label(label,text="ENTER COUNTRY NAME",font=("arial",10))
label1.grid(row=0,column=3,padx=20)
ent=Entry(label,width=50,textvariable=entt)
ent.grid(padx=5,row=0,column=9)

btn=Button(lb,text="ENTER",command=country)
btn.pack(pady=5)


label2=Label(lb,text="Here you can get the live COVID CASE UPDATES of any country.\nSearch your country name, and get the current covid case updates.\nStay HOME ,Stay SAFE.",bg="black",fg="white",font=("helvetica",12,"italic"))
label2.pack(pady=20)





root.mainloop()