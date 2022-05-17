from card_payment import CardPayment
from cash_payment import CashPayment
from database import Database
from item import Item
from payment import Payment

def main():
    
    database = Database()
    """
    # delete current menu
    for item in database.get_menu().items:
        database.delete_menu_item(item.id)

    database.create_menu_item(Item(1, "Test1", 10, ["ingredient1", "ingredient2", "ingredient3"]))
    database.create_menu_item(Item(2, "Test2", 10, ["ingredient1", "ingredient2"]))
    database.create_menu_item(Item(3, "Test3", 10, ["ingredient1", "ingredient2", "ingredient3", "ingredient4"]))

    #database.delete_menu_item()

    database.create_menu_item(Item(3, "Testchange3", 90, ["ingredient1", "ingredient2", "ingredient3", "ingredient4", "ingredient5"]))

    database.delete_menu_item(2)

    print(database.get_menu().items)
    """

    # workflow for payment
    payment = Payment(database)
    amount_due = payment.create_transaction()
    if amount_due != -1:
        while payment.retry_payment():
            print("The amount due for payment is: " + str(amount_due))
            payment_method = input("Pay by card or cash? (card/cash/exit): ")
            # determines payment method
            if payment_method == "card":
                payment_method = CardPayment(database)
            elif payment_method == "cash":
                payment_method = CashPayment(database)
            elif payment_method == "exit":
                payment.state = "Failed"
                print(payment.state)
                continue
            payment.state = payment_method.process_payment()
            # print invoice if success, offers retry if failed
            if payment.state == "Success":
                Payment.print_invoice(amount_due)
            print(payment.state)
    print("Payment completed/exited")

if __name__ == "__main__":
    main()