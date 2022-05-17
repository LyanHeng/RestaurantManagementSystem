from payment import Payment

def main():
    print("Make a payment")
    payment = Payment()
    payment.create_transaction()

if __name__ == "__main__":
    main()