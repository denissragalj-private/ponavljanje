

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


class Cart:
    """
    Košarica proizvoda.

    Polje:
    - items: lista Product objekata
    """

    def __init__(self):
        # STUDENT CODE START
        self.items = [] # lista u koju ćemo dodavati proizvode , prazna lista na početku (košarica je prazna)

        # STUDENT CODE END

    def add(self, product: Product) -> None:
        """Dodaj product u items."""
        # STUDENT CODE START
        self.items.append(product)
        
    
    
    
        # STUDENT CODE END

    def total(self) -> int:
        """Vrati zbroj cijena svih proizvoda u items."""
        # STUDENT CODE START
        #Lujov način:
        # return sum(item.price for item in self.items) # sum() funkcija zbraja sve elemente u generatoru, 
        #                                               # a generator se stvara kroz izraz (item.price for item in self.items) 
        #                                               # koji prolazi kroz svaki proizvod u items i uzima njegovu cijenu (price)
 
        total_price = 0                     # varijabla u koju ćemo spremati zbroj cijena
        for item in self.items:             # prolazimo kroz sve proizvode u košarici
            total_price += item.price       # dodajemo cijenu trenutnog proizvoda na ukupnu cijenu
        return total_price                  # vraćamo ukupnu cijenu svih proizvoda u košarici  
    
    
    
    
    
        # STUDENT CODE END



# Product
p1 = Product("Kruh", 2)
p2 = Product("Sir", 10)
assert p1.name == "Kruh" and p1.price == 2
p2.apply_discount(10)
assert p2.price == 9
p2.apply_discount(0)
assert p2.price == 9


# Cart
c = Cart()
c.add(p1)
c.add(p2)
assert c.total() == 11