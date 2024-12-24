import main_menu
import passenger
import flights
import bookings
import report
while True:
    print("\t\t-----------------------------------------------")
    print("\t\t_____Welcome to Airline Reservation System_____")
    print("\t\t-----------------------------------------------")
    print("\t\t__________Azzy Airlines Travael Agent__________")
    print("1: Passenger")
    print("2: Flights")
    print("3: Bookings")
    print("4: Graphical Report")
    print("5: Exit")
    print("\t\t-----------------------------------------------")
    c=int(input("Enter your choice: "))
    if c==1:
        passenger.ps_menu()
    elif c==2:
        flights.fl_menu()
    elif c==3:
        bookings.bk_menu()
    elif c==4:
        report.rp_menu()
    elif c==5:
        break
    else:
        print("Error: Invalid Choice")
        conti="Press any key to return to Main menu"
    
    
    
