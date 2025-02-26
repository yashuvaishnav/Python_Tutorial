class Person:
  def __init__(self, first_name, last_name, address):
    self.first_name = first_name 
    self.last_name = last_name 
    self.address = address

  def __str__(self):
    return f"First Name = {self.first_name} and Last Name = {self.last_name}"
  
  def __repr__(self):
        """
        Called in contexts like the Python interpreter, or when doing repr(obj).
        Typically returns a developer-oriented representation 
        that can help recreate the object if possible.
        """
        return f"Employee({self.first_name!r}, {self.last_name!r})"

  def get_address(self):
    return self.address



class Employee(Person):
  def __init__(self, first_name, last_name, address, temp = False):
    # Call the parent class's _init_()
    super().__init__(first_name, last_name, address)

    self.temp = temp
    

  def time_in(self):
    print("Time-in") 

  def time_out(self):
    print("Time-out")

  def get_salary(self):
    pass

class ITConsultant(Employee):
  def __init__(self, first_name, last_name, address):
    super().__init__(first_name, last_name, address, True) 

  def raise_invoice(self, amount):
    print(f"{self.first_name} has raised the invoice for amount Rs. {amount}")

rajesh = Employee("Rajesh", "Pillai", "Mumbai", True)


print(rajesh)  # uses __str__()

print("\nUsing repr(emp):")
print(repr(rajesh))  # Invokes emp.__repr__()

print(rajesh.address)
print(rajesh.get_address())


rajesh.time_in()
rajesh.time_out()


bill = ITConsultant("bill", "gates", "us")
print(bill.temp)

bill.time_in()
bill.raise_invoice(1000)

# person = Person("abc","yz","unknown")

# print(person.get_address())
# print(person.temp)