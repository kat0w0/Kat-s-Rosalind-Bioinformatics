class Employee:
    num = 0
    state = "L"
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@gmail.com'
        Employee.num += 1

    def fillname(self):
        return '{} {}'.format(self.first, self.last)

    def applyL(self):
        self.last += self.state

print(Employee.num)
emp1 = Employee('Test', 'User')
emp2 = Employee('Tet', 'Usr')


print(emp1.email)
print('{} {}'.format(emp2.first, emp2.last))
print(emp1.fillname())
Employee.applyL(emp1)
print(Employee.fillname(emp1))
print(emp1.__dict__)
Employee.state = "W"
Employee.applyL(emp1)
emp1.state = "P"
Employee.applyL(emp1)
print(Employee.fillname(emp1))
print(emp2.email)
print(Employee.num)
