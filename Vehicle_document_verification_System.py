import PIL.Image
import cv2
import easyocr
import numpy
import numpy as np
import imutils
from numpy import uint8
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
import tkinter as tk
import os.path

from mysql.connector.plugins import caching_sha2_password

root=Tk()
root.title("Login")
root.geometry('1500x1000')
root.configure(bg="#fff")
#root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
    if username=='admin' and password=='1234':
        root = Tk()
        frame = tk.Frame(root, bg='#45aaf2')
        lbl_pic_path = tk.Label(frame, text='Image Path:', padx=25, pady=25, font=('verdana', 16), bg='#45aaf2')
        lbl_show_pic = tk.Label(frame, bg='#45aaf2')
        entry_pic_path = tk.Entry(frame, font=('verdana', 11))
        btn_browse = tk.Button(frame, text='Select Image', bg='grey', fg='#ffffff', font=('verdana', 16))
        img=' '
        def selectPic():
            global img
            filename = filedialog.askopenfilename(initialdir="/final images", title="Select Image ",
                                                  filetypes=(("png images", ".png"), ("jpg images", ".jpg")))
            print(filename)
            img = Image.open("")
            img = ImageTk.PhotoImage(img)
            lbl_show_pic['image'] = img
            entry_pic_path.insert(0, filename)

        btn_browse['command'] = selectPic

        frame.pack()

        lbl_pic_path.grid(row=0, column=0)
        lbl_show_pic.grid(row=1, column=0, columnspan="2")
        entry_pic_path.grid(row=0, column=1, padx=(0, 40))
        btn_browse.grid(row=2, column=0, columnspan="2", padx=10, pady=10)

        root.mainloop()


       #screen=Toplevel(root)
       #screen.title("App")
       #screen.geometry('1200x800')
       #screen.config(bg='white')


    elif username!='admin' and password!='1234':
        messagebox.showerror("Invalid","Invalid Username and Password")
    elif password!='1234':
        messagebox.showerror("Invalid", "Invalid Password")
    elif Username!='admin':
        messagebox.showerror("Invalid", "Invalid Username")



#img=PhotoImage(file='gated-comm.jpg')
#img1=Label(root,image=img,bg='white').place(x=30,y=30)
image=Image.open('ANPR-Camera.jpg')
photo=ImageTk.PhotoImage(image)

label=Label(root,image=photo,bg='black').place(x=0,y=0)
frame=Frame(root,width=450,height=450,bg='white')
frame.place(x=500,y=100)

heading=Label(frame,text="Sign in",fg="#57a1f8",bg="white",font=('Arial Black',30,'bold'))
heading.place(x=150,y=50)

#####-----------------------------------------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e) :
    name=user.get()
    if name=='':
        user.insert(0,"Username")

user=Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=60,y=120)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=35,y=150)

####----------------------------------------------------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e) :
    name=code.get()
    if name=='':
        code.insert(0,"Password")
code=Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=60,y=170)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=35,y=200)

########--------------------------------------------------------------------------------------------------------------------
Button(frame,width=49,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=235)
label=Label(frame,text="Don't have an Account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=95,y=300)

Sign_up=Button(frame,width=6,text='Sign_up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
Sign_up.place(x=237,y=300)




root.mainloop()
root=Tk()
frame=tk.Frame(root,bg='#45aaf2')
lbl_pic_path=tk.Label(frame,text='Image Path:',padx=25,pady=25,font=('verdana',16),bg='#45aaf2')
lbl_show_pic=tk.Label(frame,bg='#45aaf2')
entry_pic_path=tk.Entry(frame,font=('verdana',11))
btn_browse=tk.Button(frame,text='Select Image',bg='grey',fg='#ffffff',font=('verdana',16))
filename=''


def selectPic():
    global img
    filename=filedialog.askopenfilename(initialdir="/images",title="Select Image ",filetypes=(("png images",".png"),("jpg images",".jpg")))
    img=Image.open(filename)
   # img=img.resize((100,100),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    lbl_show_pic['image']=img
    entry_pic_path.insert(0,filename)
    return img

btn_browse['command']=selectPic
print(type(filename))
img=filename

#print(type(imgpil))
#img=cv2.cvtColor(numpy.array(imgpil), cv2.COLOR_RGB2BGR)
#print(type(img))
# #absolute_path= os.path.dirname(filename)
#relative_path="src/lib"
#fullpath=os.path.join(absolute_path,relative_path)
#filename=os.path.abspath("")
#fullpath=filename+"\Screenshot.png"




frame.pack()

lbl_pic_path.grid(row=0,column=0)
lbl_show_pic.grid(row=1,column=0,columnspan="2")
entry_pic_path.grid(row=0,column=1,padx=(0,40))
btn_browse.grid(row=2,column=0,columnspan="2",padx=10,pady=10)

root.mainloop()






imj = cv2.imread("verified images/1679687584558.jpg")

cv2.imshow("window", imj)
cv2.waitKey(0)

img_gray = cv2.cvtColor(imj, cv2.COLOR_BGR2GRAY)
cv2.imshow("window", img_gray)
cv2.waitKey(0)

bfilter = cv2.bilateralFilter(img_gray, 11, 17, 17)  # noice reduction
edged = cv2.Canny(bfilter, 30, 200)  # edge detection
cv2.imshow("window", edged)
cv2.waitKey(0)
keypoints = cv2.findContours(edged.copy(), mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

location
mask = np.zeros(img_gray.shape, dtype=uint8)
new_img = cv2.drawContours(mask, [location], 0, 255, -1)
# cv2.imshow("Window",mask)
# cv2.waitKey(0)
new_img = cv2.bitwise_and(imj, imj, mask=mask)

cv2.imshow("Window", new_img)
cv2.waitKey(0)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_img = img_gray[x1:x2 + 1, y1:y2 + 1]

cv2.imshow("window", cropped_img)
cv2.waitKey(0)

reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_img)

x=str(result[0][1])
print(x)
print(type(x))


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='BTCS_G65',
    port='3306',
    database='btcs_g65')

mycursor = mydb.cursor()
print("Vehicle_ID  ","  Name      ","    Aadhar_no   ","    Insurance_no  "," License_no    ","  PUC_registration_no")
Query="Select * from vehicle_details where Vehicle_ID=%(T)s"
mycursor.execute(Query,{'T':x})

for i in mycursor:
    print(type(i))
    print(i)
    Vehicleid=i[0]
    Name=i[1]
    Aadharno=i[2]
    InsurenceNo=i[3]
    Licence_no=i[4]
    Puc=i[5]
mydb.close()

root=Tk()
root.geometry('1500x1000')
root.configure(bg="pink")
image=Image.open('FINAL.jpg')
photo=ImageTk.PhotoImage(image)
label=Label(root,image=photo,bg='black',height=600,width=600).place(x=800,y=150)


Label(root,text='Verification Result',font=("ArialBlack",25,'bold'),pady=50,bg="pink").grid(row=0,column=2)
OName=Label(root,text="Owner Name",font=("comicsansms 12 bold"),pady=30,bg="pink")
Adhar = Label(root,text="Adhar Number",font=("comicsansms 12 bold"),pady=30,bg="pink")
Insurance=Label(root,text="Insurance Number",font=("comicsansms 12 bold"),pady=30,bg="pink")

Licence=Label(root,text="Licence Number",font=("comicsansms 12 bold"),pady=30,bg="pink")
PUC=Label(root,text="PUC Registration Number",font=("comicsansms 12 bold"),pady=30,bg="pink")

OName.grid(row=1,column=1)
Adhar.grid(row=4,column=1)
Insurance.grid(row=7,column=1)
Licence.grid(row=10,column=1)
PUC.grid(row=13,column=1)

name=Label(root,text=Name,font=("comicsansms 12 bold"),pady=30,bg="pink")
an=Label(root,text=Aadharno,font=("comicsansms 12 bold"),pady=30,bg="pink")
In=Label(root,text=InsurenceNo,font=("comicsansms 12 bold"),pady=30,bg="pink")
Ln=Label(root,text=Licence_no,font=("comicsansms 12 bold"),pady=30,bg="pink")
puc=Label(root,text=Puc, font=("comicsansms 12 bold"),pady=30,bg="pink")

name.grid(row=1,column=3)
an.grid(row=4,column=3)
In.grid(row=7,column=3)
Ln.grid(row=10,column=3)
puc.grid(row=13,column=3)
root.mainloop()

