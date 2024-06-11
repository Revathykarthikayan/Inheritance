class Grandpa():

    def __init__(self,property="80 crore"):
        self.property = property

    def land(self):
        return f" In grandpa class land method{self.property}"

class Dad():
    def __init__(self,goldq="10kg"):
        self.goldq=goldq

    def gold(self):
        return f" In dad class gold method{self.goldq}"

#child1 using parent1 and parent2
class Son(Grandpa,Dad):
    def __init__(self,property,goldq="5 kg",mutual_fundq="hike is 800 percentange"):

        Grandpa.__init__(self, property)
        Dad.__init__(self,goldq)
        self.mutual_fundq = mutual_fundq

    def mutual(self):
        grandpa_info= self.land()
        dad_info=self.gold()

        return f"Grandpa_aquires :{grandpa_info} , Dad_aquires :{dad_info}, Son_aquires mutual fund :{self.mutual_fundq}"
# grandpa takes his own constructor value
a1=Grandpa()
print(a1.land())

#dad takes his own constructor value
a2=Dad()
print(a2.gold())

#  son class has taken input 35 crore from user,but takes gold and mutual fund from child class constr not from parent clases
#  but prints the return value from parent clases like in grandpa class, in dad class but not values
a3=Son("35 crore")
print(a3.mutual())





