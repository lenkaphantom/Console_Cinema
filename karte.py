from globalne_promenljive import *
from funkcije_provere import *
import termin_projekcije
import sala
import menadzer


def load_from_file(filename='karte.txt'):
    with open(filename, 'r', encoding="utf-8") as termin_projekcije:
        for line in termin_projekcije:
            tickets = line.strip().split(" | ")
            if len(tickets) == 7:
                index, name, date_of_screening, seat, date, type_of_ticket, active = tickets
                tickets_dict = {
                    "name": name,
                    "date_of_screening": date_of_screening,
                    "seat": seat,
                    "date": date,
                    "type_of_ticket": type_of_ticket,
                    "active": active
                 }
                dict_of_tickets[index] = tickets_dict
        
    with open("prodate_karte.txt", 'r', encoding="utf-8") as prodate_karte:
        for line in prodate_karte:
            tickets = line.strip().split(" | ")
            if len(tickets) == 3:
                index, salesman, ticket_cost = tickets
                salesman_dict = {
                    "username": salesman,
                    "ticket_cost": ticket_cost
                }
                salesman_tickets[index] = salesman_dict


def write_to_file(filename='karte.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for index, tickets_dict in dict_of_tickets.items():
            file.write(f"{index} | {tickets_dict['name']} | {tickets_dict['date_of_screening']} | {tickets_dict['seat']} | {tickets_dict['date']} | {tickets_dict['type_of_ticket']} | {tickets_dict['active']}\n")

    with open("prodate_karte.txt", 'w', encoding="utf-8") as file:
        for index, salesman_dict in salesman_tickets.items():
            file.write(f"{index} | {salesman_dict['username']} | {salesman_dict['ticket_cost']}\n")


def choose_date_of_screening():
    while True:
        print("Odaberite termin projekcije: ")
        print("1. Odaberite pretragom termina projekcije.")
        print("2. Odaberite unosom šifre termina projekcije.")
        print()
        opcija = input("Unesite opciju koju želite: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            return opcija
        elif opcija == '1':
            backup_dict = termin_projekcije.search_date_of_screening()
            if backup_dict == '-1':
                return backup_dict
            index = input("Unesite indeks ispred termina projekcije: ")
            if index == '-1':
                return index
            if not int(index) in backup_dict.keys():
                print("Niste uneli ispravan indeks. Unesite ponovo.")
                continue
            return backup_dict[int(index)]
        elif opcija == '2':
            termin_projekcije.print_date_of_screening()
            passcode = input("Unesite šifru termina projekcije: ")
            return passcode
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            continue


def available_tickets():
    global dict_of_booked_tickets

    for date_of_screenings_dict in dict_of_date_of_screenings.values():
        seats_dict = {}
        
        date_of_screening_passcode = date_of_screenings_dict['passcode']
        screening_passcode = date_of_screening_passcode[0:4]
        auditorium = dict_of_cinema_screenings[screening_passcode]['auditorium']

        number_of_rows = int(dict_of_auditoriums[auditorium]['number_of_rows'])
        seats_string = dict_of_auditoriums[auditorium]['seats']
        seats_list = [seat.strip() for seat in seats_string.split(',')]

        for row in range(1, number_of_rows + 1):
            seats_dict[row] = seats_list

        dict_of_booked_tickets[date_of_screening_passcode] = seats_dict       

    for ticket_dict in dict_of_tickets.values():
        date_of_screening_passcode = ticket_dict['date_of_screening']
        seats_dict = dict_of_booked_tickets[date_of_screening_passcode]

        row = ""
        seat = ""
        for char in ticket_dict['seat']:
            if char.isdigit():
                row += char
            else:
                seat += char

        row = int(row)
        index = 0
        seats_list = seats_dict[row]
        for seat_temp in seats_list:
            if seat_temp == seat:
                break
            index += 1
        if ticket_dict['active'] == 'True':
            seat_list_temp = seats_list.copy()
            seat_list_temp[index] = '*'
            seats_dict[row] = seat_list_temp

        dict_of_booked_tickets[date_of_screening_passcode] = seats_dict


def book_menu(number):
    while True:
        print("Kome želite da rezervišete kartu?")
        print("1: Registrovanom korisniku.")
        print("2: Neregistrovanom korisniku.")
        print()

        opcija = input("Unesite broj koji želite: ")
        print()
        if len(opcija) < 1:
            print("Polje nije popunjeno, Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            print()
            return
        if opcija == '1':
            username = input("Unesite korisničko ime korisnika: ")
            print()
            if len(username) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if username == '-1':
                print()
                return
            if not username in dict_of_registered_users.keys() or dict_of_registered_users[username]['role'] != roles[1]:
                print("Niste uneli ispravan username. Unesite ponovo.")
                print()
                continue
            book_ticket(number, username)
            continue
        elif opcija == '2':
            book_ticket(number)
            continue
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            print()
            continue


def book_ticket(number, username = None):
    global dict_of_booked_tickets
    seats_dict = {}

    while True:
        tickets_index = list(dict_of_tickets.keys())
        index = int(tickets_index[-1]) + 1

        name = None
        if username == None:
            name = input("Unesite ime i prezime: ")
            print()
            if name == '-1':
                print()
                return
            if ' ' not in name:
                print("Uneli ste neispravno ime i prezime. Unesite ponovo.")
                print()
                continue
            if not check_name(name):
                print()
                continue

        date_of_screening = choose_date_of_screening()
        if date_of_screening == '-1':
            print()
            return '-1'
        
        screening_passcode = date_of_screening[0:4]
        auditorium_passcode = dict_of_cinema_screenings[screening_passcode]['auditorium']
        print()
        print("Odaberite sedište koje želite da rezervišete.")
        print("Napomena: Sedišta označena sa '*' su zauzeta!")
        print()

        seats_dict = dict_of_booked_tickets[date_of_screening]
        sala.print_seats_rows(seats_dict)

        seats_string = dict_of_auditoriums[auditorium_passcode]['seats']
        seats_list = [seat.strip() for seat in seats_string.split(',')]

        row = input("Unesite broj reda u kojem želite da rezervišete sedište: ")
        if row == '-1':
            print()
            continue
        if not check_ticket_row(row, auditorium_passcode):
            print()
            continue

        seat = input("Unesite oznaku sedišta koje želite da rezervišete: ")
        if seat == '-1':
            print()
            continue
        if not check_ticket_seat(seat, auditorium_passcode):
            print()
            continue

        i = 0
        for seat_temp in seats_list:
            if seat_temp == seat:
                break
            i += 1
            
        seat_list = seats_dict[int(row)]
        if seat_list[i] == '*':
            print("Sedište je zauzeto. Unesite ponovo.")
            print()
            continue

        temp_seat_list = seat_list.copy()
        temp_seat_list[i] = '*'
        seats_dict[int(row)] = temp_seat_list

        dict_of_booked_tickets[date_of_screening] = seats_dict

        today = datetime.now()
        date_ = today.strftime("%d.%m.%Y")

        if number == 1:
            type_of_ticket = types_of_tickets[0]
        else:
            type_of_ticket = types_of_tickets[1]

        active = 'True'
        seat = row + seat

        if name == None:
            name = username

        ticket_dict = {
            "name": name,
            "date_of_screening": date_of_screening,
            "seat": seat,
            "date": date_,
            "type_of_ticket": type_of_ticket,
            "active": active
        }
        dict_of_tickets[str(index)] = ticket_dict
        available_tickets()
        if number == 1:
            continue
        return index
    

def check_ticket_active():
    global dict_of_tickets

    for ticket_dict in dict_of_tickets.values():
        date_of_screening_passcode = ticket_dict['date_of_screening']
        date_of_screening_dict = dict_of_date_of_screenings[date_of_screening_passcode]
        if date_of_screening_dict['active'] == 'False':
            ticket_dict['active'] = 'False'


def print_ticket(username, bb_ticket_dict = dict_of_tickets):
    dict_backup = {}
    print(f"+{'-'*3}+{'-' * 10}+{'-' * 50}+{'-' * 15}+{'-' * 20}+{'-'*20}+{'-'*7}+")
    print(f"|{'ID':<3}|{'Passcode':<10}|{'Movie name':<50}|{'Date':<15}|{'Time beginning':<20}|{'Time ending':<20}|{'Seat':<7}|")
    print(f"+{'-'*3}+{'-' * 10}+{'-' * 50}+{'-' * 15}+{'-' * 20}+{'-'*20}+{'-'*7}+")

    for index, ticket_dict in bb_ticket_dict.items():
        if ticket_dict['name'] == username and ticket_dict['active'] == 'True':
            date_of_screening_passcode = ticket_dict['date_of_screening']
            screening_passcode = date_of_screening_passcode[0:4]
            screening_dict = dict_of_cinema_screenings[screening_passcode]
            date_of_screening_dict = dict_of_date_of_screenings[date_of_screening_passcode]
            movie_index = screening_dict['movie']
            print(f"|{index:<3}|{date_of_screening_passcode:<10}|{dict_of_movies[movie_index]['name'][:50]:<50}|{date_of_screening_dict['date']:<15}|{screening_dict['time_beginning']:<20}|{screening_dict['time_ending']:<20}|{ticket_dict['seat']:<7}|")
            dict_backup[index] = ticket_dict
    print(f"+{'-'*3}+{'-' * 10}+{'-' * 50}+{'-' * 15}+{'-' * 20}+{'-'*20}+{'-'*7}+")
    print()
    return dict_backup


def print_ticket_salesman(number, bb_ticket_dict = dict_of_tickets):
    print(f"+{'-'*3}+{'-' * 10}+{'-' * 40}+{'-' * 30}+{'-' * 15}+{'-' * 10}+{'-'*10}+{'-'*5}+{'-'*15}+")
    print(f"|{'ID':<3}|{'Passcode':<10}|{'Name':<40}|{'Movie name':<30}|{'Date':<15}|{'Time beg':<10}|{'Time end':<10}|{'Seat':<5}|{'Type':<15}|")
    print(f"+{'-'*3}+{'-' * 10}+{'-' * 40}+{'-' * 30}+{'-' * 15}+{'-' * 10}+{'-'*10}+{'-'*5}+{'-'*15}+")

    for index, ticket_dict in bb_ticket_dict.items():
        if ticket_dict['active'] == 'True':
            date_of_screening_passcode = ticket_dict['date_of_screening']
            screening_passcode = date_of_screening_passcode[0:4]
            screening_dict = dict_of_cinema_screenings[screening_passcode]
            date_of_screening_dict = dict_of_date_of_screenings[date_of_screening_passcode]
            movie_index = screening_dict['movie']
            if number == 1 and ticket_dict['type_of_ticket'] == 'kupljena':
                continue
            print(f"|{index:<3}|{date_of_screening_passcode:<10}|{ticket_dict['name'][:40]:<40}|{dict_of_movies[movie_index]['name'][:30]:<30}|{date_of_screening_dict['date']:<15}|{screening_dict['time_beginning']:<10}|{screening_dict['time_ending']:<10}|{ticket_dict['seat']:<5}|{ticket_dict['type_of_ticket']:<15}|")
    print(f"+{'-'*3}+{'-' * 10}+{'-' * 40}+{'-' * 30}+{'-' * 15}+{'-' * 10}+{'-'*10}+{'-'*5}+{'-'*15}+")
    print()


def cancle_ticket(username = None):
    global dict_of_tickets

    while True:
        print("Pregled karata: ")
        if username == None:
            print_ticket_salesman(0)
            tickets_dict = dict_of_tickets
        else:
            tickets_dict = print_ticket(username)
        opcija = input("Odaberite indeks karte koju želite da poništite: ")
        if opcija == '-1':
            print()
            return
        if not opcija in tickets_dict.keys() or tickets_dict[opcija]['active'] == 'False':
            print("Uneli ste neispravan indeks. Unesite ponovo.")
            print()
            continue
        dict_of_tickets[opcija]['active'] = 'False'
        print("Uspešno ste poništili kartu.")
        available_tickets()
        print()
    

def sell_ticket(salesman):
    global salesman_tickets

    while True:
        print("Kome želite da prodate kartu?")
        print("1: Registrovanom korisniku.")
        print("2: Neregistrovanom korisniku.")
        print()

        opcija = input("Unesite broj koji želite: ")
        print()
        if len(opcija) < 1:
            print("Polje nije popunjeno, Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            print()
            return
        if opcija == '1':
            username = input("Unesite korisničko ime korisnika: ")
            print()
            if len(username) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if username == '-1':
                print()
                return
            if not username in dict_of_registered_users.keys() or dict_of_registered_users[username]['role'] != roles[1]:
                print("Niste uneli ispravan username. Unesite ponovo.")
                print()
                continue
            index = str(book_ticket(2, username))
            if index == '-1':
                print()
                return
            print("Uspešno ste prodali kartu.")
            print()
            passcode = dict_of_tickets[index]['date_of_screening']
            screening_passcode = passcode[0:4]
            screening_date = datetime.strptime(dict_of_date_of_screenings[passcode]['date'], "%d.%m.%Y")
            day_index = screening_date.weekday()
            day = days_of_week[day_index]
            screening_passcode = dict_of_tickets[index]['date_of_screening'][0:4]
            ticket_cost = change_ticket_cost(day, float(dict_of_cinema_screenings[screening_passcode]['ticket_cost']))
            ticket_cost *= menadzer.discount_loyalty_card(username)
            salesman_dict = {
                "username": salesman,
                "ticket_cost": ticket_cost
            }
            salesman_tickets[index] = salesman_dict
            available_tickets()
            continue
        elif opcija == '2':
            index = str(book_ticket(2))
            if index == '-1':
                print()
                return
            print("Uspešno ste prodali kartu.")
            print()
            passcode = dict_of_tickets[index]['date_of_screening']
            screening_passcode = passcode[0:4]
            screening_date = datetime.strptime(dict_of_date_of_screenings[passcode]['date'], "%d.%m.%Y")
            day_index = screening_date.weekday()
            day = days_of_week[day_index]
            ticket_cost = change_ticket_cost(day, float(dict_of_cinema_screenings[screening_passcode]['ticket_cost']))
            salesman_dict = {
                "username": salesman,
                "ticket_cost": ticket_cost
            }
            salesman_tickets[index] = salesman_dict
            available_tickets()
            continue
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            print()
            continue


def sell_booked_ticket(salesman):
    global dict_of_tickets, salesman_tickets

    while True:
        print("Pregled karata: ")
        print_ticket_salesman(1)
        opcija = input("Odaberite indeks karte koju želite da prodate: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            print()
            return
        if opcija not in dict_of_tickets.keys() or dict_of_tickets[opcija]['active'] == 'False':
            print("Uneli ste neispravan indeks. Unesite ponovo.")
            print()
            continue
        today = datetime.now()
        passcode = dict_of_tickets[opcija]['date_of_screening']
        screening_passcode = passcode[0:4]
        screening_date = datetime.strptime(dict_of_date_of_screenings[passcode]['date'], "%d.%m.%Y")
        print("Uspešno ste prodali kartu.")
        print()
        username = dict_of_tickets[opcija]['name']
        day_index = screening_date.weekday()
        day = days_of_week[day_index]
        ticket_cost = change_ticket_cost(day, float(dict_of_cinema_screenings[screening_passcode]['ticket_cost']))
        ticket_cost *= menadzer.discount_loyalty_card(username)
        salesman_dict = {
            "username": salesman,
            "ticket_cost": ticket_cost
        }
        dict_of_tickets[opcija]['type_of_ticket'] = types_of_tickets[1]
        dict_of_tickets[opcija]['date'] = today.strftime("%d.%m.%Y")
        salesman_tickets[opcija] = salesman_dict
        available_tickets()
        continue
    

def search_date_passcode(passcode, bb_ticket_dict = dict_of_tickets):
    search_ticket_dict = {}

    for index, ticket_dict in bb_ticket_dict.items():
        if ticket_dict['date_of_screening'] == passcode:
            search_ticket_dict[index] = ticket_dict

    return search_ticket_dict


def search_first_last_name(name, bb_ticket_dict = dict_of_tickets):
    search_ticket_dict = {}

    for index, ticket_dict in bb_ticket_dict.items():
        if name in ticket_dict['name']:
            search_ticket_dict[index] = ticket_dict

    return search_ticket_dict


def search_date_ticket(date, bb_ticket_dict = dict_of_tickets):
    search_ticket_dict = {}

    for index, ticket_dict in bb_ticket_dict.items():
        passcode = ticket_dict['date_of_screening']
        if dict_of_date_of_screenings[passcode]['date'] == date:
            search_ticket_dict[index] = ticket_dict

    return search_ticket_dict


def search_time_menu():
    print("1: Minimalno vreme početka projekcije.")
    print("2: Maksimalno vreme zarvšetka projekcije.")
    print("3: Navođenje obeju granica.")

    while True:
        opcija = input("Unesite opciju koju želite: ")
        if opcija == '-1':
            return opcija
        elif opcija == '1':
            time_beginning = input("Unesite vreme početka: ")
            if len(time_beginning) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            return search_time_beginning(time_beginning)
        elif opcija == '2':
            time_ending = input("Unesite vreme završetka: ")
            if len(time_ending) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            return search_time_ending(time_ending)
        elif opcija == '3':
            time_beginning = input("Unesite vreme početka: ")
            time_ending = input("Unesite vreme završetka: ")
            if len(time_beginning) < 1 or len(time_ending) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            return search_time(time_beginning, time_ending)
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            continue
        

def search_time(time_beginning, time_ending, bb_ticket_dict = dict_of_tickets):
    search_ticket_dict = {}

    for index, ticket_dict in bb_ticket_dict.items():
        screening_passcode = ticket_dict['date_of_screening'][0:4]
        if (time_beginning <= dict_of_cinema_screenings[screening_passcode]['time_beginning']) and (time_ending >= dict_of_cinema_screenings[screening_passcode]['time_ending']):
            search_ticket_dict[index] = ticket_dict

    return search_ticket_dict


def search_time_beginning(time_beginning, bb_ticket_dict = dict_of_tickets):
    search_ticket_dict = {}

    for index, ticket_dict in bb_ticket_dict.items():
        screening_passcode = ticket_dict['date_of_screening'][0:4]
        if time_beginning <= dict_of_cinema_screenings[screening_passcode]['time_beginning']:
            search_ticket_dict[index] = ticket_dict

    return search_ticket_dict


def search_time_ending(time_ending, bb_ticket_dict = dict_of_tickets):
    search_ticket_dict = {}

    for index, ticket_dict in bb_ticket_dict.items():
        screening_passcode = ticket_dict['date_of_screening'][0:4]
        if time_ending >= dict_of_cinema_screenings[screening_passcode]['time_ending']:
            search_ticket_dict[index] = ticket_dict

    return search_ticket_dict


def search_type_of_ticket(type_of_ticket, bb_ticket_dict = dict_of_tickets):
    search_ticket_dict = {}

    for index, ticket_dict in bb_ticket_dict.items():
        if ticket_dict['type_of_ticket'] == type_of_ticket:
            search_ticket_dict[index] = ticket_dict

    return search_ticket_dict


def search_ticket():
    while True: 
        print("Opcije za pretragu karata: ")
        print("1: Pretraga po šifri termina projekcije.")
        print("2: Pretraga po imenu kupca.")
        print("3: Pretraga po prezimenu kupca.")
        print("4: Pretraga po datumu projekcije.")
        print("5: Pretraga po vremenu projekcije.")
        print("6: Pretraga po tipu karte.")
        print()

        opcija = input("Unesite broj ispred opcije: ")
        print()
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            print()
            return
        if opcija == '1':
            passcode = input("Unesite šifru termina projekcije: ")
            if len(passcode) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if passcode == '-1':
                print()
                return
            print_ticket_salesman(0, search_date_passcode(passcode))
            return
        elif opcija == '2':
            firstname = input("Unesite ime korisnika: ")
            if len(firstname) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if firstname == '-1':
                print()
                return 
            print_ticket_salesman(0, search_first_last_name(firstname))
            return
        elif opcija == '3':
            lastname = input("Unesite prezime korisnika: ")
            if len(lastname) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if lastname == '-1':
                print()
                return 
            print_ticket_salesman(0, search_first_last_name(lastname))
            return
        elif opcija == '4':
            date = input("Unesite datum projekcije u obliku 'D.M.G': ")
            if len(date) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if date == '-1':
                print()
                continue
            if not check_valid_date(date):
                print()
                continue
            print_ticket_salesman(0, search_date_ticket(date))
            return
        elif opcija == '5':
            ticket_dict = search_time_menu()
            if ticket_dict == '-1':
                print()
                return
            print_ticket_salesman(0, ticket_dict)
            return
        elif opcija == '6':
            type_of_ticket = input("Unesite tip karte: ")
            if len(type_of_ticket) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if type_of_ticket == '-1':
                print()
                return
            print_ticket_salesman(0, search_type_of_ticket(type_of_ticket))
            return
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            continue


def automatically_cancle_ticket():
    global dict_of_tickets

    for index, ticket_dict in dict_of_tickets.items():
        today = datetime.now()
        date_today = today.strftime("%d.%m.%Y")
        time_today = today.strftime("%H:%M")
        passcode = ticket_dict['date_of_screening']
        if date_today == dict_of_date_of_screenings[passcode]['date']:
            screening_passcode = passcode[0:4]
            time_today = datetime.strptime(time_today, "%H:%M")
            time_start = datetime.strptime(dict_of_cinema_screenings[screening_passcode]['time_beginning'], "%H:%M")
            time_today += timedelta(minutes = 30)
            if time_today >= time_start:
                dict_of_tickets[index]['active'] = 'False'
                print("Uspešno ste poništili kartu.")
    available_tickets()
    print()
    return

def change_ticket():
    while True:
        while True:
            print("Pregled karata: ")
            print_ticket_salesman(0)
            index = input("Odaberite indeks karte koju želite da promenite: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            if not index in dict_of_tickets.keys() or dict_of_tickets[index]['active'] == 'False':
                print("Uneli ste neispravan indeks. Unesite ponovo.")
                print()
                continue
            break

        passcode = dict_of_tickets[index]['date_of_screening']
        name = dict_of_tickets[index]['name']
        seat = dict_of_tickets[index]['seat']
        while True:
            print("Opcije za izmenu karte: ")
            print("1: Izmena termina bioskopske projekcije")
            print("2: Izmena imena i prezimena kupca")
            print("3: Izmena sedišta")
            print()

            allowed_characters = "123 ,"
            opcija = input("Unesite broj(eve) ispred opcije: ")
            if len(opcija) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if opcija == '-1':
                print()
                return
            if not all(char in allowed_characters for char in opcija):
                print("Niste uneli ispravnu opciju. Unesite ponovo.")
                print()
                continue
            if '1' in opcija:
                if '3' not in opcija:
                    print("Da biste promenili termin projekcije na karti, morate promeniti i sedište. Unesite ponovo.")
                    print()
                    continue
                passcode = choose_date_of_screening()
                if passcode == '-1':
                    print()
                    return
            if '2' in opcija:
                if name in dict_of_registered_users.keys():
                    print("Ne možete da promenite korisničko ime. Unesite ponovo.")
                    print()
                    continue
                name = input("Unesite ime i prezime: ")
                print()
                if name == '-1':
                    print()
                    return
                if not check_name(name):
                    print()
                    continue
            if '3' in opcija:
                screening_passcode = passcode[0:4]
                auditorium_passcode = dict_of_cinema_screenings[screening_passcode]['auditorium']
                print()
                print("Odaberite sedište koje želite da rezervišete.")
                print("Napomena: Sedišta označena sa '*' su zauzeta!")
                print()

                seats_dict = dict_of_booked_tickets[passcode]
                sala.print_seats_rows(seats_dict)

                seats_string = dict_of_auditoriums[auditorium_passcode]['seats']
                seats_list = [seat.strip() for seat in seats_string.split(',')]

                row = input("Unesite broj reda u kojem želite da rezervišete sedište: ")
                if row == '-1':
                    print()
                    continue
                if not check_ticket_row(row, auditorium_passcode):
                    print()
                    continue

                seat = input("Unesite oznaku sedišta koje želite da rezervišete: ")
                if seat == '-1':
                    print()
                    continue
                if not check_ticket_seat(seat, auditorium_passcode):
                    print()
                    continue

                i = 0
                for seat_temp in seats_list:
                    if seat_temp == seat:
                        break
                    i += 1
                    
                seat_list = seats_dict[int(row)]
                if seat_list[i] == '*':
                    print("Sedište je zauzeto. Unesite ponovo.")
                    print()
                    continue

                temp_seat_list = seat_list.copy()
                temp_seat_list[i] = '*'
                seats_dict[int(row)] = temp_seat_list

                dict_of_booked_tickets[passcode] = seats_dict
                seat = row + seat
            
            dict_of_tickets[index]['date_of_screening'] = passcode
            dict_of_tickets[index]['name'] = name
            dict_of_tickets[index]['seat'] = seat
            available_tickets()

            break
        continue
    

def change_ticket_cost(day_of_week, ticket_cost):
    if day_of_week == 'utorak':
        ticket_cost -= 50
    if day_of_week == 'subota' or day_of_week == 'nedelja':
        ticket_cost += 50
    return ticket_cost


if __name__ == '__main__':
    load_from_file()
    write_to_file()