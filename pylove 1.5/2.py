class Czlowiek:
    def __init__(self, name, height, weight):
        self.bribe = True
        self.name = name
        self.height = height
        self.weight = weight

    def speak(self):
        print("Mowie prawde")

    def count_bmi(self):
        pass

    def diff_to_norm(self):
        pass

    def save_data(self):
        pass

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    def speak(self):
        if self.bribe:
            print("Klamie, bo moge")
        else:
            super().speak()

    def recive_bribe(self):
        self.bribe = False

poli = Polityk('Zenek',120,150)
czlo = Czlowiek("Magda", 145, 132)
print(str(poli.speak()) + str(poli.name))
print(str(czlo.speak())+ str(czlo.name))
poli.recive_bribe()
print(poli.speak())