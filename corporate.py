class CorporateGuests:
    def __init__(self, name='', sname='', adress='', status=''):
        self.name = name
        self.sname = sname
        self.adress = adress
        self.status = status

    def __str__(self):
        return f'"{self.name} {self.sname}", г. "{self.adress}", Статус: "{self.status}"'


class Mentor(CorporateGuests):
    def __init__(self, name, sname, adress, status, lvl=0):
        super().__init__(name, sname, adress, status)
        self.lvl = lvl

    def __str__(self):
        if self.lvl > 0:
            return f'"{self.name} {self.sname}", г. "{self.adress}", Статус: "{self.status} lvl= {self.lvl}"'
        else:
            return f'"{self.name} {self.sname}", г. "{self.adress}", Статус: "{self.status}"'


class Volunteer(CorporateGuests):
    def __init__(self, name, sname, adress, status, donat=0):
        super().__init__(name, sname, adress, status, )
        self.donat = donat

    def __str__(self):
        if self.donat > 0:
            return f'"{self.name} {self.sname}", г. "{self.adress}", Статус: "{self.status}" пожертвовал {self.donat} рублей '
        else:
            return f'"{self.name} {self.sname}", г. "{self.adress}", Статус: "{self.status}" Ничего не пожертвовал'


guest_m_1 = Mentor('ivan', 'ivanov', 'ivanovka', 'mentor', 23)
guest_v_1 = Volunteer('Bruce', 'Wayne', 'Gotem', 'Volunteer', 44)
guest_v_2 = Volunteer('Ron', 'Vizli', 'Hogvards', 'Volunteer')

guests = [guest_m_1, guest_v_1, guest_v_2]

for guest in guests:
    if isinstance(guest, Mentor):
        print(guest.__str__())
    else:
        print(guest.__str__())
