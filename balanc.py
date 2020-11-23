class Client:
    def __init__(self, name, sname, balance):
        self.name = name
        self.sname = sname
        self.balance = balance

    def get_client_info(self):
        return f'"{self.name} {self.sname}". Balance: {self.balance} rub.'


new_client1 = Client('Ivan', 'Ivanov', 50)
new_client2 = Client('Petor', 'Petrovich', 32)

print(new_client1.get_client_info())

print(new_client2.get_client_info())
