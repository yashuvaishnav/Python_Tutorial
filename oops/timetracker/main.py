from fulltime import FullTimeEmployee 
from parttime import PartTimeEmployee
from tracker import TimeTracker, PayrollService


def main():
    from abc import ABC, abstractmethod

    # We can now rely on the fact that Employee is an abstract class.
    ram = FullTimeEmployee(employee_id=1, name="Ram", monthly_salary=3500.0)
    gopal = PartTimeEmployee(employee_id=2, name="Gopal", hourly_rate=18.5)

    tracker = TimeTracker()
    tracker.clock_in(ram)
    tracker.clock_in(gopal)

    # (Simulate time passing...)
    tracker.clock_out(ram)
    tracker.clock_out(gopal)

    payroll = PayrollService(tracker)
    payroll.print_payslip(ram)
    payroll.print_payslip(gopal)

if __name__ == "__main__":
    main() 