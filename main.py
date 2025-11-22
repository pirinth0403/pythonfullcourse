

#OOP CONCEPT
"""class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):#
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, score):
        super().__init__(fname, lname,)
        self.score = score
    def printscore(self):
        print(self.score)
x=Student("Michael","Smith","34")
x.printname()
x.printscore()"""
class Person:
    def __init__(self, fname, lname,age):
        self.firstname = fname
        self.lastname = lname
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 18:
            self.__age = age
        else:
           print("age should be 18")

p1=Person("Michael","Smith","2")
print(p1.firstname)
print(p1.lastname)
print(p1.get_age())

p1.set_age(13)
print(p1.get_age())





















