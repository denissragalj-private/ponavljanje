

class Product:
    """
    Proizvod s cijenom.

    Polja:
    - name: string
    - price: int (>=0)
    """

    def __init__(self, name: str, price: int):
        # STUDENT CODE START
        self.name = name
        self.price = max(0, price)
        # self.price = price if price >= 0 else 0
        # if price >= 0:
        #     self.price = price
        # else:
        #     self.price = 0
        # STUDENT CODE END

    def apply_discount(self, percent: int) -> None:
        """
        Smanji cijenu za percent (%).
        Cijena ostaje int;
        Ako je percent <= 0, ne mijenjaj cijenu.
        """
        # STUDENT CODE START
        if percent > 0:
            # self.price -= int(self.price * (percent / 100))
            self.price = self.price - int(self.price * (percent / 100))
        # STUDENT CODE END



#region Product
p1 = Product("Kruh", 2)
p2 = Product("Sir", 10)
assert p1.name == "Kruh" and p1.price == 2
p2.apply_discount(10)
assert p2.price == 9
p2.apply_discount(0)
assert p2.price == 9
#endregion