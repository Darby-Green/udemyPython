from player import Player

darby = Player("Darby")

from enemy import Enemy

basicEnemy = Enemy("Bat", 12, 1)
print(basicEnemy)

basicEnemy.take_damage(4)
print(basicEnemy)