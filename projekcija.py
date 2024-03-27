from globalne_promenljive import *
from funkcije_provere import *
import filmovi
import sala


def load_from_file(filename='projekcija.txt'):
    with open(filename, 'r', encoding="utf-8") as projekcija:
        for line in projekcija:
            cinema_screening = line.strip().split(" | ")
            if len(cinema_screening) == 8:
                passcode, auditorium, time_beginning, time_ending, days, movie, ticket_cost, active = cinema_screening
                cinema_screening_dict = {
                    "passcode": passcode,
                    "auditorium": auditorium,
                    "time_beginning": time_beginning,
                    "time_ending": time_ending,
                    "days": days,
                    "movie": movie,
                    "ticket_cost": ticket_cost,
                    "active": active
                }
                dict_of_cinema_screenings[passcode] = cinema_screening_dict


def write_to_file(filename='projekcija.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for cinema_screening in dict_of_cinema_screenings.values():
            file.write(f"{cinema_screening['passcode']} | {cinema_screening['auditorium']} | {cinema_screening['time_beginning']} | {cinema_screening['time_ending']} | {cinema_screening['days']} | {cinema_screening['movie']} | {cinema_screening['ticket_cost']} | {cinema_screening['active']}\n")


def add_screening():
    while True:
        passcode = input("Unesite šifru projekcije: ")
        if passcode == '-1':
            print()
            return
        if not check_screening_passcode(passcode):
            print()
            continue

        auditorium = input("Unesite šifru sale: ")
        if auditorium == '-1':
            print()
            return
        if auditorium not in dict_of_auditoriums.keys():
            print("Uneli ste neispravnu šifru sale. Unesite ponovo.")
            print()
            continue

        time_beginning = input("Unesite vreme početka prikazivanja filma: ")
        if time_beginning == '-1':
            print()
            return
        if not check_time(time_beginning):
            print()
            continue

        time_ending = input("Unesite vreme završetka prikazivanja filma: ")
        if time_ending == '-1':
            print()
            return
        if not check_time(time_ending):
            print()
            continue

        days = input("Unesite dane u nedelji kada se prikazuje film: ")
        if days == '-1':
            print()
            return
        if not check_days(days):
            print()
            continue
        
        print("Pregled filmova: ")
        filmovi.print_movies()
        movie = input("Unesite indeks filma koji se prikazuje: ")
        if movie == '-1':
            print()
            return
        if not check_movie_screening(movie):
            print()
            continue
        
        ticket_cost = input("Unesite cenu karte: ")
        if ticket_cost == '-1':
            print()
            return
        if not check_ticket_cost(ticket_cost):
            print()
            continue

        movie_name = dict_of_movies[movie]['name']

        if not check_cinema_screening(auditorium, time_beginning, time_ending, days, movie_name):
            print()
            continue

        active = 'True'
        
        cinema_screening_dict = {
                     "passcode": passcode,
                     "auditorium": auditorium,
                     "time_beginning": time_beginning,
                     "time_ending": time_ending,
                     "days": days,
                     "movie": movie,
                     "ticket_cost": ticket_cost,
                     "active": active
                 }
        dict_of_cinema_screenings[passcode] = cinema_screening_dict
        print(f"Uspešno ste dodali projekciju {passcode}.")
        print()
        return
    

def print_screening(opcija, screening_dict = dict_of_cinema_screenings):
    index = 1
    print(f"+{'-'*3}+{'-' * 10}+{'-' * 12}+{'-' * 50}+{'-' * 20}+{'-'*20}+")
    print(f"|{'ID':<3}|{'Passcode':<10}|{'Auditorium':<12}|{'Movie name':<50}|{'Time beginning':<20}|{'Time ending':<20}|")
    print(f"+{'-'*3}+{'-' * 10}+{'-' * 12}+{'-' * 50}+{'-' * 20}+{'-'*20}+")
    for passcode, screening_dict_bb in screening_dict.items():
        movie_id = screening_dict_bb['movie']
        movie_name = dict_of_movies[movie_id]['name']
        print(f"|{index:<3}|{passcode:<10}|{screening_dict_bb['auditorium']:<12}|{movie_name[:50]:<50}|{screening_dict_bb['time_beginning']:<20}|{screening_dict_bb['time_ending']:<20}|")
        index += 1
    print(f"+{'-'*3}+{'-' * 10}+{'-' * 12}+{'-' * 50}+{'-' * 20}+{'-'*20}+")
    print()

    if opcija == '-1':
        print()
        return opcija
    elif opcija == '9':
        passcode = input("Unesite šifru projekcije koju želite da obrišete: ")
        if passcode in screening_dict.keys():
            print()
            return passcode
        if passcode == '-1':
            return passcode
    elif opcija == '11':
        passcode = input("Unesite šifru projekcije koju želite da izmenite: ")
        if passcode in screening_dict.keys():
            print()
            return passcode
        if passcode == '-1':
            return passcode
    print("Uneli ste neispravnu opciju. Unesite ponovo.")
    return None
    

def delete_screening(screening_dict):
    screening_dict['active'] = 'False'
    print(f"Projekcija {screening_dict['passcode']} je obrisana.")
    print()
    return


def change_screening(passcode):
    auditorium = dict_of_cinema_screenings[passcode]['auditorium']
    time_beginning = dict_of_cinema_screenings[passcode]['time_beginning']
    time_ending = dict_of_cinema_screenings[passcode]['time_ending']
    days = dict_of_cinema_screenings[passcode]['days']
    movie = dict_of_cinema_screenings[passcode]['movie']
    ticket_cost = dict_of_cinema_screenings[passcode]['ticket_cost']

    while True:
        print("Odaberite podatke projekcije koje želite da izmenite: ")
        print("1: Sala projekcije.")
        print("2: Vreme početka projekcije.")
        print("3: Vreme završetka projekcije.")
        print("4: Dane u nedelji kada se prikazuje projekcija.")
        print("5: Film koji se prikazuje.")
        print("6: Cena karte za projekciju.")
        print()

        allowed_characters = "123456 ,"
        opcija = input("Unesite broj ispred podatka koji želite da izemnite: ")
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
            auditorium = input("Unesite novu šifru sale: ")
            if auditorium == '-1':
                print()
                return
            if auditorium == dict_of_cinema_screenings[passcode]['auditorium']:
                print("Ne možete da unesete staru salu. Unesite ponovo.")
                print()
                continue
            if auditorium not in dict_of_auditoriums.keys():
                print("Uneli ste neispravnu šifru sale. Unesite ponovo.")
                print()
                continue
        if '2' in opcija:
            time_beginning = input("Unesite novo vreme početka prikazivanja filma: ")
            if time_beginning == '-1':
                print()
                return
            if not check_time(time_beginning):
                print()
                continue
            if time_beginning == dict_of_cinema_screenings[passcode]['time_beginning']:
                print("Ne možete da unesete staro vreme početka prikazivanja filma. Unesite ponovo.")
                print()
                continue
        if '3' in opcija:
            time_ending = input("Unesite vreme završetka prikazivanja filma: ")
            if time_ending == '-1':
                print()
                return
            if not check_time(time_ending):
                print()
                continue
            if time_ending == dict_of_cinema_screenings[passcode]['time_ending']:
                print("Ne možete da unesete staro vreme početka prikazivanja filma. Unesite ponovo.")
                print()
                continue
        if '4' in opcija:
            days = input("Unesite nove dane u nedelji kada se prikazuje film: ")
            if days == '-1':
                print()
                return
            if not check_days(days):
                print()
                continue
            if days == dict_of_cinema_screenings[passcode]['days']:
                print("Ne možete da unesete stare dane u nedelji kada se prikazuje film. Unesite ponovo.")
                print()
                continue
        if '5' in opcija:
            filmovi.print_movies()
            movie = input("Unesite novi indeks filma koji se prikazuje: ")
            if movie == '-1':
                print()
                return
            if not check_movie_screening(movie):
                print()
                continue
            if movie == dict_of_cinema_screenings[passcode]['movie']:
                print("Ne možete da unesete stari indeks filma koji se prikazuje. Unesite ponovo.")
                print()
                continue
        if '6' in opcija:
            ticket_cost = input("Unesite cenu karte: ")
            if ticket_cost == '-1':
                print()
                return
            if not check_ticket_cost(ticket_cost):
                print()
                continue
            if ticket_cost == dict_of_cinema_screenings[passcode]['ticket_cost']:
                print("Ne možete da unesete staru cenu karte. Unesite ponovo.")
                print()
                continue

        movie_name = dict_of_movies[movie]['name']

        if not (auditorium == dict_of_cinema_screenings[passcode]['auditorium']
            and time_beginning == dict_of_cinema_screenings[passcode]['time_beginning']
            and time_ending == dict_of_cinema_screenings[passcode]['time_ending']
            and days == dict_of_cinema_screenings[passcode]['days']
            and movie == dict_of_cinema_screenings[passcode]['movie']
        ):
            if not check_cinema_screening(auditorium, time_beginning, time_ending, days, movie_name):
                print()
                continue

        dict_of_cinema_screenings[passcode]['auditorium'] = auditorium
        dict_of_cinema_screenings[passcode]['time_beginning'] = time_beginning
        dict_of_cinema_screenings[passcode]['time_ending'] = time_ending
        dict_of_cinema_screenings[passcode]['days'] = days
        dict_of_cinema_screenings[passcode]['movie'] = movie
        dict_of_cinema_screenings[passcode]['ticket_cost'] = ticket_cost

        print()
        print(f"Uspešno ste izmenili odabrane podakte projekcije {passcode}.")
        return


if __name__ == '__main__':
    sala.load_from_file()
    filmovi.load_from_file()
    load_from_file()
    add_screening()
    write_to_file()
    filmovi.write_to_file()
    sala.write_to_file()