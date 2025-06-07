# class Employee:
#     company = "Google"

# emp1 = Employee()
# emp1.name = "Viral"

# print(emp1.name)
# print(emp1.company)

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum =0 
        for mark in self.marks:
            sum+=mark
        print("Hello" , self.name, "Your avg score is:", sum/3)
        


s1 = Student("Karan",[78,90,56])
s1.get_avg()
        
