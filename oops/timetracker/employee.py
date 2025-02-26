from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Abstract Base Class (ABC) for all employee types.
    Forces subclasses to implement calculate_pay method.
    """
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    @abstractmethod
    def calculate_pay(self, hours_worked):
        """
        Must be overridden by subclasses.
        """
        pass

    def __str__(self):
        return f"Employee(ID={self.employee_id}, Name={self.name})"