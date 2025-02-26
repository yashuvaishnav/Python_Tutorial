from datetime import datetime

class TimeRecord:
    def __init__(self, employee):
        self.employee = employee
        self.clock_in_time = None
        self.clock_out_time = None
    
    def clock_in(self):
        self.clock_in_time = datetime.now()
    
    def clock_out(self):
        self.clock_out_time = datetime.now()
    
    def hours_worked(self):
        if self.clock_in_time and self.clock_out_time:
            delta = self.clock_out_time - self.clock_in_time
            return round(delta.total_seconds() / 3600, 2)
        return 0.0

    def __str__(self):
        return (f"TimeRecord for {self.employee.name} | "
                f"In: {self.clock_in_time}, Out: {self.clock_out_time}, "
                f"Hours: {self.hours_worked()}")


class TimeTracker:
    def __init__(self):
        self.records = []

    def clock_in(self, employee):
        record = TimeRecord(employee)
        record.clock_in()
        self.records.append(record)
        print(f"{employee.name} clocked in at {record.clock_in_time}")

    def clock_out(self, employee):
        open_records = [r for r in self.records 
                        if r.employee == employee and r.clock_out_time is None]
        if open_records:
            latest_record = open_records[-1]
            latest_record.clock_out()
            hrs = latest_record.hours_worked()
            print(f"{employee.name} clocked out at {latest_record.clock_out_time}. "
                  f"Hours worked: {hrs}")
        else:
            print(f"No open record for {employee.name}!")

    def get_employee_hours(self, employee):
        total_hours = 0.0
        for record in self.records:
            if record.employee == employee and record.clock_out_time:
                total_hours += record.hours_worked()
        return total_hours


class PayrollService:
    def __init__(self, time_tracker):
        self.time_tracker = time_tracker

    def process_pay(self, employee):
        total_hours = self.time_tracker.get_employee_hours(employee)
        pay = employee.calculate_pay(total_hours)  # Polymorphic call
        return pay

    def print_payslip(self, employee):
        pay_amount = self.process_pay(employee)
        total_hours = round(self.time_tracker.get_employee_hours(employee), 2)
        print(f"\n=== Payslip for {employee.name} ===")
        print(f"Employee Type: {employee.__class__.__name__}")
        print(f"Hours Worked: {total_hours}")
        print(f"Pay: ${pay_amount}") 
