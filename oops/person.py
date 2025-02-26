class Person:  # Custom Data type
  # constructor
  def __init__(self, name = "unknown", skills="not skilled"):
    self.name = name 
    self.skills =skills

    print(self.name,self.skills)
  # def __str__(self):
  #   return f"Name: {self.name} and skills are {self.skills}"


  def get_profile(self):
    return (f"Name: = {self.name} and Skills= {self.skills}")

rajesh = Person("rajesh", "unskilled") 
print(rajesh)
# class Car:
#   con](this,name,skill)
#   this.n



# jai = Person("jai", "expert") 
# print(jai)

# urvashi = Person("urvashi", "expert")
# print(urvashi) 

# deepali = Person("deepali","intermediate")
# print(deepali)

# prasanna = Person("prasanna", "expert")
# print(prasanna)


# print(deepali.name) # whats your name?
# print(jai.name)

# print(rajesh.get_profile())

# print(jai.get_profile())


