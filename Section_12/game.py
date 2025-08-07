from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

darby = Player("Darby")

basicEnemy = Enemy("Bat", 12, 1)
print(basicEnemy)

basicEnemy.take_damage(4)
print(basicEnemy)

uglyTroll = Troll("Pug")
print("Ugly Troll - {}".format(uglyTroll))

anoutherTroll = Troll("Ug")
print("Anouther troll - {}".format(anoutherTroll))
anoutherTroll.take_damage(12)
print(anoutherTroll)

brotherTroll = Troll("Urg")
print(brotherTroll)

uglyTroll.grunt()
anoutherTroll.grunt()
brotherTroll.grunt()

vamp = Vampyre("Vamp")
print(vamp)
vamp.take_damage(3)
print(vamp)

while vamp.alive:
    vamp.take_damage(1)
    print(vamp)

vampKing = VampyreKing("Dracula")
print(vampKing)
vampKing.take_damage(20)
print(vampKing)


