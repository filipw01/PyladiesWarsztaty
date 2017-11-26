import json
class Czlowiek:
    def __init__(self, name, height, weight):
        self.bribe = True
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = 0
        self.kcalToBurn = 0
        self.diffUp = 0
        self.diffDown = 0
        self.goodWeightDown = 0
        self.goodWeightUp = 0
        self.kcalToBurn = 0
        self.running = 0
        self.bicycling = 0
        self.hobby = 0
        self.chess = 0
        self.kcalToTake = 0
        self.chocolate = 0
        self.potato = 0

    def speak(self):
        return "Mowie prawde"

    def count_bmi(self):
        self.bmi = self.weight/(self.height/100)**2
        return self.bmi

    def diff_to_norm(self):
        self.count_bmi()
        if self.bmi<18.5 or self.bmi>25:
            self.goodWeightUp = (self.height/100)**2*25
            self.goodWeightDown = (self.height/100)**2*18.5
            self.diffUp = self.weight - self.goodWeightUp
            self.diffDown = self.weight - self.goodWeightDown
            if self.diffUp<0:
                return"Do dolnej granicy normy brakuje ci " +str(self.diffDown)+" ,a do gornej brakuje ci "+str(self.diffUp)
            else:
                return "Do dolnej granicy normy masz o tyle kg za duzo " + str(self.diffDown) + " ,a do gornej masz tyle kg za duzo " + str(
                    self.diffUp)
        else:
            return "Masz poprawne BMI"
    def save_data(self):
        with open(str(self.name)+".json",'w')as file:
            json.dump(
                {
                    'waga':self.weight,
                    'imie':self.name,
                    'wzrost':self.height
                },fp=file
            )

    def to_burn(self):
        self.diff_to_norm()
        if self.diffUp>0:
            self.kcalToBurn = self.diffUp*6000
            self.running = self.kcalToBurn/500
            self.bicycling = self.kcalToBurn/600
            self.hobby = self.kcalToBurn/250
            self.chess = self.kcalToBurn/150
        return 'Running [h]:'+str(self.running)+'Bicycling [h]:'+str(self.bicycling)+'Hobby [h]:'+str(self.hobby)+'Chess [h]:'+str(self.chess)

    def to_eat(self):
        self.diff_to_norm()
        if self.diffDown < 0:
            self.kcalToTake = self.diffDown*6000
            self.chocolate = self.kcalToTake/4500
            self.potato = self.kcalToTake/800
        return 'Chocolate [kg]:'+str(self.chocolate)+'Potato [kg]:'+str(self.potato)

    def what_to_do(self):
        self.diff_to_norm()
        if self.diffUp>0:
            return self.to_burn()
        if self.diffDown<0:
            return self.to_eat()

class Polityk(Czlowiek):
    def speak(self):
        if self.bribe:
            print("Klamie, bo moge")
        else:
            super().speak()

    def recive_bribe(self):
        self.bribe = False

poli = Polityk('Zenek', 170,84)
print(poli.what_to_do())