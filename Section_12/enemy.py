class Enemy:
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        reamining_points = self.hit_points - damage
        if reamining_points >= 0:
            self.hit_points = reamining_points
            print("I took {} points of damage and have {} left.".format(damage, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}".format(self)