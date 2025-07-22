import datetime
import time, pytz

class Account:
    """ Simple (bank) account balance w/ deposit, withdraw, and account checking functions"""

    @staticmethod
    def _currentTime():
        utcTime = datetime.datetime.utcnow()
        return pytz.utc.localize(utcTime)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactionList = [(Account._currentTime(), balance, self.name)]
        print("Account created for " + self.name)
        self.showBalance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.showBalance()
            self.transactionList.append((Account._currentTime(), amount, self.name))

    def withdraw(self, amount):
        if self.balance > amount and amount > 0:
            self.balance -= amount
            self.showBalance()
            self.transactionList.append((Account._currentTime(), -amount, self.name))
        else:
            print("You don't have enough money for a withdraw of {}".format(amount))

    def showBalance(self):
        print("{}'s balance is {}".format(self.name, self.balance))

    def printTransactionList(self):
        for date , amount, name in self.transactionList:
            if amount > 0:
                transactionType = "deposited"
            else:
                transactionType = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (Local time {}), by {}"
                  .format(amount, transactionType, date, date.astimezone(), name))


if __name__ == "__main__":
    Darby = Account("Darby", 0)
    Darby.showBalance()
    Darby.deposit(50)
    Darby.withdraw(30)
    Darby.printTransactionList()

    Dank = Account("Dank", 200)
    Dank.showBalance()
    Dank.deposit(40)
    Dank.withdraw(20)
    Dank.printTransactionList()
