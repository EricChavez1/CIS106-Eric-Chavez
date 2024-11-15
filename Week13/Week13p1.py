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


emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('test', 'employee', 60000)


bonus_rate = 0.10  
emp_1_bonus = emp_1.compute_bonus(bonus_rate)
emp_2_bonus = emp_2.compute_bonus(bonus_rate)

print(f"{emp_1.fullname()}'s bonus at {bonus_rate*100}% rate: ${emp_1_bonus}")
print(f"{emp_2.fullname()}'s bonus at {bonus_rate*100}% rate: ${emp_2_bonus}")
