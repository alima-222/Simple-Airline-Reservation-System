import main_menu
import bookings
import flights
import mysql.connector as co
def bk_menu():
    while True:
        print("\t\t-----------------------------------------------")
        print("\t\t_____Welcome to Airline Reservation System_____")
        print("\t\t-----------------------------------------------")
        print("\t\t__________Azzy Airlines Travael Agent__________")
        print("1: Make a new Booking")
        print("2: Show all Bookings")
        print("3: Search booking")
        print("4: Delete a booking")
        print("5: Update bookings")
        print("6: Return")    
        print("\t\t-----------------------------------------------")
        c=int(input("Enter your choice: "))
        if c==1:
            bookings.bk_details()
        elif c==2:
            bookings.bk_show()
        elif c==3:
            bookings.bk_search()
        elif c==4:
            bookings.bk_delete()
        elif c==5:
            bookings.bk_update()
        elif c==6:
            return
        else:
            print("Error: Invalid Choice")
            conti="Press any key to return to Main menu"
def bk_details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
        cursor=mycon.cursor()
        cursor.execute("select * from flights")
        data = cursor.fetchall()
        print("The available flights are:")
        for row in data:
            print(row)
        print("\n*MAKE SURE TO REGIESTER YOUR DETAILS IN PASSENGER TABLE BEFORE BOOKING*")
        p=int(input("\nType 1 to continue and 2 ro return to Main Menu: "))
        if p==1:
            a=int(input("Enter your ID No: "))
            b=input("Enter your Name: ")
            c=int(input("Enter the Flight No: "))
            d=int(input("Enter numner of seats to be reserved: "))
            e=input("Enter the class type: ")

            query="INSERT INTO bookings values(%s,%s,%s,%s,%s)"
            data=(a,b,c,d,e)
            cursor.execute(query,data)
            
            mycon.commit()
            mycon.close()
            cursor.close()
            mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
            cursor=mycon.cursor()
            fare="select fare from flights where flight_no='%s'"%(c)
            cursor.execute(fare)
            o=cursor.fetchall()
            z=o[0]
            x=z[0]
            mycon.commit()
            mycon.close()
            cursor.close()
            print("Record has been saved")
            print ("You have reserved",d,"seats for Flight no",c,"for",e,"class")
            print("Your Total amount is:",int(x)*d)
        if p==2:
            return
    except:
        print("error")
def bk_show():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    cursor.execute("select * from bookings")
    data = cursor.fetchall()
    for row in data:
        print(row)
def bk_search():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID No: "))
    q="select * from bookings where id_no='%s'"%(ab)
    cursor.execute(q)
    data=cursor.fetchall()
    print(data)
def bk_delete():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID No: "))
    q="delete from bookings where id_no='%s'"%(ab)
    cursor.execute(q)
    mycon.commit()
    print("Data has been deleted")
def bk_update():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    
    print("\t\t---------------------------")
    print("\t\t-------UPDATE OPTIONS------")
    print("\t\t---------------------------")
    print("1: Edit Name")
    print("2: Edit Flight No")
    print("3: Edit Seats")
    print("4: Edit Class")
    print("5: Return")
    print("\t\t---------------------------")
    c=int(input("Enter your choice: "))
    if c==1:
        bookings.update_na()
    elif c==2:
        bookings.update_fl()
    elif c==3:
        bookings.update_se()
    elif c==4:
        bookings.update_cl()
    elif c==5:
         return
    else:
        print("Error: Invalid Choice")
        conti="Press any key to return to Main menu"
def update_na():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID No: "))
    name=input("Enter the correct Name: ")
    q="update bookings set name='%s' where id_no='%s'"%(name,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
def update_se():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter Flight No: "))
    name=input("Enter the correct number of seats: ")
    q="update bookings set seats='%s' where id_no='%s'"%(name,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
def update_cl():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID No: "))
    name=input("Enter the correct class: ")
    q="update bookings set class='%s' where id_no='%s'"%(name,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
def update_fl():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID No: "))
    name=input("Enter the Flight No: ")
    q="update bookings set flight_no='%s' where id_no='%s'"%(name,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")



