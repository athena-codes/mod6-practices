from employee import Employee
from manager import Manager

hobbes = Manager("Hobbes", 1000000, "Founder")
calvin = Manager("Calvin", 130000, "Director", [hobbes])
susie = Manager("Susie", 100000, "TA Manager", [calvin])
lily = Employee("Lily", 90000, "TA", susie)
clifford = Employee("Clifford", 90000, "TA", susie)

print('HOBBES', hobbes.calculate_bonus(.05))
print('CALVIN', calvin.calculate_bonus(.05))
print('SUSIE', susie.calculate_bonus(.05))
print('LILY', lily.calculate_bonus(.05))
print('CLIFFORD', clifford.calculate_bonus(.05))
