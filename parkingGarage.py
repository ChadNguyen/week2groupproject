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


        





