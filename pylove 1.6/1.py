class Czas:
    def __init__(self, godzina = 0 , minuta = 0, sekunda = 0):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda
        self.ms = 0


    def __str__(self):
        return "h{},m{},s{}".format(self.godzina, self.minuta, self.sekunda)

    def set_time(self,g = None ,m=None,s=None):
        if g or g == 0:
            self.godzina = g
        if m or m ==0:
            self.minuta = m
        if s or s ==0:
            self.sekunda = s

    def add_time(self,extra_h=0,extra_m=0,extra_s=0):
        self.godzina += extra_h
        self.minuta += extra_m
        self.sekunda += extra_s
        if self.sekunda>59:
            self.minuta += int(self.sekunda/60)
            self.sekunda %= 24
        if self.minuta>59:
            self.godzina += int(self.minuta/60)
            self.minuta %= 24

    def get_seconds(self):
        return self.sekunda + self.minuta*60 + self.godzina*3600

    def get_minutes(self):
         return self.sekunda/60 + self.minuta + self.godzina*60

    def get_hours(self):
        return self.sekunda / 3600 + self.minuta/60 + self.godzina


class Zegar(Czas):
    def __init__(self,*args,format_czasu,**kwargs):
        super().__init__(*args,**kwargs)
        self.format=format_czasu

    def __str__(self):
        temp = super().__str__()
        temp += "format={}".format(self.format)
        return temp

class DokladnyZegar(Zegar):
    def __init__(self,*args,ms=0,**kwargs):
        super().__init__(*args,**kwargs)
        self.ms = ms

    def __str__(self):
        return super().__str__()

def mojprint(count):
    zegarek_dokladny = DokladnyZegar(1, format_czasu="12H", ms=4, minuta=2, sekunda=3)
    zegarek_dokladny.set_time(s=0, m=0, g=0)
    zegarek_dokladny.add_time(extra_h=0, extra_m=0, extra_s=3600000)
    while count>0:
        print(zegarek_dokladny.__str__(),".suffix")
        count-=1

mojprint(666)