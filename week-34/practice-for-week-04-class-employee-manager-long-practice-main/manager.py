# - Import the Employee module you created in Phase 1.
# - Define a Manager class that inherits from the Employee class by passing
#  Employee as an argument to the Manager class definition.
# - Define a new employees property that is an empty list.
# - Add a constructor method to the Manager class that accepts the same arguments as
#  the Employee constructor method plus the new employees property. In the constructor, set the value of employees to the empty list if no employees argument is passed in .
# - Define an instance method named addEmployee that accepts an Employee instance as an
#  argument and appends it to the employees list.
# - Export your Manager class.

from employee import Employee


class Manager(Employee):
    def __init__(self, name, salary, title, employees=None):
        super().__init__(name, salary, title)
        self.employees = employees or []
        for emp in self.employees:
            emp.manager = self  # set the manager for each employee in the manager's list

    def addEmployee(self, employee):
        self.employees.append(employee)
        employee.manager = self  # set the manager for the new employee added to the list

    # bonus = (manager's salary + total salary of all employees under them) * multiplier

    def _total_sub_salary(self):
        total_salary = 0
        for employee in self.employees:
            if isinstance(employee, Manager):
                total_salary += employee._total_sub_salary()
            else:
                total_salary += employee.salary
        return total_salary


    def calculate_bonus(self, multiplier):
        bonus = (self.salary + self._total_sub_salary()) * multiplier
        return bonus

    def __repr__(self):
        return f"Manager(name='{self.name}', salary={self.salary}, title='{self.title}', employees={self.employees})"


splinter = Manager('Splinter', 100000, 'Sensei')
# print('Before: ', splinter.employees)

leo = Employee('Leonardo', 90000, 'Ninja', splinter)
mikey = Employee('Michelangelo', 90000, 'Ninja', splinter)
donnie = Employee('Donatello', 85000, 'Ninja', splinter)
raph = Employee('Raphael', 85000, 'Ninja', splinter)

# print('After: ', splinter.employees)

# print(raph.calculate_bonus(.25))  # --> 22500.0
# print(leo.calculate_bonus(.05))  # --> 4500.0
# print(splinter.calculate_bonus(.05))  # --> 22500.0
# Automatically adds the employee to the manager's employee array:
# Before:  []
# After:  [Employee(name='Leonardo', salary=90000, title='Ninja'), Employee(name='Michelangelo', salary=90000, title='Ninja'), Employee(
# name='Donatello', salary=90000, title='Ninja'), Employee(name='Raphael', salary=90000, title='Ninja')]
