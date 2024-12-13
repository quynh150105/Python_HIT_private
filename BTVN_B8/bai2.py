class Person:
    #init
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
    
    #getter
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob
    
    #setter
    def set_name(self,name):
        self.name = name
    def set_dob(self,dob):
        self.dob = dob
    
    #describe
    def describe(self):
        print(f"name= {self.name}, dob= {self.dob}", end=", ")

class Student(Person):
    #init
    def __init__(self,name,dob,grade):
        super().__init__(name,dob)
        self.grade = grade

    #getter
    def get_grade(self):
        return self.grade

    #setter
    def set_grade(self,grade):
        self.grade = grade
 
    #describe
    def describe(self):
        super().describe()
        print(f"grade= {self.grade}")       

class Teacher(Person):
    #init
    def __init__(self,name,dob,subject):
        super().__init__(name,dob)
        self.subject = subject

    #getter
    def get_subject(self):
        return self.subject
    
    #setter
    def set_subject(self,subject):
        self.subject = subject

    #describe
    def describe(self):
        super().describe()
        print(f"subject= {self.subject}")

class Doctor(Person):
    #__init__
    def __init__(self,name,dob,specialist):
        super().__init__(name,dob)
        self.specialist = specialist

    #getter
    def get_specialist(self):
        return self.specialist
    
    #setter
    def set_specialist(self,specialist):
        self.specialist = specialist
    
    #describe
    def describe(self):
        super().describe()
        print(f"specialist= {self.specialist}")

from typing import List,  Optional
class Ward:
    #__init__
    def __init__(self, name: str, list_person: Optional[List[Person]] = None):
        
        self.name = name
        self.list_person = list_person if list_person else []

    #add Person
    def addPerson(self,people:Person):
        if isinstance(people,Person):
            self.list_person.append(people)

    #describe
    def describe(self):
        print(f"Ward name: {self.name}")
        for person in self.list_person:
            person.describe()

    #countDoctor
    def countDoctor(self):
        count = 0
        for person in self.list_person:
            if isinstance(person,Doctor):
                count += 1
        print(f"number_of_Doctor= {count}")

    #sortAge
    def sortAge(self):
        self.list_person.sort(key=lambda person: person.get_dob())


ward = Ward("Ward")
student1 = Student(name="studentA", dob=2010, grade="7")
teacher1 = Teacher(name="teacherA", dob=1969, subject="Math")
doctor1 = Doctor(name="doctorA", dob=1945, specialist="Endocrinologists")
teacher2 = Teacher(name="teacherB", dob=1995, subject="History")
doctor2 = Doctor(name="doctorB", dob=1975, specialist="Cardiologists")
ward.addPerson(student1)
ward.addPerson(teacher1)
ward.addPerson(teacher2)
ward.addPerson(doctor1)
ward.addPerson(doctor2)
ward.describe()
ward.countDoctor()
ward.sortAge()
ward.describe()








