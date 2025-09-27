#amount_of_students = 0
class Student: 
    print('Hi')
    def __init__(self, height=170):
        #self.height = height
        #Student.amount_of_students += 1
        #print(self.height)
        self.height += 10
    height = 170
    def printer(self):
        print(self.height)



Ira = Student()
Olexandra = Student()
#Olexandra = Student(height=172)
#print(Ira.height)
#print(Olexandra.height)
#print(Ira.amount_of_students)
#print(Olexandra.amount_of_students)