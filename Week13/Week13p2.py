class Student:

    def __init__(self, first, last, district_code, enrolled_credits):
        self.first = first
        self.last = last
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def compute_tuition(self):
        
        if self.district_code.upper() == 'I':
            rate_per_credit = 250.00  
        else:
            rate_per_credit = 500.00  
        
        
        tuition_owed = self.enrolled_credits * rate_per_credit
        return tuition_owed


student_1 = Student('Vin', 'Diesel', 'I', 15)     
student_2 = Student('Kobe', 'Bryant', 'O', 12)   


print(f"{student_1.fullname()}'s tuition: ${student_1.compute_tuition()}")
print(f"{student_2.fullname()}'s tuition: ${student_2.compute_tuition()}")
