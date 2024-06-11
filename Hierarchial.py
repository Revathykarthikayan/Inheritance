class Person():
          #class attributes parent class1
    name="Revathy"
    age=30
    def __init__(self,quali="B.Tech",stream="CSE"):
        self.quali=quali
        self.stream=stream

        #used class attributes inside methods of same class
    def info(self):
        return f"name: {self.name},  Age: {self.age},  Quali: {self.quali}"

        #child class1
class Daughter(Person):
    def __init__(self,quali,stream,father,mother):
        super().__init__(quali,stream)   # used super method to avoid self. in child too( here u r using parents method, atributes)
        self.father=father
        self.mother=mother
        self.info()

    def  info_daughter(self):
        return f"{self.info()}, Father: {self.father},  Mother: {self.mother}"


 # child class 2
class Mother(Person):
    def __init__(self,spouse,children,):
        #super method now aceessing every atribute of parent class and parent methods
        super().__init__()
        self.spouse = spouse
        self.children = children
        self.info()

    def info_mother(self):
        return f"{self.info()}, Spouse: {self.spouse}, Children: {self.children}"


#displaying child class1
d=Daughter("B.Tech","","Ravichandiran","Mahalakshmi")
print(d.info_daughter())
# diplaying child class 2
m=Mother("karthikayan",'shai,vivi')
print(m.info_mother())