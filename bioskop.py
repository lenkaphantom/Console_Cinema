from globalne_promenljive import *
from funkcije_provere import *
from login_logout import *
import korisnik
import menadzer
import filmovi
import projekcija
import sala
import termin_projekcije
import karte
import izvestaji


def load_from_file():
    korisnik.load_from_file()
    filmovi.load_from_file()
    sala.load_from_file()
    projekcija.load_from_file()
    termin_projekcije.load_from_file()
    karte.load_from_file()


def write_to_file():
    korisnik.write_to_file()
    filmovi.write_to_file()
    sala.write_to_file()
    projekcija.write_to_file()
    termin_projekcije.write_to_file()
    karte.write_to_file()

def meni():
    while True:
        print("Dobro došli u aplikaciju. Ovo su Vaše opcije.")
        print("1: Prijava na sistem.")
        print("2: Registracija novog korisnika.")
        print("3: Pregled dostupnih filmova.")
        print("4: Pretraga filmova.")
        print("5: Višekriterijumska pretraga filmova.")
        print("6: Pretraga termina bioskopske projekcije.")
        print("-1: Izlaz iz aplikacije.")
        print()

        opcija = input("Unesite opciju koju želite: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            return
        if opcija == '1':
            username = login()
            if username == '-1':
                print()
                continue
            call_meni(username)
            print()
            continue
        elif opcija == '2':
            reg = korisnik.registration()
            if reg == '1':
                username = login()
                call_meni(username)
            print()
            continue
        elif opcija == '3':
            print("Dostupni filmovi: ")
            filmovi.print_movies()
            filmovi.print_movies_more()
            continue
        elif opcija == '4':
            filmovi.search_movies()
            print()
            continue
        elif opcija == '5':
            filmovi.multicriteria_search_movies()
            print()
            continue
        elif opcija == '6':
            termin_projekcije.search_date_of_screening()
            print()
            continue
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            print()
            continue


def meni_registeredUser(username):
    while True:
        print("Dobrodošli u meni. Ovo su Vaše opcije.")
        print("1: Izmena podataka.")
        print("2: Pregled dostupnih filmova.")
        print("3: Pretraga filmova.")
        print("4: Višekriterijumska pretraga filmova.")
        print("5: Pretraga termina bioskopske projekcije.")
        print("6: Rezervacija karata.")
        print("7: Pregled rezervisanih karata.")
        print("8: Poništi rezervaciju.")
        print("-1: Odjava sa sistema.")
        print()

        opcija = input("Unesite opciju koju želite: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            logout()
            print()
            return
        elif opcija == '1':
            korisnik.change_user(username)
            print()
            continue
        elif opcija == '2':
            print("Dostupni filmovi: ")
            filmovi.print_movies()
            filmovi.print_movies_more()
            continue
        elif opcija == '3':
            filmovi.search_movies()
            print()
            continue
        elif opcija == '4':
            filmovi.multicriteria_search_movies()
            print()
            continue
        elif opcija == '5':
            termin_projekcije.search_date_of_screening()
            print()
            continue
        elif opcija == '6':
            karte.book_ticket(1, username)
            print()
            continue
        elif opcija == '7':
            karte.print_ticket(username)
            print()
            continue
        elif opcija == '8':
            karte.cancle_ticket(username)
            print()
            continue
        else:
            print("Niste uneli ispravnu opciju, unesite ponovo.")
            print()
            continue


def meni_manager(username):
    while True:
        print("Dobrodošli u meni. Ovo su Vaše opcije.")
        print("1: Izmena podataka.")
        print("2: Registracija novih menadžera i prodavaca.")
        print("3: Pregled dostupnih filmova.")
        print("4: Pretraga filmova.")
        print("5: Višekriterijumska pretraga filmova.")
        print("6: Dodaj film.")
        print("7: Dodaj bioskopsku projekciju.")
        print("8: Ukloni film.")
        print("9: Ukloni bioskopsku projekciju.")
        print("10: Izmeni film.")
        print("11: Izmeni bioskopsku projekciju.")
        print("12: Pretraga termina bioskopske projekcije.")
        print("13: Generisanje termina bioskopske projekcije.")
        print("14: Izveštaji.")
        print("-1: Odjava sa sistema.")
        print()

        opcija = input("Unesite opciju koju želite: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            logout()
            print()
            return
        elif opcija == '1':
            korisnik.change_user(username)
            print()
            continue
        elif opcija == '2':
            menadzer.registration_manager()
            print()
            continue
        elif opcija == '3':
            print("Dostupni filmovi: ")
            filmovi.print_movies()
            filmovi.print_movies_more()
            continue
        elif opcija == '4':
            filmovi.search_movies()
            print()
            continue
        elif opcija == '5':
            filmovi.multicriteria_search_movies()
            print()
            continue
        elif opcija == '6':
            filmovi.add_movie()
            print()
            continue
        elif opcija == '7':
            projekcija.add_screening()
            print()
            continue
        elif opcija == '8':
            index = filmovi.print_index(opcija)
            if index == None:
                print()
                return
            filmovi.delete_movie(dict_of_movies[index])
            print()
            continue
        elif opcija == '9':
            passcode = projekcija.print_screening(opcija)
            if passcode == None:
                print()
                continue
            if passcode == '-1':
                print()
                return
            projekcija.delete_screening(dict_of_cinema_screenings[passcode])
            print()
            continue
        elif opcija == '10':
            index = filmovi.print_index(opcija)
            if index == '-1':
                print()
                return
            if index == None:
                print()
                continue
            filmovi.change_movie(index)
            print()
            continue
        elif opcija == '11':
            passcode = projekcija.print_screening(opcija)
            if passcode == '-1':
                print()
                return
            if passcode == None:
                print()
                continue
            projekcija.change_screening(passcode)
            print()
            continue
        elif opcija == '12':
            termin_projekcije.search_date_of_screening()
            print()
            continue
        elif opcija == '13':
            termin_projekcije.generate_date_of_screening()
            print()
            continue
        elif opcija == '14':
            izvestaji.report_menu()
            print()
            continue
        else:
            print("Niste uneli ispravnu opciju, unesite ponovo.")
            print()
            continue


def meni_salesman(username):
    while True:
        print("Dobrodošli u meni. Ovo su Vaše opcije.")
        print("1: Izmena podataka.")
        print("2: Pregled dostupnih filmova.")
        print("3: Pretraga filmova.")
        print("4: Višekriterijumska pretraga filmova.")
        print("5: Pretraga termina bioskopske projekcije.")
        print("6: Rezervacija karata.")
        print("7: Pregled rezervisanih karata.")
        print("8: Poništavanje karata.")
        print("9: Pretraga karata.")
        print("10: Direktna prodaja karata.")
        print("11: Prodaja rezervisanih karata.")
        print("12: Izmena karte.")
        print("13: Automatsko poništavanje rezervacija.")
        print("-1: Odjava sa sistema.")
        print()

        opcija = input("Unesite opciju koju želite: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            logout()
            print()
            return
        elif opcija == '1':
            korisnik.change_user(username)
            print()
            continue
        elif opcija == '2':
            print("Dostupni filmovi: ")
            filmovi.print_movies()
            filmovi.print_movies_more()
            continue
        elif opcija == '3':
            filmovi.search_movies()
            print()
            continue
        elif opcija == '4':
            filmovi.multicriteria_search_movies()
            print()
            continue
        elif opcija == '5':
            termin_projekcije.search_date_of_screening()
            print()
            continue
        elif opcija == '6':
            karte.book_menu(0)
            print()
            continue
        elif opcija == '7':
            karte.print_ticket_salesman(0)
            print()
            continue
        elif opcija == '8':
            karte.cancle_ticket()
            print()
            continue
        elif opcija == '9':
            karte.search_ticket()
            print()
            continue
        elif opcija == '10':
            karte.sell_ticket(username)
            print()
            continue
        elif opcija == '11':
            karte.sell_booked_ticket(username)
            print()
            continue
        elif opcija == '12':
            karte.change_ticket()
            print()
            continue
        elif opcija == '13':
            karte.automatically_cancle_ticket()
            print()
            continue
        else:
            print("Niste uneli ispravnu opciju, unesite ponovo.")
            print()
            continue


def call_meni(username):
    if korisnik.get_user_by_username(username)['role'] == roles[1]:
        meni_registeredUser(username)
    elif korisnik.get_user_by_username(username)['role'] == roles[2]:
        meni_salesman(username)
    else:   
        meni_manager(username)
    return

        
if __name__ == '__main__':
    load_from_file()
    karte.available_tickets()
    check_date_of_screening()
    karte.check_ticket_active()
    meni()
    write_to_file()