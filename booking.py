from table import Table

class Booking():
    def __init__(self, id, name, time, table):
        self.id = id
        self.name = name
        self.time = time
        self.table = table

    def show_bookings(bookings):
        print("Current Bookings: ")
        print()
        id = 'Id'.ljust(5)
        name = 'Name'.ljust(25)
        time = 'Time'.ljust(10)
        table = 'Table'.ljust(7)
        print('{0}{1}{2}{3}'.format(id, name, time, table))
        for booking in bookings:
            id = str(getattr(booking,'id')).ljust(5)
            name = str(getattr(booking,'name')).ljust(25)
            time = str(getattr(booking,'time')).ljust(10)
            table = str(getattr(booking,'table')).ljust(7)
            print('{0}{1}{2}{3}'.format(id,name,time,table))
