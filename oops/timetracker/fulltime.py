from employee import Employee
class FullTimeEmployee(Employee):
    """
    A full-time employee with a monthly salary.
    """
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self, hours_worked):
        return self.monthly_salary