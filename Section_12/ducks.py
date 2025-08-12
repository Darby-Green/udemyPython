class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("wee I can fly")
        else:
            print("Well at least i can swim")

class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)
    def walk(self):
        print("Waddle Waddle")

    def swim(self):
        print("Bwub bwub")

    def quack(self):
        print("Quack Quack")

    def fly(self):
        self._wing.fly()


# def testDuck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # testDuck(daffie)