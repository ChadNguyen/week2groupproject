class ParkingGarage:
    def __init__(self,parkingspace=100):
        self.parkingspace = parkingspace

    def enter(self,taken_space):
        self.taken_space = 1
        self.parkingspace -= taken_space
        if self.parkingspace >= 0:
            print(f'Welcome to the parking garage! Enjoy your time here!')
        else:
            print('Sorry, there are no more available parking spaces.')

    
    def leave(self,taken_space):
        self.taken_space = 1
        self.parkingspace += taken_space
        print('Goodbye, thank you for coming! Have a wonderful day!')

class ParkingTicket:
    def init(self, ticket_num=100):
        self.ticket_num = ticket_num
        self.tickets = [{"number": i, "paid": False} for i in range(ticket_num)]
        self.current_ticket = None

    def take_ticket(self, customer_qty):
        if len(self.tickets) >= taken_space:
            self.current_tickets = [self.tickets.pop() for i in range(customer_qty)]
            print(f"{len(self.tickets)} tickets left. Please pay for parking.")
        else:
            print("Sorry, there are no more available tickets.")

    def pay_for_parking(self, customer_qty):
        if not self.current_tickets:
            print("No ticket has been taken.")
            return

        payment = input("Please enter payment amount: ")
        payment = int(payment)
        if payment >= 10 * taken_space:
            print("Your tickets have been paid. You have 15 minutes to leave.")
        for i in range(taken_space):
            self.current_tickets[i]["paid"] = True

        else:
            print("Payment must be at least $10 per vehicle.")

    def leave_garage(self, customer_qty):
        if len(self.current_tickets) == taken_space:
            all_paid = True
        for ticket in self.current_tickets:
            if not ticket["paid"]:
                all_paid = False
                break
        if all_paid:
            print("Thank you, have a nice day!")
            self.current_tickets = []
        else:
            print("Not all tickets have been paid for.")

parking_garage = ParkingGarage()
parking_ticket = ParkingTicket()

customer_qty = int(input("Welcome to the parking garage! How many cars do you have? "))
parking_garage.enter(taken_space)
parking_ticket.take_ticket(taken_space)
parking_ticket.pay_for_parking(taken_space)
parking_ticket.leave_garage(taken_space)
parking_garage.leave(taken_space)
