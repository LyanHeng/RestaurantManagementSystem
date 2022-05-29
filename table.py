from collections import namedtuple

class Table():
    def __init__(self, id, size, state):
        self.id = id
        self.size = size
        self.state = state

    #display items currently in the menu with format
    def display_table(tables):
        TableEntry = namedtuple('TableEntry', ['id','size','state'])
        _table = []
        for t in tables:
            _table.append(TableEntry(t.id, t.size, t.state))

        for entry in _table:
            id = str(getattr(entry,'id')).ljust(5)
            size = str(getattr(entry,'size')).ljust(25)
            state = str(getattr(entry,'state')).ljust(10)
            print ('{0}{1}{2}'.format(id,size,state))