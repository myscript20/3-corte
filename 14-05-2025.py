class Dog:
    def __init__(self, size, color, race, price):#cosntructor of the class
        self.size = size
        self.color = color
        self.race = race
        self.price = price

    def walking(self):
        print(f"{self.race} is the race")
Rufo = Dog("Small", "Brown","Pug","Free" )
print(f"Rufo: {Rufo.size}")

Chanda = Dog("Big", "Black","Husky", 5000 )
print(f"Chanda: {Chanda.size}")

Sol = Dog("Small", "White","Bulldog",1000 )
print(f"Sol: {Sol.size}, {Sol.color}, {Sol. race}, {Sol.price}.")

Uniqua = Dog("Big", "Brown","Golden Retriever","Free" )
print(f"Uniqua: {Uniqua.size}, {Uniqua.color}, {Uniqua. race}, {Uniqua.price}.")

Lola = Dog("Small", "Brown","Chihuahua","Free" )
print(f"Lola: {Lola.size}, {Lola.color}, {Lola. race}, {Lola.price}.")
Lola.walking()

print("-"*100)

class people:
    def __init__(me,size, haircolor,eyesize, mood):
        me.size = size
        me.haircolor = haircolor
        me.eyesize = eyesize
        me.mood = mood
    def fealing(me):
        print(f"{me.mood} is the mood")

Andrea = people(1.59, "Brown","Big","bored" )
print(f"{Andrea.size}, {Andrea.haircolor}, {Andrea.eyesize}")
Andrea.fealing()

Master = people(1.69, "Brown","small","joker" )
print(f"{Master.size}, {Master.haircolor}, {Master.eyesize}")
Master.fealing()

Alvaro = people(1.70, "Brown","Big","Mad")
print(f"{Alvaro.size}, {Alvaro.haircolor}, {Alvaro.eyesize}")

Camilo = people(1.83, "Brown","Small","Focus")
print(f"{Camilo.size}, {Camilo.haircolor}, {Camilo.eyesize}")

Sergio= people(1.78, "Black","Medium","Sad")
print(f"{Sergio.size}, {Sergio.haircolor}, {Sergio.eyesize}")

print("-"*100)

class Cat:
    def __init__(self, size, color, race, price, name):
        self.size = size
        self.color = color
        self.race = race
        self.price = price
        self.name = name

    def walking(self):
         print(f"{self.name} is walking")   
        
Misifu = Cat("Small","Orange", "Somali", "Adopt", "Misifu")
print(f"Misifu: {Misifu.size}, {Misifu.color}, {Misifu.race}, {Misifu.price}")
Misifu.walking()

Salchicha = Cat("Big","White","Maine coon",5000, "Salchicha")
print(f"Salchicha: {Salchicha.size}, {Salchicha.color}, {Salchicha.race}, {Salchicha.price}")

Gates = Cat("Medium","Pruple","Sphynx", "Free", "Gates")
print(f"Gates: {Gates.size}, {Gates.color}, {Gates.race}, {Gates.price}")

Fisioso = Cat("Medium","White","Somali", 3000, "Fisioso")
print(f"Fisioso: {Fisioso.size}, {Fisioso.color}, {Fisioso.race}, {Fisioso.price}")
Fisioso.walking()

Brayan = Cat("Medium","Black","Criole", "Free", "Brayan")
print(f"Brayan: {Brayan.size}, {Brayan.color}, {Brayan.race}, {Brayan.price}")
    