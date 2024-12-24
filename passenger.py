import main_menu
import passenger
import mysql.connector as co
def ps_menu():
    while True:
        print("\t\t-----------------------------------------------")
        print("\t\t_____Welcome to Airline Reservation System_____")
        print("\t\t-----------------------------------------------")
        print("\t\t__________Azzy Airlines Travael Agent__________")
        print("1: Add Passenger Details")
        print("2: Show Passenger Details")
        print("3: Search Passenger records")
        print("4: Deletion of passenger details")
        print("5: Update Passenger")
        print("6: Return")
        print("\t\t-----------------------------------------------")
        c=int(input("Enter your choice: "))
        if c==1:
            passenger.ps_details()
        elif c==2:
            passenger.ps_show()
        elif c==3:
            passenger.ps_search()
        elif c==4:
            passenger.ps_delete()
        elif c==5:
            passenger.ps_update()
        elif c==6:
            return
        else:
            print("Error: Invalid Choice")
            conti="Press any key to return to Main menu"

def ps_details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
        cursor=mycon.cursor()
        a=int(input("Enter ID No: "))
        b=input("Enter your name: ")
        c=int(input("Enter your age: "))
        d=input("Enter your gender(M/F): ")
        e=int(input("Enter your mobile number: "))

        query="INSERT INTO passenger values(%s,%s,%s,%s,%s)"
        data=(a,b,c,d,e)
        cursor.execute(query,data)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved")
    except:
        print("error")
    #except co.error as err:
        #if err.error==errorcode.ER ACCESS SENIES ERROR:
         #    print("Something is invalid...Re.Check User name or password
        #if err.errno==errorcode.ER_BAD_DB_ERROR:
         #    print("Admission:DATABASE does not exist..")
        #else:
         #print(err)
def ps_show():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    cursor.execute("select * from passenger")
    data = cursor.fetchall()
    for row in data:
        print(row)
def ps_search():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID no: "))
    q="select * from passenger where id_no='%s'"%(ab)
    cursor.execute(q)
    data=cursor.fetchall()
    print(data)
def ps_delete():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID no: "))
    q="delete from passenger where id_no='%s'"%(ab)
    cursor.execute(q)
    mycon.commit()
    print("Data has been deleted")
def ps_update():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    
    print("\t\t---------------------------")
    print("\t\t-------UPDATE OPTIONS------")
    print("\t\t---------------------------")
    print("1: Edit name")
    print("2: Edit age")
    print("3: Edit mobile_no")
    print("4: Return")
    print("\t\t---------------------------")
    c=int(input("Enter your choice: "))
    if c==1:
        passenger.update_name()
    elif c==2:
        passenger.update_age()
    elif c==3:
        passenger.update_mob()
    elif c==4:
         return
    else:
        print("Error: Invalid Choice")
        conti="Press any key to return to Main menu"
def update_name():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID no: "))
    name=input("Enter your correct name: ")
    q="update passenger set Name='%s' where id_no='%s'"%(name,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
def update_age():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID no: "))
    age=int(input("Enter your correct age: "))
    q="update passenger set Age='%s' where id_no='%s'"%(age,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
def update_mob():
    mycon=co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor=mycon.cursor()
    ab=int(input("Enter ID no: "))
    mob=int(input("Enter your correct mobile number: "))
    q="update passenger set mobile ='%s' where id_no='%s'"%(mob,ab)
    cursor.execute(q)
    mycon.commit()
    print("Data updated succesfully")
        


                     
