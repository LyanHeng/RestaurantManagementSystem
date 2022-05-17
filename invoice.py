class Invoice():
    def __init__(self, payment):
        self.payment = payment
    
    # mock printing on invoice printing machine
    def print_invoice(self, amount_paid):
        print("Order Number: " + self.payment.order.id)
        print("Amount Total: " + self.payment.total_amount_due())
        print("Amount Paid: " + amount_paid)
        print("Thank you for coming! Have a great day!")
