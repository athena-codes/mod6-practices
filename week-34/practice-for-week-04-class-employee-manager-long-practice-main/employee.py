class Employee:
    def __init__(self, name, salary, title, manager=None):
        self.name = name
        self.salary = salary
        self.title = title
        self.manager = manager

    def __str__(self):
        return f"Employee(name={self.name}, salary={self.salary}, title={self.title}, manager={self.manager})"

    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self.salary}, title='{self.title}')"

leo = Employee('Leonardo', 90000, 'Ninja')

print(leo)
# Employee(name=Leonardo, salary=90000, title=Ninja, manager=None)
