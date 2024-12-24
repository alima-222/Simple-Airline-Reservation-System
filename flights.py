import main_menu
import passenger
import flights
import mysql.connector as co
def fl_menu():
    while True:
        print("\t\t-----------------------------------------------")
        print("\t\t_____Welcome to Airline Reservation System_____")
        print("\t\t-----------------------------------------------")
        print("\t\t__________Azzy Airlines Travael Agent__________")
        print("1: Add Flight Details")
        print("2: Show all Flight Details")
        print("3: Search Flights")
        print("4: Deletion of records")
        print("5: Update flights")
        print("6: Return")    
        print("\t\t-----------------------------------------------")
        c=int(input("Enter your choice: "))
        if c==1:
            flights.fl_details()
        elif c==2:
            flights.fl_show()
        elif c==3:
            flights.fl_search()
        elif c==4:
            flights.fl_delete()
        elif c==5:
            flights.fl_update()
        elif c==6:
            return
        else:
            print("Error: Invalid Choice")
            conti="Press any key to return to Main menu"

def fl_details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
        cursor=mycon.cursor()
        a=int(input("Enter Flight No: "))
        b=input("Enter the Origin of flight: ")
        c=input("Enter the Destination of flight: ")
        d=int(input("Enter numner of seats available: "))
        e=int(input("Enter the ticket fare: "))

        query="INSERT INTO flights values(%s,%s,%s,%s,%s)"
        data=(a,b,c,d,e)
        cursor.execute(query,data)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved")
    except:
        print("error")
def fl_show():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    cursor.execute("select * from flights")
    data = cursor.fetchall()
    for row in data:
        print(row)
def fl_search():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter Flight No: "))
    q="select * from flights where flight_no='%s'"%(ab)
    cursor.execute(q)
    data=cursor.fetchall()
    print(data)
def fl_delete():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter Flight No: "))
    q="delete from flights where flight_no='%s'"%(ab)
    cursor.execute(q)
    mycon.commit()
    print("Data has been deleted")
def fl_update():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    
    print("\t\t---------------------------")
    print("\t\t-------UPDATE OPTIONS------")
    print("\t\t---------------------------")
    print("1: Edit Origin")
    print("2: Edit Destination")
    print("3: Edit Seats")
    print("4: Edit Fare")
    print("5: Return")
    print("\t\t---------------------------")
    c=int(input("Enter your choice: "))
    if c==1:
        flights.update_or()
    elif c==2:
        flights.update_de()
    elif c==3:
        flights.update_se()
    elif c==4:
        flights.update_fa()
    elif c==5:
         return
    else:
        print("Error: Invalid Choice")
        conti="Press any key to return to Main menu"
def update_or():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter Flight No: "))
    name=input("Enter the correct Origin of Flight: ")
    q="update flights set origin='%s' where flight_no='%s'"%(name,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
def update_de():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter Flight No: "))
    name=input("Enter the correct Destination of Flight: ")
    q="update flights set destination='%s' where flight_no='%s'"%(name,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
def update_se():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter Flight No: "))
    name=input("Enter the correct No of Seats : ")
    q="update flights set seats='%s' where flight_no='%s'"%(name,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
def update_fa():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter Flight No: "))
    name=input("Enter the correct Fare price: ")
    q="update flights set fare='%s' where flight_no='%s'"%(name,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
