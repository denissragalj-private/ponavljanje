class User:
    """
    Predstavlja korisnika pretplate.

    Polja:
    - name: string
    - balance: int  (pozitivno znači dugovanje, 0 znači nema duga)

    - funkcionalnosti:
        Povećaj dugovanje (balance) za amount ako je amount > 0.
        Smanji dugovanje (balance) za amount ako je amount > 0. Balance ne smije pasti ispod 0.
    """
    # STUDENT CODE START
    def __init__(self, name: str, balance: int = 0):
        self.name = name
        self.balance = balance
    
    def pay(self, amount: int):
        if amount > 0:
            self.balance = max(0, self.balance - amount)

    def charge(self, amount: int):
        if amount > 0:
            self.balance += amount
    
    

    # STUDENT CODE END


# User
u = User("Ana", 0)
assert u.name == "Ana"
assert u.balance == 0
u.charge(20)
assert u.balance == 20
u.pay(5)
assert u.balance == 15
u.pay(100)
assert u.balance == 0
u.charge(-10)  # ignoriraj
assert u.balance == 0