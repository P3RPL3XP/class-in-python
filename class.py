class Student:
       #class variable
       name="iiit"
       def init(self,name,age,gender):
              self.name=name
              self.age=age
              self.gender=gender
              print("constructor created")
       def get_data(self):
              self.name=input("enter name")
              self.age=int(input("enter age"))
              self.gender=input("enter gender")
       def display(self):
              print("hi{} your age is{} and your gender is{}".format(self.name,self.age,self.gender))
obj=Student()
obj.get_data()
obj.display()

#chld clASS

class Nuz_Student(Student):
       def __init__(self):
              print("Nuzvid Student")
       def whereis(self):
              print("i am from Nuzvid")
obj_nuz=Nuz_Student()
obj_nuz.whereis()
obj_nuz.get_data()
obj_nuz.display()
print("Handsome sai durga")
