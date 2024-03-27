from globalne_promenljive import *
from funkcije_provere import *
from login_logout import *

def registration_manager():
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

        password_p = input("Potvrdite vasu lozinku: ")
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

        firstname = input("Unesite vaše ime: ")
        if firstname == '-1':
            print()
            return
        if not check_name(firstname):
            print()
            continue
        
        lastname = input("Unesite vaše prezime: ")
        if lastname == '-1':
            print()
            return
        if not check_name(lastname):
            print()
            continue

        opcija = input("Unesite broj 1 ako želite da dodate prodavca, a broj 2 ako želite menadžera: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            continue
        if opcija == '-1':
            logout()
            return
        if opcija == '1':
            role = roles[2]
        elif opcija == '2':
            role = roles[3]
        else:
            print("Niste uneli ispravnu vrednost. Unesite ponovo.")
            continue

        user_dict = {
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "role": role
        }

        dict_of_registered_users[username] = user_dict

        if opcija == '1':
            print("Uspešno ste registrovali novog prodavca.")
        elif opcija == '2':
            print("Uspešno ste registrovali novog menadžera.")
        print()
        return


def print_users_accounts():
    print()
    for user in dict_of_registered_users.values():
        for key, value in user.items():
            print(f"{key} : {value}")
        print()


def discount_loyalty_card(username):
    today = datetime.now()
    today -= timedelta(days = 365)

    total_spent = 0
    for index, ticket_dict in dict_of_tickets.items():
        date_sold = datetime.strptime(ticket_dict['date'], "%d.%m.%Y")
        if ticket_dict['name'] == username and ticket_dict['type_of_ticket'] == types_of_tickets[1] and date_sold > today:
            if index in salesman_tickets.keys():
                total_spent += float(salesman_tickets[index]['ticket_cost'])

    if total_spent > 5000:
        return 0.9
    return 1