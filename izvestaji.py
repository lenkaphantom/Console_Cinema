from globalne_promenljive import *
from funkcije_provere import *
from login_logout import *
import korisnik
import filmovi
import projekcija
import sala
import termin_projekcije
import karte


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


def sold_tickets_by_date(date_sold):
    global report_a
    search_ticket_dict = {}

    for index, ticket_dict in dict_of_tickets.items():
        if ticket_dict['type_of_ticket'] == types_of_tickets[0]:
            continue
        if ticket_dict['date'] == date_sold:
            search_ticket_dict[index] = ticket_dict

    print(f"+{'-' * 15}+{'-' * 5}+{'-' * 15}+{'-' * 50}+")
    print(f"|{'Date_sold':<15}|{'ID':<5}|{'Passcode':<15}|{'Name':<50}|")
    print(f"+{'-' * 15}+{'-' * 5}+{'-' * 15}+{'-' * 50}+")

    for index, ticket_dict in search_ticket_dict.items():
        print(f"|{date_sold:<15}|{index:<5}|{ticket_dict['date_of_screening']:<15}|{ticket_dict['name'][:50]:<50}|")

    print(f"+{'-' * 15}+{'-' * 5}+{'-' * 15}+{'-' * 50}+")

    report_a[date_sold] = search_ticket_dict
    if search_ticket_dict == {}:
        print(f"Nijedna karta nije prodata za datum {date_sold}.")
        return search_ticket_dict

    opcija = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? Y/N: ")
    if opcija == 'Y' or opcija == 'y':
        write_report_a()

    return search_ticket_dict


def write_report_a(filename='izvestaj_a.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for date_sold, report in report_a.items():
            for index, tickets_dict in report.items():
                file.write(f"{date_sold} | {index} | {tickets_dict['name']} | {tickets_dict['date_of_screening']} | {tickets_dict['seat']} | {tickets_dict['active']}\n")


def sold_tickets_by_date_of_screening(date_of_screening):
    global report_b
    search_ticket_dict = {}

    for index, ticket_dict in dict_of_tickets.items():
        if ticket_dict['type_of_ticket'] == types_of_tickets[0]:
            continue
        passcode = ticket_dict['date_of_screening']
        if dict_of_date_of_screenings[passcode]['date'] == date_of_screening:
            search_ticket_dict[index] = ticket_dict

    print(f"+{'-' * 20}+{'-' * 5}+{'-' * 15}+{'-' * 50}+")
    print(f"|{'Date_of_screening':<20}|{'ID':<5}|{'Passcode':<15}|{'Name':<50}|")
    print(f"+{'-' * 20}+{'-' * 5}+{'-' * 15}+{'-' * 50}+")

    for index, ticket_dict in search_ticket_dict.items():
        print(f"|{date_of_screening:<20}|{index:<5}|{ticket_dict['date_of_screening']:<15}|{ticket_dict['name'][:50]:<50}|")

    print(f"+{'-' * 20}+{'-' * 5}+{'-' * 15}+{'-' * 50}+")

    report_b[date_of_screening] = search_ticket_dict
    if search_ticket_dict == {}:
        print(f"Nijedna karta nije prodata za datum projekcije {date_of_screening}.")
        return search_ticket_dict

    opcija = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? Y/N: ")
    if opcija == 'Y' or opcija == 'y':
        write_report_b()

    return search_ticket_dict


def write_report_b(filename='izvestaj_b.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for date_of_screening, report in report_b.items():
            for index, tickets_dict in report.items():
                file.write(f"{date_of_screening} | {index} | {tickets_dict['name']} | {tickets_dict['date']} | {tickets_dict['seat']} | {tickets_dict['active']}\n")


def sold_tickets_by_date_and_salesman(date_sold, salesman):
    global report_c
    search_ticket_dict = {}

    for index, ticket_dict in dict_of_tickets.items():
        if ticket_dict['type_of_ticket'] == types_of_tickets[0]:
            continue
        if ticket_dict['date'] == date_sold and salesman_tickets[index]['username'] == salesman:
            search_ticket_dict[index] = ticket_dict

    print(f"+{'-' * 15}+{'-' * 20}+{'-' * 5}+{'-' * 15}+{'-' * 50}+")
    print(f"|{'Date_sold':<15}|{'Salesman':<20}|{'ID':<5}|{'Passcode':<15}|{'Name':<50}|")
    print(f"+{'-' * 15}+{'-' * 20}+{'-' * 5}+{'-' * 15}+{'-' * 50}+")

    for index, ticket_dict in search_ticket_dict.items():
        print(f"|{date_sold:<15}|{salesman[:20]:<20}|{index:<5}|{ticket_dict['date_of_screening']:<15}|{ticket_dict['name'][:50]:<50}|")

    print(f"+{'-' * 15}+{'-' * 20}+{'-' * 5}+{'-' * 15}+{'-' * 50}+")

    id = date_sold + '|' + salesman
    report_c[id] = search_ticket_dict
    if search_ticket_dict == {}:
        print(f"Nijedna karta nije prodata za datum {date_sold}. i prodavca {salesman}.")
        return search_ticket_dict

    opcija = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? Y/N: ")
    if opcija == 'Y' or opcija == 'y':
        write_report_c()

    return search_ticket_dict


def write_report_c(filename='izvestaj_c.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for id, report in report_c.items():
            for index, tickets_dict in report.items():
                file.write(f"{id} | {index} | {tickets_dict['name']} | {tickets_dict['date_of_screening']} | {tickets_dict['seat']} | {tickets_dict['active']}\n")


def total_number_and_cost_for_day_of_selling(day):
    global report_d
    total_number = 0
    total_cost = 0

    for index, ticket_dict in dict_of_tickets.items():
        if ticket_dict['type_of_ticket'] == types_of_tickets[0]:
            continue
        date_sold = datetime.strptime(ticket_dict['date'], "%d.%m.%Y")
        day_sold = days_of_week[date_sold.weekday()]
        if day_sold == day:
            total_number += 1
            total_cost += float(salesman_tickets[index]['ticket_cost'])

    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+")
    print(f"|{'Day_sold':<20}|{'Total_number':<20}|{'Total_cost':<20}|")
    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+")
    print(f"|{day:<20}|{total_number:<20}|{total_cost:<20}|")
    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+")

    total_dict = {
        "total_number": total_number,
        "total_cost": total_cost
    }
    report_d[day] = total_dict

    opcija = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? Y/N: ")
    if opcija == 'Y' or opcija == 'y':
        write_report_d()

    return total_dict


def write_report_d(filename='izvestaj_d.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for day, report in report_d.items():
            file.write(f"{day} | {report['total_number']} | {report['total_cost']}\n")


def total_number_and_cost_for_day_of_screening(day):
    global report_e
    total_number = 0
    total_cost = 0

    for index, ticket_dict in dict_of_tickets.items():
        if ticket_dict['type_of_ticket'] == types_of_tickets[0]:
            continue
        passcode = ticket_dict['date_of_screening']
        date_screening = datetime.strptime(dict_of_date_of_screenings[passcode]['date'], "%d.%m.%Y")
        date_screening = days_of_week[date_screening.weekday()]
        if date_screening == day:
            total_number += 1
            total_cost += float(salesman_tickets[index]['ticket_cost'])

    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+")
    print(f"|{'Day_of_screening':<20}|{'Total_number':<20}|{'Total_cost':<20}|")
    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+")
    print(f"|{day:<20}|{total_number:<20}|{total_cost:<20}|")
    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+")

    total_dict = {
        "total_number": total_number,
        "total_cost": total_cost
    }
    report_e[day] = total_dict

    opcija = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? Y/N: ")
    if opcija == 'Y' or opcija == 'y':
        write_report_e()

    return total_dict


def write_report_e(filename='izvestaj_e.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for day, report in report_e.items():
           file.write(f"{day} | {report['total_number']} | {report['total_cost']}\n")


def total_cost_for_movie(movie_index):
    global report_f
    total_cost = 0

    for index, ticket_dict in dict_of_tickets.items():
        if ticket_dict['type_of_ticket'] == types_of_tickets[0]:
            continue
        screening_passcode = ticket_dict['date_of_screening'][0:4]
        if dict_of_cinema_screenings[screening_passcode]['movie'] == movie_index:
            total_cost += float(salesman_tickets[index]['ticket_cost'])

    print(f"+{'-' * 50}+{'-' * 20}+")
    print(f"|{'Movie':<50}|{'Total_cost':<20}|")
    print(f"+{'-' * 50}+{'-' * 20}+")
    print(f"|{dict_of_movies[movie_index]['name'][:50]:<50}|{total_cost:<20}|")
    print(f"+{'-' * 50}+{'-' * 20}+")

    report_f[movie_index] = total_cost

    opcija = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? Y/N: ")
    if opcija == 'Y' or opcija == 'y':
        write_report_f()

    return total_cost


def write_report_f(filename='izvestaj_f.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for movie_index, total_cost in report_f.items():
            file.write(f"{dict_of_movies[movie_index]['name']} | {total_cost}\n")


def total_number_and_cost_for_day_and_salesman(day, salesman):
    global report_g
    total_number = 0
    total_cost = 0

    for index, ticket_dict in dict_of_tickets.items():
        if ticket_dict['type_of_ticket'] == types_of_tickets[0]:
            continue
        date_sold = datetime.strptime(ticket_dict['date'], "%d.%m.%Y")
        day_sold = days_of_week[date_sold.weekday()]
        if day_sold == day and salesman_tickets[index]['username'] == salesman:
            total_number += 1
            total_cost += float(salesman_tickets[index]['ticket_cost'])

    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+{'-' * 20}+")
    print(f"|{'Day_of_screening':<20}|{'Salesman':<20}|{'Total_number':<20}|{'Total_cost':<20}|")
    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+{'-' * 20}+")
    print(f"|{day:<20}|{salesman[:20]:<20}|{total_number:<20}|{total_cost:<20}|")
    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+{'-' * 20}+")

    total_dict = {
        "total_number": total_number,
        "total_cost": total_cost
    }
    id = day + '|' + salesman
    report_g[id] = total_dict

    opcija = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? Y/N: ")
    if opcija == 'Y' or opcija == 'y':
        write_report_g()

    return total_dict


def write_report_g(filename='izvestaj_g.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for id, report in report_g.items():
            index = id.find('|')
            day = id[:index]
            salesman = id[index+1:]
            file.write(f"{day} | {salesman} | {report['total_number']} | {report['total_cost']}\n")


def total_number_and_cost_for_salesman():
    global report_h
    
    for username in dict_of_registered_users.keys():
        total_number = 0
        total_cost = 0
        if dict_of_registered_users[username]['role'] != roles[2]:
            continue
        for index, ticket_dict in dict_of_tickets.items():
            if ticket_dict['type_of_ticket'] == types_of_tickets[0]:
                continue
            date_sold = datetime.strptime(dict_of_tickets[index]['date'], "%d.%m.%Y")
            today = datetime.now()
            date_limit = today - timedelta(days = 30)
            if date_sold > date_limit and salesman_tickets[index]['username'] == username:
                total_number += 1
                total_cost += float(salesman_tickets[index]['ticket_cost'])

        total_dict = {
            "total_number": total_number,
            "total_cost": total_cost
        }
        report_h[username] = total_dict

    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+")
    print(f"|{'Salesman':<20}|{'Total_number':<20}|{'Total_cost':<20}|")
    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+")
    for salesman, total_dict in report_h.items():
        print(f"|{salesman[:20]:<20}|{total_dict['total_number']:<20}|{total_dict['total_cost']:<20}|")
    print(f"+{'-' * 20}+{'-' * 20}+{'-' * 20}+")

    opcija = input("Da li želite da sačuvate izveštaj u tekstualnu datoteku? Y/N: ")
    if opcija == 'Y' or opcija == 'y':
        write_report_h()

    return total_dict


def write_report_h(filename='izvestaj_h.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for salesman, report in report_h.items():
            file.write(f"{salesman} | {report['total_number']} | {report['total_cost']}\n")


def report_menu():
    while True:
        print("Odaberite koji izveštaj želite da vidite: ")
        print("1: Prodate karte za datum prodaje.")
        print("2: Prodate karte za datum projekcije.")
        print("3: Prodate karte za datum prodaje i prodavca.")
        print("4: Ukupan broj prodatih karata i ukupna cena za dan prodaje.")
        print("5: Ukupan broj prodatih karata i ukupna cena za dan projekcije.")
        print("6: Ukupna cena prodatih karata za film.")
        print("7: Ukupan broj prodatih karata i ukupna cena za dan prodaje i prodavca.")
        print("8: Ukupan broj prodatih karata i ukupna cena za prodavca u poslednjih 30 dana.")
        print()
        opcija = input("Unesite broj ispred opcije koju želite: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            print()
            return
        if opcija == '1':
            date_sold = input("Unesite datum prodaje: ")
            if len(date_sold) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if date_sold == '-1':
                print()
                return
            if not check_valid_date(date_sold):
                print()
                continue
            sold_tickets_by_date(date_sold)
            return
        elif opcija == '2':
            date_screening = input("Unesite datum projekcije: ")
            if len(date_screening) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if date_screening == '-1':
                print()
                return
            if not check_valid_date(date_screening):
                print()
                continue
            sold_tickets_by_date_of_screening(date_screening)
            return
        elif opcija == '3':
            date_sold = input("Unesite datum prodaje: ")
            if len(date_sold) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if date_sold == '-1':
                print()
                return
            if not check_valid_date(date_sold):
                print()
                continue
            salesman = input("Unesite prodavca: ")
            if len(salesman) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if salesman == '-1':
                print()
                return
            if not salesman in dict_of_registered_users.keys() or dict_of_registered_users[salesman]['role'] != roles[2]:
                print("Uneli ste neispravnog prodavca. Unesite ponovo.")
                print()
                continue
            sold_tickets_by_date_and_salesman(date_sold, salesman)
            return
        elif opcija == '4':
            day = input("Unesite dan prodaje: ")
            if len(day) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if day == '-1':
                print()
                return
            total_number_and_cost_for_day_of_selling(day)
            return
        elif opcija == '5':
            day = input("Unesite dan projekcije: ")
            if len(day) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if day == '-1':
                print()
                return
            total_number_and_cost_for_day_of_screening(day)
            return
        elif opcija == '6':
            print("Pregled filmova: ")
            filmovi.print_movies()
            movie_index = input("Unesite indeks filma: ")
            if len(movie_index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if movie_index == '-1':
                print()
                return
            if movie_index not in dict_of_movies.keys() or dict_of_movies[movie_index]['active'] == 'False':
                print("Niste uneli ispravan indeks. Unesite ponovo.")
                print()
                continue
            total_cost_for_movie(movie_index)
            return
        elif opcija == '7':
            day = input("Unesite dan prodaje: ")
            if len(day) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if day == '-1':
                print()
                return
            salesman = input("Unesite prodavca: ")
            if len(salesman) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if salesman == '-1':
                print()
                return
            if not salesman in dict_of_registered_users.keys() or dict_of_registered_users[salesman]['role'] != roles[2]:
                print("Uneli ste neispravnog prodavca. Unesite ponovo.")
                print()
                continue
            total_number_and_cost_for_day_and_salesman(day, salesman)
            return
        elif opcija == '8':
            total_number_and_cost_for_salesman()
            return
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            print()
            continue


if __name__ == '__main__':
    load_from_file()
    report_menu()
    write_to_file()