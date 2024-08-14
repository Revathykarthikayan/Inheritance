class Company():
    def __init__(self):
        self.companyname="Amazon"

c1=Company()
# without encaptulation: it is possible to modify and use data
print("Modified  data is printed")
c1.companyname="Amazzzoon"
print(c1.companyname)
print()

class Company():
    def __init__(self):
        self._officename = "zoho"#  protected variable can be accessed own and  child class
        self.__companyname ="Google"

#private variable declaration ,can be accesed only by method that belongs to same calass

    def print_companyname(self):
        print( "Printing private varaible using method of same class" )
        return self.__companyname
#child class
class Beta(Company):
    pass


c2=Company()
# print(c2.__companyname) is not possible to call without a method of same class
print(c2.print_companyname())
print()
print("Printing protected variable by child class object")

#callinf protected variable by child class object
b1=Beta()
print(b1._officename)