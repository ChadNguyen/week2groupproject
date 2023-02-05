# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# Start Your Code here

class Garagelot:
    def __init__(self, vehicle, pay=10, dailytotal, availablespaces=100, tickets=0,):
        self.vehicle = vehicle
        self.pay = pay
        self.dailytotal = dailytotal
        self.availablespaces = availablespaces
        self.tickets = tickets


    def vehicle_entering(self, parked=1, sold_tickets=1):
        self.availablespaces += parked
        self.tickets += sold_tickets 
        if self.availablespaces >= 0:
            print('Welcome to the parking garage! Enjoy your time here!')
        else:
            print('Sorry, there are no more available parking spaces.')

    
    def vehicle_exiting(self, exiting=1):
        self.availablespaces -= exiting
        print('Goodbye, thank you for coming! Have a wonderful day!')
        

    def driver():
        parking = True
        while parking:

class ParkingGarage:
    ticket = 0

    def __init__(self, space_qty=100):
        self.space_qty = space_qty
        self.open_spaces = space_qty
        
    def enter(self, customer_qty):
        self.open_spaces -= customer_qty
        if self.open_spaces >= 0:
            print('Welcome to the parking garage! Enjoy your time here!')
        else:
            print('Sorry, there are no more available parking spaces.')
    
    def leave(self, customer_qty):
        self.open_spaces += customer_qty
        print('Goodbye, thank you for coming! Have a wonderful day!')
    def leave(self, customer_qty):
        self.open_spaces += customer_qty
        print('Goodbye, thank you for coming! Have a wonderful day!')

    def leaveGarage(self):
        while not paid:
            payment = input("Have you paid your ticket? (yes/no)")
            if payment.lower() == "yes":
                paid = True
                print("Thank you, have a nice day!")
            elif payment.lower() == "no":
                payment = input("Please enter your payment:")
                print("Thank you, have a nice day!")
                paid = True
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        self.open_spaces += 1
    
    def takeTicket(self, customer_qty):
        if self.open_spaces - customer_qty >= 0:
            print("Here is your ticket. Enjoy your stay!")
            self.enter(customer_qty)
        else:
            print("Sorry, there are no more available parking spaces.")
        self.ticket += 1
