from globalne_promenljive import *
from funkcije_provere import *
from login_logout import *

def load_from_file(filename='registrovani_korisnici.txt'):
    with open(filename, 'r', encoding="utf-8") as registrovani_korisnici:
        for line in registrovani_korisnici:
            user = line.strip().split(" | ")
            if len(user) == 5:
                username, password, firstname, lastname, role = user
                user_dict = {
                    "username": username,
                    "password": password,
                    "firstname": firstname,
                    "lastname": lastname,
                    "role": role
                }
                dict_of_registered_users[username] = user_dict


def write_to_file(filename='registrovani_korisnici.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for user in dict_of_registered_users.values():
            file.write(f"{user['username']} | {user['password']} | {user['firstname']} | {user['lastname']} | {user['role']}\n")


def get_user_by_username(username):
    if username in dict_of_registered_users.keys():
        return dict_of_registered_users[username]
    return None


def registration():
    global dict_of_registered_users
    user_dict = {}
    while True:
        username = input("Zdravo! Unesite željeno korisničko ime: ")
        if username == '-1':
            print()
            return
        if not check_username(username):
            print()
            continue

        password = input("Unesite Željenu lozinku: ")
        if password == '-1':
            print()
            return
        if not check_password(password):
            print()
            continue

        password_p = input("Potvrdite Vašu lozinku: ")
        if len(password_p) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if password_p == '-1':
            print()
            return
        if password != password_p:
            print("Lozinke se ne podudaraju. Unesite ih ponovo.")
            print()
            continue

        firstname = input("Unesite Vaše ime: ")
        if firstname == '-1':
            print()
            return
        if not check_name(firstname):
            print()
            continue
        
        lastname = input("Unesite Vaše prezime: ")
        if lastname == '-1':
            print()
            return
        if not check_name(lastname):
            print()
            continue

        role = roles[1]

        user_dict = {
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "role": role
        }
        
        dict_of_registered_users[username] = user_dict

        print()
        print("Uspešno ste registrovali Vaš nalog. Da biste pristupili Vašem nalogu, potrebno je da se ulogujete.")
        opcija = input("Ukoliko želite da se ulogujete, unesite broj 1: ")
        if opcija == '1':
            print()
            return opcija
        else:
            print()
            return '-1'


def change_user(username):
    global dict_of_registered_users
    
    password = get_user_by_username(username)['password']
    firstname = get_user_by_username(username)['firstname']
    lastname = get_user_by_username(username)['lastname']

    while True:
        print("Opcije za promenu podataka: ")
        print("1: Promena lozinke.")
        print("2: Promena imena.")
        print("3: Promena prezimena.")
        print()

        allowed_characters = "123 ,"
        broj = input("Unesite koje podatke želite da promenite: ")
        if len(broj) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if broj == '-1':
            logout()
            print()
            return
        if not all(char in allowed_characters for char in broj):
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            print()
            continue

        if broj in ('1', '12', '13', '123'):
            password = input("Unesite novu lozinku: ")
            if password == '-1':
                print()
                return
            if not check_password(password):
                print()
                continue
            password_p = input("Potvrdite Vašu lozinku: ")
            if len(password_p) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if password != password_p:
                print("Lozinke se ne podudaraju. Unesite ih ponovo.")
                print()
                continue
            if password == get_user_by_username(username)['password']:
                print("Ne možete uneti staru lozinku. Unesite ponovo.")
                print()
                continue

        if broj in ('2', '12', '23', '123'):
            firstname = input("Unesite novo ime: ")
            if firstname == '-1':
                print()
                return
            if not check_name(firstname):
                print("Ime sme da sadrži samo razmake ili slova. Unesite ponovo.")
                print()
                continue
            if firstname == get_user_by_username(username)['firstname']:
                print("Ne možete uneti staro ime. Unesite ponovo.")
                print()
                continue

        if broj in ('3', '13', '23', '123'):
            lastname = input("Unesite novo prezime: ")
            if lastname == '-1':
                print()
                return
            if not check_name(lastname):
                print("Prezime sme da sadrži samo razmake ili slova. Unesite ponovo.")
                print()
                continue
            if lastname == get_user_by_username(username)['lastname']:
                print("Ne možete uneti staro prezime. Unesite ponovo.")
                print()
                continue
        
        get_user_by_username(username)['password'] = password
        get_user_by_username(username)['firstname'] = firstname
        get_user_by_username(username)['lastname'] = lastname

        print()
        print("Uspešno ste izmenili podatke Vašeg naloga.")
        print()
        return
        
if __name__ == '__main__':
    pass