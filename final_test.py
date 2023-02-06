class ParkingGarage:
    def __init__(self, space_qty=100):
        self.space_qty = space_qty
        self.open_spaces = space_qty
        
    def enter(self, customer_qty):
        self.open_spaces -= customer_qty
        if self.open_spaces >= 0:
            print(f'Welcome to the parking garage! Enjoy your time here!')
        else:
            print('Sorry, there are no more available parking spaces.')
    
    def leave(self, customer_qty):
        self.open_spaces += customer_qty
        print('Goodbye, thank you for coming! Have a wonderful day!')

class ParkingTicket:
    def __init__(self, ticket_num=100):
        self.ticket_num = ticket_num
        self.tickets = [{"number": i, "paid": False} for i in range(ticket_num)]
        self.current_ticket = None
    
    def take_ticket(self, customer_qty):
        if len(self.tickets) >= customer_qty:
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
        if payment >= 10 * customer_qty:
            print("Your tickets have been paid. You have 15 minutes to leave.")
        for i in range(customer_qty):
            self.current_tickets[i]["paid"] = True

        else:
            print("Payment must be at least $10 per vehicle.")
    
    def leave_garage(self, customer_qty):
        if len(self.current_tickets) == customer_qty:
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
parking_garage.enter(customer_qty)
parking_ticket.take_ticket(customer_qty)
parking_ticket.pay_for_parking(customer_qty)
parking_ticket.leave_garage(customer_qty)
parking_garage.leave(customer_qty)

