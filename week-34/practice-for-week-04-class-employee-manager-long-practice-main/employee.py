class Employee:
    def __init__(self, name, salary, title, manager=None):
        self.name = name
        self.salary = salary
        self.title = title
        self.manager = manager
        if manager:
            manager.addEmployee(self)

    def calculate_bonus(self, multiplier):
        bonus = self.salary * multiplier
        return bonus

    def __str__(self):
        return f"Employee(name={self.name}, salary={self.salary}, title={self.title}, manager={self.manager})"

    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self.salary}, title='{self.title}')"


leo = Employee('Leonardo', 90000, 'Ninja')
raph = Employee('Raphael', 90000, 'Ninja')
donny = Employee('Donatello', 85000, 'Grasshopper')
# Employee(name=Leonardo, salary=90000, title=Ninja, manager=None)

# print(leo)
# print(raph.calculate_bonus(0.25))  # => 22500
# print(donny.calculate_bonus(0.15))  # => 12750
