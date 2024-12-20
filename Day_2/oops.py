class Speaker:
     brand="boat"
     def __init__(self, color, model):
          self.color=color
          self.model=model
     def power_on(self):
          print(f"""powering on "{self.color} {self.model}" speaker""")
     def power_of(self):
          print(f"powering off {self.color} {self.model} speaker")
speaker1=Speaker('black','a823wfx')
speaker2=Speaker('white','2af42')
# print(
#      f"speaker one has {speaker1.color} and the brand of speake one is {speaker1.brand}"
# )
# speaker1.power_on()

# inheritance

class Person:
     def __init__(self, name, idnumber):
          self.name=name
          self.idnumber=idnumber

     def display(self):
          print(f"the names are: {self.name}\n and their id numbers: {self.idnumber}")
          
class Employee(Person):
     def __init__(self, name, idnumber, salary):
          super().__init__(name, idnumber)
          self.salary=salary

     def increment_hike(self, in_hike):
          self.n=in_hike
          salary_hike=self.salary*(self.n/100)
          self.salary=self.salary+salary_hike
          print(f"salary after hike: {self.salary}")

     def employe_display(self):
          print(f"the original salary is: {self.salary}")

E=Employee('suraj',23,25000)
# E.display()
# E.employe_display()
# E.increment_hike(10)

class Person:
     def __init__(self, *name, **idnumber):
          self.name = name
          self.idnumber = idnumber


     def display(self): 
          val = self.idnumber.values()
          v = 0
          for i in self.name:
               print(f"name is: {i} and their id: {list(val)[v]}")
               v+=1

p=Person('suraj','abhishek','nayan', a=10121,b=34132,c=312412)
# p.display()


# public members 
class Public_class:
     def __init__(self, name):
          self.name = name
          print(f"name is: {self.name}")

#pc=Public_class("ajay")

# private member
class Private_class:
     def __init__(self, age, year, dob):
          self.__age = age # private attribute
          self.__year = year # private attribute
          self.dob=dob

     def display_age(self):  # this method helps to get the private data
          print(f"age is: {self.__age}")

     def display_year(self):
          print(f"year is: {self.__year}")

     def __private_class(self, *games): # private class
          for i in games:
               if i == 'chess':
                    print("this game is great")

# pc_1=Private_class(23, 2001, "10-10-2001")
# pc_1.display_age()
# pc_1.display_year()
# print(pc_1.dob) # public method can accessible outside the class
# pc_1._Private_class__private_class('cricket','chess','hocky')

# protected member

class Protected_class:
     def __init__(self):
          self._age=30

class Subclass(Protected_class):
    def display_age(self):
        print(self._age)

# obj=Subclass();
# obj.display_age()
# obj._age
os=Protected_class()
print(os._age)