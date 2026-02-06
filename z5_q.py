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


def split_books_by_length(pages, threshold=300):
    """Dijeli knjige na broj stranica 'iznad' i 'ispod' definirane granice."""

    """Funkcija split_books_by_length(pages, threshold=300) prima listu broja stranica pojedinih knjiga i pragu stranica.
    Vraća dvije liste: prva s knjigama ispod praga, druga s knjigama jednakim ili većim od praga,
    zadržavajući izvorni redoslijed. Prag je po zadanom 300, ali ga korisnik može promijeniti argumentom threshold."""
    # START SOLUTION
    iznad = []
    ispod = []

    for page in pages:
        if page < threshold:
            ispod.append(page)
        else:
            iznad.append(page)

    return ispod, iznad

    # END SOLUTION


def main():
    assert split_books_by_length([150, 400, 200, 500], 300) == ([150, 200], [400, 500])
    assert split_books_by_length([], 250) == ([], [])
    print("All tests passed.")


if __name__ == "__main__":
    main()
