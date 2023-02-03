# Start Your Code here
# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

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

    
    def vehicle_exiting(self, exiting=1):
        self.availablespaces -= exiting
        

    def driver():
        parking = True
        while parking:




        




