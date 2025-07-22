class Kettle(object):

    powerSource = "electricity"
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switchOn(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

print(kenwood.on)
kenwood.switchOn()
print(kenwood.on)

kenwood.power = 1.5
print(kenwood.power)

print(Kettle.powerSource)
print(kenwood.powerSource)
