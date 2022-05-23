from asyncio.windows_events import NULL
from database import Database
from invoice import Invoice
from order import Order

class Payment():
    def __init__(self, database, order):
        self.database = database
        if not order:
            self.order = Order(NULL, NULL, NULL)
        else:
            self.order = order
        self.state = "Empty"
        self.amount_paid = 0.0

    # create a new transaction
    def create_transaction(self):
        while True:
            order_id = input("Enter order id (<order id>/exit): ")
            if order_id == "exit":
                return -1
            # order does not exist in database
            order = self.database.get_order(order_id)
            if not order:
                print("Order does not exist")
                continue
            # calculate total amount due
            self.order = order
            amount_due = self.total_amount_due()
            self.state = "Running"
            return amount_due

    # calculate total amount due
    def total_amount_due(self):
        total = 0.0
        for item_id in self.order.item_ids:
            item = self.database.get_item(item_id)
            # this should never happen if application creates item objects properly
            if not item:
                print("Unexpected Error: item does not exist in database")
                return -1
            total += item.price
        return total

    # check that amount paid is correct
    def amount_is_sufficient(self, amount):
        if amount >= self.total_amount_due():
            return True
        else:
            return False

    # state monitor to retry payment
    def retry_payment(self):
        return self.state == "Retry" or self.state == "Running"

    # print invoice 
    def print_invoice(self, is_cash_payment):
        self.state = "Success"
        # mock communication to invoice printer
        invoice = Invoice(self)
        invoice.print_invoice(self.amount_paid, is_cash_payment)

    ### ABSTRACT METHODS ###
    # process payment class
    def process_payment():
        return 