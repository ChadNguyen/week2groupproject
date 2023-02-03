# Start Your Code here
# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

class ticket:


    def __init__(self, vehicle, quantity, pay, dailytotal):
        self.vehicle = vehicle
        self.quantity = quantity
        self.pay = pay
        self.dailytotal = dailytotal

    def vehicle_entering(self, small=1, oversize=1):
        self.quantity += small
        self.quantity += oversize



class ParkingSpaces:
    spaces = []

    def vehecle_parked(self, parkingspot=100, ):
        self.parkingspot -= parkingspot
     

    def vehecle_exiting(self, parkingspot=100, ):
        self.parkingspot += parkingspot
        




