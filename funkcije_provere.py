from globalne_promenljive import *
from datetime import datetime, timedelta


def digit_in_string(string):
    for char in string:
        if char.isdigit():
            return True
    return False


def check_username(username):
    if len(username) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if ' ' in username:
        print("Korisničko ime ne sme da sadrži razmake. Unesite ponovo.")
        return False
    if username in dict_of_registered_users.keys():
        print("Korisničko ime već postoji. Unesite ponovo.")
        return False
    return True


def check_password(password):
    if len(password) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if len(password) <= 6:
        print("Lozinka mora biti duža od 6 karatkera. Unesite ponovo.")
        return False
    if not digit_in_string(password):
        print("Lozinka mora sadržati makar jednu cifru. Unesite ponovo.")
        return False
    if ' ' in password:
        print("Lozinka ne sme da sadrži razmake. Unesite ponovo.")
        return False
    return True


def check_name(name):
    allowed_characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZšđčćžŠĐČĆŽ"
    index = name.find(' ')
    if len(name) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if index == 0:
        print("Razmak ne sme da bude na početku vlastite imenice. Uneiste ponovo.")
        return False
    if name[0].islower():
        print("Vlastito ime mora počinjati velikim slovom. Unesite ponovo.")
        return False
    if index != -1:
        if name[index] == name[-1]:
            print("Razmak ne sme da bude na kraju imena. Unesite ponovo.")
            return False
        if name[index+1].islower():
            print("Vlastito ime mora počinjati velikim slovom. Unesite ponovo.")
            return False
    if not all(char in allowed_characters for char in name):
        print("Vlastito ime sme da sadrži samo razmake ili slova. Unesite ponovo.")
        return False
    return True


def check_movie_name(name):
    if len(name) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if '|' in name:
        print("Uneli ste neispravno ime filma. Unesite ponovo.")
        return False
    return True


def check_genre(genre):
    if len(genre) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if '|' in genre:
        print("Uneli ste neispravan žanr filma. Unesite ponovo.")
        return False
    if digit_in_string(genre):
        print("Uneli ste neispravan žanr filma. Unesite ponovo.")
        return False
    return True


def check_duration(duration):
    if len(duration) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if '|' in duration:
        print("Uneli ste neispravno vreme trajanja filma. Unesite ponovo.")
        return False
    if not duration.isdigit():
        print("Uneli ste neispravno vreme trajanja filma. Unesite ponovo.")
        return False
    return True


def check_names(names):
    if len(names) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    names_list = [name for name in names.split(', ')]
    for name in names_list:
        if not check_name(name):
            return False
    return True


def check_year(year):
    if len(year) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if not year.isdigit():
        print("Morate uneti ceo broj. Unesite ponovo.")
        return False
    if len(year) != 4:
        print("Broj mora biti četvorocifren. Unesite ponovo.")
        return False
    return True


def check_summary(summary):
    if len(summary) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if len(summary) > 1000:
        print("Rezime filma je previše dugačak. Unesite ponovo.")
        return False
    if '|' in summary:
        print("Uneli ste neispravan tekst. Unesite ponovo.")
        return False
    return True


def check_auditorium_passcode(passcode):
    if len(passcode) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if ' ' in passcode:
        print("Šifra sale ne može da sadrži razmak. Unesite ponovo.")
        return False
    if passcode in dict_of_auditoriums.keys():
        print("Šifra sale već postoji. Unesite ponovo.")
        return False
    return True


def check_auditorium_name(name):
    if '|' in name:
        print("Uneli ste neispravno ime sale. Unesite ponovo.")
        return False
    if name[0] == ' ':
        print("Razmak ne može biti na prvom mestu u imenu. Unesite ponovo.")
        return False
    if name[0].isdigit():
        print("Cifra ne može biti na prvom mestu u imenu. Unesite ponovo.")
        return False
    if name[0].islower():
        print("Ime mora počinjati velikim slovom. Unesite ponovo.")
        return False
    return True


def check_number_of_rows(number_of_rows):
    if len(number_of_rows) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if not number_of_rows.isdigit():
        print("Broj redova mora biti prirodan broj. Unesite ponovo.")
        return False
    return True


def check_seats(seats):
    if len(seats) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    seats_list = [seat.strip().lower() for seat in seats.split(',')]
    if not all(seat.isalpha() and seat.isupper() for seat in seats_list):
        print("Oznaka sedišta mora sadržati samo velika slova. Unesite ponovo.")
        return False
    return True


def check_screening_passcode(passcode):
    if len(passcode) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if len(passcode) != 4:
        print("Šifra projekcije mora biti četvorocifreni broj. Unesite ponovo.")
        return False
    if not passcode.isdigit():
        print("Šifra projekcije mora biti četvorocifreni broj. Unesite ponovo.")
        return False
    if passcode in dict_of_cinema_screenings.keys():
        print("Šifra već postoji. Unesite ponovo.")
        return False
    return True


def check_time(movie_time):
    try:
        min_time = "10:00"
        min_time = datetime.strptime(min_time, "%H:%M")
        max_time = "23:30"
        max_time = datetime.strptime(max_time, "%H:%M")
        movie_time = datetime.strptime(movie_time, "%H:%M")
        if movie_time >= min_time and movie_time <= max_time:
            return movie_time
    except ValueError:
        print("Niste uneli ispravno vreme. Unesite ponovo.")
        return False


def check_days(days):
    if len(days) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    days_list = [day.strip().lower() for day in days.split(',')]
    for day in days_list:
        if day not in days_of_week:
            print("Niste uneli ispravne dane. Unesite ponovo.")
            return False
    return True


def check_movie_screening(movie):
    if len(movie) < 1:
        print("Polje nije popujeno. Unesite ponovo.")
        return False
    for index in dict_of_movies.keys():
        if (movie == index) and (dict_of_movies[index]['active'] == 'True'):
            return True
    print("Ovaj film se ne nalazi u bazi. Unesite ponovo.")
    return False


def check_ticket_cost(ticket_cost):
    allowed_characters = "0123456789."
    index = ticket_cost.find('.')
    if len(ticket_cost) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if not all(char in allowed_characters for char in ticket_cost):
        print("Uneli ste neispravnu vrednost cene karte. Unesite ponovo.")
        return False
    if ticket_cost[0] == '0':
        print("Cena ne sme počinjati nulom. Unesite ponovo.")
        return False
    if index == -1:
        print("Uneli ste neispravnu vrednost cene karte. Unesite ponovo.")
        return False
    if ticket_cost[index] != ticket_cost[-3]:
        print("Uneli ste neispravnu vrednost cene karte. Unesite ponovo.")
        return False
    return True


def check_cinema_screening(auditorium, time_beginning, time_ending, days, movie):
    days_list = [day.strip().lower() for day in days.split(',')]
    time_start = datetime.strptime(time_beginning, "%H:%M")
    time_end = datetime.strptime(time_ending, "%H:%M")
    time_duration = (time_end - time_start).total_seconds() / 60

    for movie_info in dict_of_movies.values():
        if movie_info['name'] == movie and int(movie_info['duration']) > time_duration:
            print("Trajanje projekcije kraće je od trajanja filma. Unesite ponovo.")
            return False
        
    for screening_passcode, cinema_screening_info in dict_of_cinema_screenings.items():
        if cinema_screening_info['active'] == 'True':
            continue
        if (
            cinema_screening_info['auditorium'] != auditorium or
            cinema_screening_info['time_beginning'] != time_beginning or
            cinema_screening_info['time_ending'] != time_ending or
            cinema_screening_info['days'] != days or
            cinema_screening_info['movie'] != movie
        ):
            continue
        for date_of_screening_passcode, screening_date_info in dict_of_date_of_screenings.items():
            if screening_passcode not in date_of_screening_passcode:
                continue
            if screening_date_info['active'] == 'True':
                print(f"Ne možete uneti projekciju sa ovim osobinama dok se ne završe termini projekcije {screening_passcode}, koja ima iste ove osobine.")
                return False

    for cinema_screening_info in dict_of_cinema_screenings.values():
        if cinema_screening_info['auditorium'] == auditorium and cinema_screening_info['active'] == 'True':
            for day in days_list:
                if day in cinema_screening_info['days']:
                    screening_start = datetime.strptime(cinema_screening_info['time_beginning'], "%H:%M")
                    screening_end = datetime.strptime(cinema_screening_info['time_ending'], "%H:%M")

                    if (
                        (screening_start <= time_start <= screening_end) or
                        (screening_start <= time_end <= screening_end) or
                        (time_start <= screening_start <= time_end) or
                        (time_start <= screening_end <= time_end)
                    ):
                        print("Vreme projekcije se poklapa sa drugom projekcijom. Unesite ponovo.")
                        return False

    return True


def check_date_of_screening():
    global dict_of_date_of_screenings

    for date_of_screenings_dict in dict_of_date_of_screenings.values():
        date_str = date_of_screenings_dict['date']
        date = datetime.strptime(date_str, "%d.%m.%Y").date()
        if date < date.today():
            date_of_screenings_dict['active'] = 'False'


def check_ticket_row(row, auditorium):
    if len(row) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if not row.isdigit():
        print("Niste uneli ispravan red. Unesite ponovo.")
        return False
    if int(row) > int(dict_of_auditoriums[auditorium]['number_of_rows']):
        print("Niste uneli ispravan red. Unesite ponovo.")
        return False
    return True


def check_ticket_seat(seat, auditorium):
    if len(seat) < 1:
        print("Polje nije popunjeno. Unesite ponovo.")
        return False
    if not seat.isalpha():
        print("Uneli ste neispravno sedište. Unesite ponovo.")
        return False
    if seat not in dict_of_auditoriums[auditorium]['seats']:
        print("Uneli ste neispravno sedište. Unesite ponovo.")
        return False
    return True


def check_selling_date(date_of_screening, date):
    date_str = datetime.strptime(date_of_screening['date'], "%d.%m.%Y").date()
    date = datetime.strptime(date, "%d.%m.%Y").date()
    if date > date_str:
        return False
    return True


def check_valid_date(date):
    try:
        datetime.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        print("Niste uneli ispravan datum.")
        return False


if __name__ == '__main__':
   pass