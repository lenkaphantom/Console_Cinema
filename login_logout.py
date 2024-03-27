from globalne_promenljive import *
from funkcije_provere import *

def login():
    while True:
        username = input("Zdravo! Unesite Vaše korisničko ime: ")
        if len(username) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if username == '-1':
            print()
            return username
        if username in dict_of_registered_users.keys():
            password = input("Unesite vašu lozinku: ")
            if password == '-1':
                print()
                return password
            if not check_password(password):
                print()
                continue
            if password != dict_of_registered_users[username]['password']:
                print("Niste uneli ispravnu lozinku!")
                print()
                continue
            print()
            print(f"Zdravo, {username}! Uspešno ste se ulogovali na Vaš nalog!")
            return username
        else:
            print("Korisničko ime nije ispravno!")
            print()
            continue


def logout():
    print("Uspešno ste se odjavili sa aplikacije.")
    return