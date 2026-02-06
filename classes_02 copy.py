

class Product:
    """
    Proizvod s cijenom.

    Polja:
    - name: string
    - price: int (>=0)
    """

    def __init__(self, name: str, price: int):
        # STUDENT CODE START
        # popunjavam konstruktor koji prima ime i cijenu proizvoda, te postavlja ta polja na odgovarajuće vrijednosti
        self.name = name   
        self.price = price
        # STUDENT CODE END

    def apply_discount(self, percent: int) -> None:
        """
        Smanji cijenu za percent (%).
        Cijena ostaje int;
        Ako je percent <= 0, ne mijenjaj cijenu.
        """
        # STUDENT CODE START
        # stvaram mmetodu.
        self.percent = percent      # stvaram self.percent da bih mogao koristiti vrijednost percent unutar metode, 
                                    # jer percent je lokalna varijabla koja postoji samo unutar metode, 
                                    # pa ako želim koristiti tu vrijednost unutar metode, moram je pohraniti u atribut objekta, 
                                    # koji je dostupan unutar metode putem self-a
        
        if self.percent > 0:
            discount_amount = self.price * self.percent / 100   # izračunavam iznos popusta koji treba 
                                                                # oduzeti od cijene, tako da pomnožim cijenu s postotkom popusta i 
                                                                # podijelim s 100 da dobijem iznos popusta u istim jedinicama kao i cijena
                                                                
            self.price = int(self.price - discount_amount)      # pretvaram u int jer cijena ostaje int
            
        else:
            self.price = self.price         # ako je percent <= 0, ne mijenjaj cijenu, pa je postavljam na istu vrijednost
        
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