# - Import the Employee module you created in Phase 1.
# - Define a Manager class that inherits from the Employee class by passing
#  Employee as an argument to the Manager class definition.
# - Define a new employees property that is an empty list.
# - Add a constructor method to the Manager class that accepts the same arguments as
#  the Employee constructor method plus the new employees property. In the constructor, set the value of employees to the empty list if no employees argument is passed in .
# - Define an instance method named addEmployee that accepts an Employee instance as an
#  argument and appends it to the employees list.
# - Export your Manager class .
from employee import Employee


class Manager(Employee):
    def __init__(self, name, salary, title, employees=None):
        super().__init__(name, salary, title)
        self.employees = employees or []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def __repr__(self):
        return f"Manager(name='{self.name}', salary={self.salary}, title='{self.title}', employees={self.employees})"


splinter = Manager('Splinter', 100000, 'Sensei')
print(splinter)

leo = Employee('Leonardo', 90000, 'Ninja', splinter)
mikey = Employee('Michelangelo', 90000, 'Ninja', splinter)
donnie = Employee('Donatello', 90000, 'Ninja', splinter)
raph = Employee('Raphael', 90000, 'Ninja', splinter)

splinter.addEmployee(leo)
splinter.addEmployee(mikey)
splinter.addEmployee(donnie)
splinter.addEmployee(raph)

print(splinter.employees)
# [Employee(name='Leonardo', salary=90000, title='Ninja'),
# Employee(name='Michelangelo', salary=90000, title='Ninja'),
# Employee(name='Donatello', salary=90000, title='Ninja'),
# Employee(name='Raphael', salary=90000, title='Ninja')]
