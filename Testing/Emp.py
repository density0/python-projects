class Employee:
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def emp_info(self):
        info = f"name: {self.first_name} {self.last_name} \nSalary: {self.salary}"
        return info

    def give_raise(self, amount=5000):
        self.salary += amount
        return self.salary

    def get_salary(self):
        money = f"{int(self.salary)}"
        return money
