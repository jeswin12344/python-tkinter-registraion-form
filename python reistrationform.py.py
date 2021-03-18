from tkinter import *
root = Tk()
root.geometry("500x300")
def getvals():
    print("Accepted")



#Heading
Label(root, text= "Python Registration Form", font="sansserif").grid(row=0, column=3)
#field name
name= Label (root, text="Name")
Phone= Label(root, text="Phone")
gender= Label(root, text="Gender")
emergency= Label(root, text="Emergency")
Paymentmethod= Label(root, text="Payment Method")
# packing fields
name.grid( row=1, column=2)
Phone.grid( row=2, column=2)
gender.grid( row=3, column=2)
emergency.grid( row=4, column=2)
Paymentmethod.grid( row=5, column=2)
# variable for storing data
namevalue = StringVar
Phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
Paymentmethodvalue = StringVar
chekvalue=IntVar

 
# Creating entry field 
nameentry = Entry( root, textvariable =namevalue)
Phoneentry = Entry( root, textvariable =Phonevalue)
genderentry = Entry( root, textvariable =gendervalue)
paymentmethodentry = Entry( root, textvariable =Paymentmethodvalue)
emergencyentry = Entry( root, textvariable =emergencyvalue)
# packing entry field
nameentry.grid(row=1, column=3)
Phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmethodentry.grid(row=5, column=3)

 # creating checkbox 
checkbtn = Checkbutton( text="remember me?", variable = chekvalue)
checkbtn.grid(row=6, column=3)

# submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

  

  
root.mainloop()