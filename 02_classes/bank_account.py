from random import randint

class BankAccount:
    def __init__(self, owner: str, balance:int = 0) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"{self.owner} has {self.balance} sek"

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if amount > self.balance:
            # print("Balance is not enough!")
            return False
        else:
            self.balance -= amount
            return True
    
    def get_balance(self):
        return self.balance

    def transfer_to(self, other_account: 'BankAccount', amount: int):
        if amount > self.balance:
            return False
        
        self.balance -= amount
        other_account.balance += amount

        return True

if __name__ == "__main__":
    accounts = []
    account_qty = 10

    asdf = BankAccount("test", 1)

    for i in range(account_qty):
        accounts.append(
            BankAccount(
                f"a{i+1}",
                randint(100, 500)
            ))
    
    for account in accounts:
        print(account)
        account.deposit(randint(0,1000))
        print(account)
        account.withdraw(randint(0,1000))
        print(account)
        print()
        

    print("Testing transfering...")
    for account in accounts:
        other_account = accounts[randint(0,account_qty-1)]

        print(f"{account}, {other_account}")

        transfer_amount = randint(1, 100)
        result = account.transfer_to(other_account, transfer_amount)

        if result:
            print(f"transfered {transfer_amount} sek from {account.owner} to {other_account.owner}")
            print(f"{account}, {other_account}")
        else:
            print(f"{account.owner} does not have enough balance to transfer {transfer_amount} sek to {other_account.owner}")
        print()





