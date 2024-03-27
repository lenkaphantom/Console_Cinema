from globalne_promenljive import *
from funkcije_provere import *
import datetime
import projekcija
import filmovi
import sala


def load_from_file(filename='termin_projekcije.txt'):
    with open(filename, 'r', encoding="utf-8") as termin_projekcije:
        for line in termin_projekcije:
            cinema_screening_date = line.strip().split(" | ")
            if len(cinema_screening_date) == 3:
                passcode, date, active = cinema_screening_date
                date_of_screenings_dict = {
                    "passcode": passcode,
                    "date": date,
                    "active": active
                }
                dict_of_date_of_screenings[passcode] = date_of_screenings_dict


def write_to_file(filename='termin_projekcije.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for date_of_screenings in dict_of_date_of_screenings.values():
            file.write(f"{date_of_screenings['passcode']} | {date_of_screenings['date']} | {date_of_screenings['active']}\n")


def generate_passcode_letters():
    two_lettered_string = []

    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char_1 in characters:
        for char_2 in characters:
            char = char_1 + char_2
            two_lettered_string.append(char)
        
    return two_lettered_string


def count_occurrences(screening_passcode):
    count = 0
    for passcode in dict_of_date_of_screenings.keys():
        if passcode.startswith(screening_passcode):
            count += 1
    return count


def generate_date(day, week):
    today = datetime.date.today()
    for i in range(len(days_of_week)):
        if day.lower() == days_of_week[i]:
            return today + datetime.timedelta(days =- today.weekday() + i, weeks = week)
        

def generate_passcode_and_date(screening_passcode, two_lettered_string, day, num, week):
    global dict_of_date_of_screenings

    passcode = screening_passcode + two_lettered_string[num]
    date = generate_date(day, week)
    date = date.strftime("%d.%m.%Y")
    for key in dict_of_date_of_screenings.keys():
        if screening_passcode in key:
            if date == dict_of_date_of_screenings[key]['date']:
                return
    active = "True"
    date_of_screenings_dict = {
        "passcode": passcode,
        "date": date,
        "active": active
    }
    dict_of_date_of_screenings[passcode] = date_of_screenings_dict
    return True


def generate_date_of_screening():
    global dict_of_date_of_screenings
    two_lettered_string = generate_passcode_letters()

    for screening_passcode, screening_dict in dict_of_cinema_screenings.items():
        if screening_dict['active'] == 'False':
            continue
        days_list = [day.strip().lower() for day in screening_dict['days'].split(',')]
        num = count_occurrences(screening_passcode)
        for day in days_list:
            week = 2
            generate_passcode_and_date(screening_passcode, two_lettered_string, day, num, week)
            num += 1
            week += 1
            generate_passcode_and_date(screening_passcode, two_lettered_string, day, num, week)
            num += 1


def search_movies(movie, date_of_screenings_dict = dict_of_date_of_screenings):
    search_date_of_screening = {}

    for passcode, date_of_screening in date_of_screenings_dict.items():
        screening_passcode = passcode[0:4]
        index = dict_of_cinema_screenings[screening_passcode]['movie']
        if movie == dict_of_movies[index]['name']:
            search_date_of_screening[passcode] = date_of_screening

    return search_date_of_screening


def search_auditoriums(auditorium, date_of_screenings_dict = dict_of_date_of_screenings):
    search_date_of_screening = {}

    for passcode, date_of_screening in date_of_screenings_dict.items():
        screening_passcode = passcode[0:4]
        if auditorium == dict_of_cinema_screenings[screening_passcode]['auditorium']:
            search_date_of_screening[passcode] = date_of_screening

    return search_date_of_screening


def search_dates(date, date_of_screenings_dict = dict_of_date_of_screenings):
    search_date_of_screening = {}

    for passcode, date_of_screening in date_of_screenings_dict.items():
        if date == date_of_screening['date']:
            search_date_of_screening[passcode] = date_of_screening

    return search_date_of_screening


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
            if time_beginning == '-1':
                print()
                return '-1'
            return search_time_beginning(time_beginning)
        elif opcija == '2':
            time_ending = input("Unesite vreme završetka: ")
            if len(time_ending) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if time_ending == '-1':
                print()
                return '-1'
            return search_time_ending(time_ending)
        elif opcija == '3':
            time_beginning = input("Unesite vreme početka: ")
            if time_beginning == '-1':
                print()
                return '-1'
            time_ending = input("Unesite vreme završetka: ")
            if time_ending == '-1':
                print()
                return '-1'
            if len(time_beginning) < 1 or len(time_ending) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if time_ending > time_beginning:
                print("Uneli ste neispravna vremena. Unesite ponovo.")
                print()
                continue
            return search_time(time_beginning, time_ending)
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            continue
        

def search_time(time_beginning, time_ending, date_of_screenings_dict = dict_of_date_of_screenings):
    search_date_of_screening = {}
    
    for passcode, date_of_screening in date_of_screenings_dict.items():
        screening_passcode = passcode[0:4]
        if (time_beginning <= dict_of_cinema_screenings[screening_passcode]['time_beginning']) and (time_ending >= dict_of_cinema_screenings[screening_passcode]['time_ending']):
            search_date_of_screening[passcode] = date_of_screening

    return search_date_of_screening


def search_time_beginning(time_beginning, date_of_screenings_dict = dict_of_date_of_screenings):
    search_date_of_screening = {}

    for passcode, date_of_screening in date_of_screenings_dict.items():
        screening_passcode = passcode[0:4]
        if time_beginning <= dict_of_cinema_screenings[screening_passcode]['time_beginning']:
            search_date_of_screening[passcode] = date_of_screening

    return search_date_of_screening


def search_time_ending(time_ending, date_of_screenings_dict = dict_of_date_of_screenings):
    search_date_of_screening = {}

    for passcode, date_of_screening in date_of_screenings_dict.items():
        screening_passcode = passcode[0:4]
        if time_ending >= dict_of_cinema_screenings[screening_passcode]['time_ending']:
            search_date_of_screening[passcode] = date_of_screening

    return search_date_of_screening


def print_date_of_screening(date_of_screenings_dict = dict_of_date_of_screenings):
    backup_dict = {}

    print(f"+{'-' * 7}+{'-' * 10}+{'-' * 50}+{'-' * 15}+{'-' * 15}+{'-' * 20}+{'-'*20}+")
    print(f"|{'Index':<7}|{'Passcode':<10}|{'Name':<50}|{'Auditorium':<15}|{'Date':<15}|{'Time beginning':<20}|{'Time ending':<20}|")
    print(f"+{'-' * 7}+{'-' * 10}+{'-' * 50}+{'-' * 15}+{'-' * 15}+{'-' * 20}+{'-'*20}+")

    i = 1
    for passcode, date_of_screening in date_of_screenings_dict.items():
        screening_passcode = passcode[0:4]
        screening_dict = dict_of_cinema_screenings[screening_passcode]

        if screening_dict['active'] == 'True' and date_of_screening['active'] == 'True':
            index = screening_dict['movie']
            movie = dict_of_movies[index]
            print(f"|{i:<7}|{passcode:<10}|{movie['name'][:50]:<50}|{screening_dict['auditorium'][:15]:<15}|{date_of_screening['date'][:15]:<15}|{screening_dict['time_beginning'][:20]:<20}|{screening_dict['time_ending'][:20]:<20}|")
            backup_dict[i] = passcode
            i += 1
    print(f"+{'-' * 7}+{'-' * 10}+{'-' * 50}+{'-' * 15}+{'-' * 15}+{'-' * 20}+{'-'*20}+")
    print()

    return backup_dict


def search_date_of_screening():
    while True:
        print("Kriterijumi za pretragu.")
        print("1. Pretraga po filmovima.")
        print("2. Pretraga po salama.")
        print("3. Pretraga po datumima.")
        print("4. Pretraga po vremenu projekcija.")

        opcija = input("Unesite po kom kriterijumu želite da pretražujete termine projekcija: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            print()
            return '-1'
        elif opcija == '1':
            filmovi.print_movie(dict_of_movie_names)
            index = input("Unesite indeks ispred imena filma: ")
            if index == '-1':
                print()
                return
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return '-1'
            if index not in dict_of_movie_names.keys():
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
            date_of_screenings_dict = search_movies(dict_of_movie_names[index])
            if date_of_screenings_dict == {}:
                print("Ne postoji nijedan termin koji zadovoljava kriterijume. Unesite ponovo.")
                print()
                continue
            return print_date_of_screening(date_of_screenings_dict)
        elif opcija == '2':
            backup_dict = sala.print_auditorium()
            auditorium = input("Unesite indeks ispred sale: ")
            if len(auditorium) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if auditorium == '-1':
                print()
                return '-1'
            if auditorium not in backup_dict.keys():
                print("Uneli ste neispravan indeks. Unesite ponovo.")
                print()
                continue
            date_of_screenings_dict = search_auditoriums(backup_dict[auditorium])
            if date_of_screenings_dict == {}:
                print("Ne postoji nijedan termin koji zadovoljava kriterijume. Unesite ponovo.")
                print()
                continue
            return print_date_of_screening(date_of_screenings_dict)
        elif opcija == '3':
            date = input("Unesite datum u obliku 'D.M.G': ")
            if len(date) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if date == '-1':
                print()
                return '-1'
            if not check_valid_date(date):
                print()
                continue
            date_of_screenings_dict = search_dates(date)
            if date_of_screenings_dict == {}:
                print("Ne postoji nijedan termin koji zadovoljava kriterijume. Unesite ponovo.")
                print()
                continue
            return print_date_of_screening(date_of_screenings_dict)
        elif opcija == '4':
            date_of_screenings_dict = search_time_menu()
            if date_of_screenings_dict == '-1':
                print()
                return '-1'
            if date_of_screenings_dict == {}:
                print("Ne postoji nijedan termin koji zadovoljava kriterijume. Unesite ponovo.")
                print()
                continue
            return print_date_of_screening(date_of_screenings_dict)
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            print()
            continue


if __name__ == '__main__':
    filmovi.load_from_file()
    projekcija.load_from_file()
    load_from_file()
    #generate_date_of_screening()
    check_date_of_screening()
    search_date_of_screening()
    write_to_file()
    projekcija.write_to_file()
    filmovi.write_to_file()