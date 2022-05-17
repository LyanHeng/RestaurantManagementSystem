from payment import Payment

class CashPayment(Payment):
    def __init__(self):
        super(self)

    # trigger cash register to open
    def open_register():
        # mock register being opened and closed, given the input amount
        return 12

    # process cash payment
    def process_payment(self):
        amount_got = self.open_register()
        if self.amount_is_sufficient(amount_got):
            return "Success"
        else:
            return "Retry"