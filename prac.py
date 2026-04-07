# Define a class Student with attributes name and marks. 
# The marks attribute is a list of integers representing the marks obtained by the student 
# in different subjects. Implement a method average() that calculates and 
# returns the average marks of the student.

class Student:

    @staticmethod # Static method does not require an instance to be called
    def hello():
        print("Hello")
        
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks)/len(self.marks)
    

s1 = Student("Smit", [80, 90, 85])
print(s1.hello(), "Name:", s1.name, "has got average marks:", s1.average())