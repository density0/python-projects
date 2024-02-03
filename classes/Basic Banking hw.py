class Account:
    def __init__(self, name, balance):
        self.account_name = name
        self.account_balance = balance

    def owner(self):
        print(self.account_name)

    def balance(self):
        print(self.account_balance)

    def deposit(self, adding):
        self.account_balance += adding

    def withdrawls(self, subtract):

        if subtract > self.account_balance:
            print("Funds Unavailable!")
        else:
            print("Withdrawal Accepted")
            self.account_balance -= subtract


al = Account('al', 200)
al.owner()
al.balance()
al.deposit(700)
al.balance()
al.withdrawls(300)
al.balance()
al.withdrawls(5000)
al.balance()
