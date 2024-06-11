 #parent1
 class Animal():
    def speak(self):
        return "animals make sound"
#child1 /parent2
class Mammal(Animal):
    def dog(self,name):
        self.name=name
        return f"dog : {self.name}  barks woof woof!!!"
    def cat(self,name):
        self.name = name
        return f"cat : {self.name}  says meeow meeow!!!"
# child2 =parent1+child1 u can use functions of parent class by this method(NO NEED TO SPECIFY SPEAK() bcos it is indirectly used by parent of display
class Display(Mammal):
    def display_action(self,dog, cat):
        self.speak()
        self.cat=cat()
        self.dog=dog()

t1=Display()
#accesing method from grandparent class animal by grandchildren class instance
print(t1.speak())
print(t1.dog("Browny"))




