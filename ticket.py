class Tickets:
    def __init__(self, cost, amount):
        self.cost = cost
        self.amount = amount

    def full_amount_for_tickets_accounting_for_inflation(self):
        total_cost = self.cost*self.amount
        return f"total cost for tickets is {total_cost}€"

class student_ticket(Tickets):
    def full_amount_for_tickets_accounting_for_inflation(self):
        total_cost = self.cost*self.amount - (self.cost*self.amount*0.15)
        return f"total cost for a discounted ticket is {total_cost}€"

class oldPeopleTicket(student_ticket):
    def full_amount_for_tickets_accounting_for_inflation(self):
        return super().full_amount_for_tickets_accounting_for_inflation()


ticketPriceNormal = Tickets(10, 73)
ticketPriceStudent = student_ticket(10, 73)
ticketPriceOld = oldPeopleTicket(10, 73)

print(ticketPriceNormal.full_amount_for_tickets_accounting_for_inflation())
print(ticketPriceStudent.full_amount_for_tickets_accounting_for_inflation())
print(ticketPriceOld.full_amount_for_tickets_accounting_for_inflation())
