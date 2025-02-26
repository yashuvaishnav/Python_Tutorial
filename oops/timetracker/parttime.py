from employee import Employee
class PartTimeEmployee(Employee):
    """
    A part-time employee with an hourly wage.
    """
    def __init__(self, employee_id, name, hourly_rate):
        super().__init__(employee_id, name)
        self.hourly_rate = hourly_rate

    def calculate_pay(self, hours_worked):
        return round(self.hourly_rate * hours_worked, 2) 