class Invoice():
    def __init__(self, payment):
        self.payment = payment
    
    # mock printing on invoice printing machine
    def print_invoice(self, amount_paid, is_cash_payment):
        print("Order Number: " + str(self.payment.order.id))
        print("Amount Total: " + str(self.payment.total_amount_due()))
        print("Amount Paid: " + str(amount_paid))
        if is_cash_payment:
            print("Change: " + str(self.payment.amount_paid - self.payment.total_amount_due()))
        print("Thank you for coming! Have a great day!")
