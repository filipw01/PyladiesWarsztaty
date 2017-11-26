class Czlowiek:
    def __init__(self):
        self.bribe = True

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

poli = Polityk()
czlo = Czlowiek()
print(poli.speak())
print(czlo.speak())
poli.recive_bribe()
print(poli.speak())