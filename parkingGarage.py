# Start Your Code here
class ParkingGarage:
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
