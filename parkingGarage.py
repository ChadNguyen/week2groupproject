class Garagelot:
    def __init__(self, vehicle, pay=10, dailytotal={}, availablespaces=100, tickets=0,):
        self.vehicle = vehicle
        self.pay = pay
        self.dailytotal = dailytotal
        self.availablespaces = availablespaces
        self.tickets = tickets

        self.dailytotal = {
            'availablespaces': 100,
            'tickets': 0,
            'pay': 10,

        }


    def vehicle_entering(self, parked=1, sold_tickets=1):
        self.availablespaces -= parked
        self.tickets += sold_tickets 
        if self.availablespaces >= 0:
            print('Please grab the ticket dispensed and proceed to the available space to park. ')
        else:
            print('Sorry, there are no more available parking spaces.')


    
    def vehicle_exiting(self, exiting=1):
        self.availablespaces += exiting
        print('Goodbye, thank you for coming! Have a wonderful day!')



    def payForParking(self):
        amount_owed = self.pay
        user_choice = input('Enter your choice (b): ')
        if user_choice == 'b':
            while amount_owed == 10:
                print(f'Your Cost to park at Cz Garagelot today is ${amount_owed}')
                total = input('Please Enter the amount you want to pay:  ')
                if total == str(amount_owed):
                    self.vehicle_exiting()
                print('Goodbye, thank you for coming! Have a wonderful day! The ticket is valid for 15 mins to exit')
                return
                
        
    def driver(self):
        price = self.pay
        amount_owed = price
        while True:
            user_choice = input('Hello! Welcome to CZ Garage, how can we help you today? (a) Take ticket and park, (b) Pay and leave garage, (c) Show Total Availability for parking. Please Choose options (a/b/c):  ').lower()
            if user_choice == 'a':
                print('Please grab the ticket dispensed and proceed to the available space to park. ')
                self.vehicle_entering()
                break
            elif user_choice == 'b':
                if amount_owed == 10:
                    print(f'Your Cost to park at Cz Garagelot today is ${amount_owed}')
                    total = input('Please Enter the amount you want to pay:  ').lower()
                    if total == str(amount_owed):
                        self.vehicle_exiting()
                        print('Goodbye, thank you for coming! Have a wonderful day! The ticket is valid for 15 mins to exit')
                        break
            elif user_choice == 'c':
                print(f'The total available spaces currently is {self.availablespaces}')
                break
            else:
                print('Please try again with a valid input option')
Garagelot.driver()
                



        





