"""
Owner: Algebra University, Zagreb
Address: Gradišćanska 24, 10000 Zagreb, Croatia
Web: www.algebra.hr
VAT-ID: 10750578045

Last modified: 09.06.2025.

NOTE: This script is the property of Algebra University, Zagreb. Unauthorized use is strictly prohibited.

VAŽNA NAPOMENA:
Kod izvan oznaka "# START SOLUTION" i "# END SOLUTION" ne smije se mijenjati (brisati, dodavati, mijenjati),
jer će to automatski označiti rješenje kao netočno.
"""


def write_books_to_csv(filename, books):
    """Writes a list of book dictionaries to a CSV file.

    CSV columns: title,author,pages
    """

    # START SOLUTION
    # import csv

    # with open(filename, "w", newline="") as csvfile:
    #     fieldnames = ["title", "author", "pages"]
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #     writer.writeheader()
    #     for book in books:
    #         writer.writerow(book)

    # pokušaj rješavanja samostalno


    for book in books:
        # book => {"title": "Dune", "author": "Frank Herbert", "pages": 604}
        # with open(filename, "w") as file_writer:
        #     file_writer.write(f"{book['title']},{book['author']},{book['pages']}")
        #     #pregazi postojeći sadržaj datoteke, a zatim upiše novi redak s podacima o knjizi, nije dobro
        #     # svaki put kada se otvori datoteka u načinu "w", prethodni sadržaj se briše, pa će na kraju u datoteci ostati samo zadnja knjiga iz liste.
        #apendanje
        with open(filename, "w") as file_writer:
            file_writer.write("title,author,pages\n")
        # sada kada imamo zaglavlje, možemo dodavati knjige bez brisanja prethodnog sadržaja
        
        for book in books:
            with open(filename, "a") as file_writer:
                file_writer.write(f"{book['title']},{book['author']},{book['pages']}\n")
        
        # ovo je kreiralo fail , ali nije dodalo zaglavlje. na nacin da cu prije petlje upisati zaglavlje, a zatim unutar petlje dodavati knjige, riješio sam problem.
        # idem na red 44


    # END SOLUTION


def average_pages_from_csv(filename):
    """Čita CSV datoteku i vraća aritmetičku sredinu broja stranica."""

    """Funkcija average_pages_from_csv(filename) prima naziv CSV datoteke sa stupcem 'pages'
    i računa aritmetičku sredinu broja stranica svih knjiga. 
    Prvu liniju (zaglavlje) treba preskočiti, a prazne ili neispravne retke ignorirati.
    Ako nema valjanih podataka, funkcija treba vratiti 0."""
    # START SOLUTION
    # import csv

    # total_pages = 0
    # num_books = 0

    # with open(filename, "r") as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         try:
    #             pages = int(row["pages"])
    #             total_pages += pages
    #             num_books += 1
    #         except (ValueError, KeyError):
    #             pass

    # if num_books > 0:
    #     return total_pages / num_books
    # else:
    #     return 0

    # pokušaj rješavanja samostalno
    aritm_sredina = 0
    broj_knjiga = 0
    sum_pages = 0
    
    
    with open(filename, "r") as file_reader:
        file_data = file_reader.readlines()
        #trebam preskočiti prvi redak (zaglavlje), pa ću početi od drugog retka
        for index, line in enumerate(file_data):
            if index == 0:
                continue
            # sada sam na redu koji sadrži podatke o knjizi, trebam ih razdvojiti i dohvatiti broj stranica
            book_data = line.strip().split(",") [-1] # ovo mi daje zadnji element liste, a to je broj stranica
            sum_pages += int(book_data.strip()) # pretvaram string u integer kako bih mogao zbrajati stranice i uklanja zadnj enter i space ako ih ima
            broj_knjiga += 1 # povećavam broj knjiga za 1 svaki put kada uspješno pročitam broj stranica, kako bih mogao izračunati aritmetičku sredinu na kraju
            
            # 
            
        #aritm_sredina = sum_pages / (broj_knjiga-1) # oduzimam 1 jer sam počeo brojati knjige od drugog retka, a prvi redak je zaglavlje koje ne sadrži podatke o knjizi, pa sam ga preskočio, ali sam ga ipak brojao u varijabli broj_knjiga, pa sada trebam oduzeti 1 da bih dobio točan broj knjiga
        aritm_sredina = sum_pages / broj_knjiga if broj_knjiga > 0 else 0
    print(aritm_sredina)
    return round(aritm_sredina, 2)
    
    
    # END SOLUTION

def main():
    books = [
        {"title": "Dune", "author": "Frank Herbert", "pages": 604},
        {"title": "1984", "author": "George Orwell", "pages": 328},
        {"title": "The Hobbit", "author": "J. R. R. Tolkien", "pages": 310},
    ]
    fname = "books.csv"
    write_books_to_csv(fname, books)
    assert round(average_pages_from_csv(fname), 2) == round((604 + 328 + 310) / 3, 2)
    print("All tests passed.")


if __name__ == "__main__":
    main()
