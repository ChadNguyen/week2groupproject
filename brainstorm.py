


# spaces increase and decrease: done
# cars entering exiting ticket count increase: done
# pay diallogue: half done
# parkingspace list: not done
# tickets: half done(need total count at end of the day)                               /



# Your parking gargage class should have the following methods:
# takeTicket
# This should decrease the amount of tickets available by 1 ##################### DONE
# This should decrease the amount of parkingSpaces available by 1 ##################### DONE



#  payForParking-half
#  Display an input that waits for an amount from the user and store it in a variable
#  If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#  This should update the "currentTicket" dictionary key "paid" to True




#  leaveGarage
#  If the ticket has been paid, display a message of "Thank You, have a nice day"
#  If the ticket has not been paid, display an input prompt for payment
#  Once paid, display message "Thank you, have a nice day!"
#  Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#  Update tickets list to increase by 1 (meaning add to the tickets list)
class ParkingGarage:
    def init(self, space_qty=100):
        self.space_qty = space_qty
        self.open_spaces = space_qty
        self.tickets = [{"number": i, "paid": False} for i in range(space_qty)]
        self.current_ticket = None

    def vehicle_entering(self, customer_qty=1):
        if self.open_spaces - customer_qty >= 0:
            print("Here is your ticket. Enjoy your stay!")
            self.open_spaces -= customer_qty
            self.current_ticket = self.tickets[self.space_qty - self.open_spaces - 1]
        else:
            print("Sorry, there are no more available parking spaces.")

    def payForParking(self):
        if self.current_ticket and not self.current_ticket["paid"]:
            payment = input("Please enter your payment:")
            self.current_ticket["paid"] = True
            print("Thank you for paying!")
        else:
            print("No payment necessary or ticket has already been paid.")

    def leaveGarage(self):
        if self.current_ticket and self.current_ticket["paid"]:
            print("Thank you, have a nice day!")
            self.open_spaces += 1
            self.tickets.append({"number": self.space_qty + 1, "paid": False})
        else:
            payment = input("Have you paid your ticket? (yes/no)")
            if payment.lower() == "yes":
                print("Thank you, have a nice day!")
                self.open_spaces += 1
                self.current_ticket = None
                self.tickets.append({"number": self.space_qty + 1, "paid": False})
                self.space_qty += 1
            elif payment.lower() == "no":
                self.payForParking()
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def driver():
        price = 10
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
                        self.leaveGarage()
                        print('Goodbye, thank you for coming! Have a wonderful day! The ticket is valid for 15 mins to exit')
                        break
            elif user_choice == 'c':
                print(f'The total available spaces currently is {self.space_qty}')
                break
            else:
                print('Please try again with a valid input option')

parking_garage = ParkingGarage()
customer_qty = int(input("Welcome to the parking garage! How many tickets do you need? "))
parking_garage.vehicle_entering(customer_qty)
parking_garage.payForParking()
parking_garage.leaveGarage()