from payment import Payment

class CardPayment(Payment):
    def __init__(self, database):
        super(database)

    # retrieve information from card reader
    def retrieve_bank_info():
        return "John Wick, 1234 5678 0000 1234, 12/12, 211, 120"

    # verify card details
    def is_card_valid(self, bank_detail):
        return bank_detail == "John Wick, 1234 5678 0000 1234, 12/12, 211"

    # process card payment
    def process_payment(self):
        # mock bank payment process
        bank_detail = self.retrieve_bank_info()

        if self.is_card_valid(bank_detail[:-5]) and self.amount_is_sufficient(bank_detail[len(bank_detail)-4:]):
            return self.show_payment_status()
        else:
            return "Retry"

    # report payment status
    def show_payment_status():
        # mock payment status from bank
        # in this case, it is always success
        return "Success"