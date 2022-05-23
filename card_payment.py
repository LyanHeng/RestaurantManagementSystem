from payment import Payment

class CardPayment(Payment):
    def __init__(self, database, order):
        super().__init__(database, order)

    # retrieve information from card reader
    def retrieve_bank_info(self):
        return "John Wick, 1234 5678 0000 1234, 12/12, 211, 120.0"

    # verify card details
    def is_card_valid(self, bank_detail):
        return bank_detail == "John Wick, 1234 5678 0000 1234, 12/12, 211"

    # process card payment
    def process_payment(self):
        # mock bank payment process
        bank_detail = self.retrieve_bank_info()
        bank_info = bank_detail[:-7]
        amount_in_account = float(bank_detail[len(bank_detail)-6:])

        if self.is_card_valid(bank_info) and self.amount_is_sufficient(amount_in_account):
            self.amount_paid = self.total_amount_due()
            return self.show_payment_status()
        else:
            return "Retry"

    # report payment status
    def show_payment_status(self):
        # mock payment status from bank
        # in this case, it is always success
        return "Success"