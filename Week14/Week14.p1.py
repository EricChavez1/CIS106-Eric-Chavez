class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def compute_bonus(self, bonus_rate):
        return self.pay * bonus_rate






class Manager(Employee):
    def long_term_bonus(self):
        return self.pay * 0.40





manager_1 = Manager('Vin', 'Diesel', 100000)




bonus_rate = 0.10
manager_bonus = manager_1.compute_bonus(bonus_rate)
long_term_bonus = manager_1.long_term_bonus()

print(f"{manager_1.fullname()}'s short-term bonus at {bonus_rate*100}% rate: ${manager_bonus}")
print(f"{manager_1.fullname()}'s long-term bonus at 40% rate: ${long_term_bonus}")
