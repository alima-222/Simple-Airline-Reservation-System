import main_menu
import report
import mysql.connector as co
import matplotlib.pyplot as plt
import numpy as np
def rp_menu():
    while True:
        print("\t\t-----------------------------------------------")
        print("\t\t_____Welcome to Airline Reservation System_____")
        print("\t\t-----------------------------------------------")
        print("\t\t__________Azzy Airlines Travael Agent__________")
        print("1: Flights available origin wise")
        print("2: Flights available destination wise")
        print("3: Return")    
        print("\t\t-----------------------------------------------")
        c=int(input("Enter your choice: "))
        if c==1:
            report.rp_r()
        elif c==2:
            report.rp_q()
        elif c==3:
            return
        else:
            print("Error: Invalid Choice")
            conti="Press any key to return to Main menu"

def rp_r():
    mycon = co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor = mycon.cursor()
    
    # Get distinct origins
    cursor.execute("SELECT DISTINCT origin FROM flights ORDER BY origin ASC")
    data = cursor.fetchall()
    origins = [row[0] for row in data]
    print("Distinct origins:", origins)
    
    # Count origins
    cursor.execute("SELECT origin, COUNT(origin) FROM flights GROUP BY origin ORDER BY origin ASC")
    data = cursor.fetchall()
    counts = [row[1] for row in data]
    print("Origin counts:", counts)
    
    # Plot bar chart
    plt.bar(origins, counts, color='skyblue')
    plt.title('Flights Available Origin-Wise')
    plt.xlabel('Origin')
    plt.ylabel('Number of Flights')
    plt.show()

def rp_q():
    mycon = co.connect(host="localhost", user="root", passwd="", database="ars")
    cursor = mycon.cursor()
    
    # Get distinct destinations
    cursor.execute("SELECT DISTINCT destination FROM flights ORDER BY destination ASC")
    data = cursor.fetchall()
    destinations = [row[0] for row in data]
    print("Distinct destinations:", destinations)
    
    # Count destinations
    cursor.execute("SELECT destination, COUNT(destination) FROM flights GROUP BY destination ORDER BY destination ASC")
    data = cursor.fetchall()
    counts = [row[1] for row in data]
    print("Destination counts:", counts)
    
    # Plot bar chart
    plt.bar(destinations, counts, color='salmon')
    plt.title('Flights Available Destination-Wise')
    plt.xlabel('Destination')
    plt.ylabel('Number of Flights')
    plt.show()
