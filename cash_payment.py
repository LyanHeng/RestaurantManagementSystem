from payment import Payment

class CashPayment(Payment):
    def __init__(self, database, order):
        super().__init__(database, order)

    # trigger cash register to open
    def open_register(self):
        # mock register being opened and closed, given the input amount
        return 500.0

    # process cash payment
    def process_payment(self):
        amount_got = self.open_register()
        if self.amount_is_sufficient(float(amount_got)):
            self.amount_paid = amount_got
            return "Success"
        else:
            return "Retry"