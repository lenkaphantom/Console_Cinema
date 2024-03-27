from globalne_promenljive import *
from funkcije_provere import *


def load_from_file(filename='filmovi.txt'):
    with open(filename, 'r', encoding="utf-8") as filmovi:
        for line in filmovi:
            movie = line.strip().split(" | ")
            if len(movie) == 10:
                index, name, genre, duration, director, main_roles, country, year, summary, active = movie
                movie_dict = {
                    "name": name,
                    "genre": genre,
                    "duration": duration,
                    "director": director,
                    "main_roles": main_roles,
                    "country": country,
                    "year": year,
                    "summary": summary,
                    "active": active
                }
                dict_of_movies[index] = movie_dict
    
    with open("filmovi_imena.txt", 'r', encoding="utf-8") as names:
        for line in names:
            names_list = line.strip().split(" | ")
            if len(names_list) == 2:
                index, name = names_list
                dict_of_movie_names[index] = name

    with open("zanrovi.txt", 'r', encoding="utf-8") as genres:
        for line in genres:
            genre_list = line.strip().split(" | ")
            if len(genre_list) == 2:
                index, genre = genre_list
                dict_of_genres[index] = genre
    
    with open("drzave.txt", 'r', encoding="utf-8") as countries:
        for line in countries:
            country_list = line.strip().split(" | ")
            if len(country_list) == 2:
                index, country = country_list
                dict_of_countries[index] = country

    with open("reziseri.txt", 'r', encoding="utf-8") as directors:
        for line in directors:
            director_list = line.strip().split(" | ")
            if len(director_list) == 2:
                index, director = director_list
                dict_of_directors[index] = director

    with open("glumci.txt", 'r', encoding="utf-8") as actors:
        for line in actors:
            actor_list = line.strip().split(" | ")
            if len(actor_list) == 2:
                index, actor = actor_list
                dict_of_actors[index] = actor


def write_to_file(filename='filmovi.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for index, movie in dict_of_movies.items():
            line = f"{index} | {movie['name']} | {movie['genre']} | {movie['duration']} | {movie['director']} | {movie['main_roles']} | {movie['country']} | {movie['year']} | {movie['summary']} | {movie['active']}\n"
            file.write(line)

    with open("filmovi_imena.txt", 'w', encoding="utf-8") as file:
        for index, name in dict_of_movie_names.items():
            line = f"{index} | {name}\n"
            file.write(line)

    with open("zanrovi.txt", 'w', encoding="utf-8") as file:
        for index, genre in dict_of_genres.items():
            line = f"{index} | {genre}\n"
            file.write(line)

    with open("drzave.txt", 'w', encoding="utf-8") as file:
        for index, country in dict_of_countries.items():
            line = f"{index} | {country}\n"
            file.write(line)

    with open("reziseri.txt", 'w', encoding="utf-8") as file:
        for index, director in dict_of_directors.items():
            line = f"{index} | {director}\n"
            file.write(line)

    with open("glumci.txt", 'w', encoding="utf-8") as file:
        for index, actor in dict_of_actors.items():
            line = f"{index} | {actor}\n"
            file.write(line)


def search_name(index_name, movies_dict = dict_of_movies):
    search_dict_movies = {}

    for index, movie in movies_dict.items():
        if dict_of_movie_names[index_name].lower() == movie['name'].lower():
            search_dict_movies[index] = movie

    return search_dict_movies


def search_genre(index_genre, movies_dict = dict_of_movies):
    search_dict_movies = {}
    genres = []

    index_list = [index.strip() for index in index_genre.split(',')]
    for index in index_list:
        if index not in dict_of_genres.keys():
            return 'False'
        genres.append(dict_of_genres[index])

    for index, movie in movies_dict.items():
        if ', ' in movie['genre']:
            genres_lower = [genre.lower() for genre in movie['genre'].split(', ')]
        else:
            genres_lower = [genre.lower() for genre in movie['genre'].split(',')]
        if all(genre.lower() in genres_lower for genre in genres):
            search_dict_movies[index] = movie

    return search_dict_movies


def search_duration_menu(movies_dict):
    while True:
        print("1. Minimalno trajanje")
        print("2. Makximalno trajanje")
        print("3. Trajanje sa navođenjem obeju granica")
        print()
        opcija = input("Unesite opciju koju želite: ")
        if len(opcija) < 1:
            print("Polje nije popunjeno. Unesite ponovo.")
            print()
            continue
        if opcija == '-1':
            return opcija
        elif opcija == '1':
            min_duration = input("Unesite minimalno trajanje filma: ")
            if len(min_duration) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if min_duration == '-1':
                print()
                return '-1'
            return search_min_duration(min_duration, movies_dict)
        elif opcija == '2':
            max_duration = input("Unesite maximalno trajanje filma: ")
            if len(max_duration) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if max_duration == '-1':
                print()
                return '-1'
            return search_max_duration(max_duration, movies_dict)
        elif opcija == '3':
            min_duration = input("Unesite donju granicu trajanja filma: ")
            if min_duration == '-1':
                print()
                return '-1'
            max_duration = input("Unesite gornju granicu trajanja filma: ")
            if max_duration == '-1':
                print()
                return '-1'
            if len(min_duration) < 1 or len(max_duration) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if max_duration > min_duration:
                print("Uneli ste neispravne granice trajanja. Unesite ponovo.")
                print()
                continue
            return search_duration(min_duration, max_duration, movies_dict)
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            continue


def search_min_duration(min_duration, movies_dict = dict_of_movies):
    search_dict_movies = {}
    try:
        for index, movie in movies_dict.items():
            duration = int(movie['duration'])
            if duration >= int(min_duration):
                search_dict_movies[index] = movie

        return search_dict_movies
    except TypeError:
        print("Uneli ste neispravno trajanje filma. Unesite ponovo.")
        return None


def search_max_duration(max_duration, movies_dict = dict_of_movies):
    search_dict_movies = {}
    try:
        for index, movie in movies_dict.items():
            duration = int(movie['duration'])
            if duration <= int(max_duration):
                search_dict_movies[index] = movie

        return search_dict_movies
    except TypeError:
        print("Uneli ste neispravno trajanje filma. Unesite ponovo.")
        return None


def search_duration(min_duration, max_duration, movies_dict = dict_of_movies):
    search_dict_movies = {}
    try:
        if int(min_duration) > int(max_duration):
            print("Unesene su neispravne vrednosti granica trajanja filma.")
            return None

        for index, movie in movies_dict.items():
            duration = int(movie['duration'])
            if duration >= int(min_duration) and duration <= int(max_duration):
                search_dict_movies[index] = movie

        return search_dict_movies
    except TypeError:
        print("Uneli ste neispravno trajanje filma. Unesite ponovo.")
        return None


def search_director(index_directors, movies_dict = dict_of_movies):
    search_dict_movies = {}
    directors = []

    index_list = [index.strip() for index in index_directors.split(',')]
    for index in index_list:
        if index not in dict_of_directors.keys():
            return 'False'
        directors.append(dict_of_directors[index])

    for index, movie in movies_dict.items():
        if ', ' in movie['director']:
            directors_lower = [director.lower() for director in movie['director'].split(', ')]
        else:
            directors_lower = [director.lower() for director in movie['director'].split(',')]
        if all(director.lower() in directors_lower for director in directors):
                search_dict_movies[index] = movie

    return search_dict_movies


def search_main_roles(index_main_roles, movies_dict=dict_of_movies):
    search_dict_movies = {}
    main_roles = []

    index_list = [index.strip() for index in index_main_roles.split(',')]
    for index in index_list:
        if index not in dict_of_actors.keys():
            return 'False'
        main_roles.append(dict_of_actors[index])

    for index, movie in movies_dict.items():
        if ', ' in movie['main_roles']:
            roles_lower = [role.lower() for role in movie['main_roles'].split(', ')]
        else:
            roles_lower = [role.lower() for role in movie['main_roles'].split(',')]
        if all(main_role.lower() in roles_lower for main_role in main_roles):
            search_dict_movies[index] = movie

    return search_dict_movies


def search_country(index_country, movies_dict = dict_of_movies):
    search_dict_movies = {}
    countries = []

    index_list = [index.strip() for index in index_country.split(',')]
    for index in index_list:
        if index not in dict_of_countries.keys():
            return 'False'
        countries.append(dict_of_countries[index])
    
    for index, movie in movies_dict.items():
        if ', ' in movie['country']:
            countries_lower = [country.lower() for country in movie['country'].split(', ')]
        else:
            countries_lower = [country.lower() for country in movie['country'].split(',')]
        if all(country.lower() in countries_lower for country in countries):
            search_dict_movies[index] = movie

    return search_dict_movies


def search_year(year, movies_dict = dict_of_movies):
    search_dict_movies = {}
    
    for index, movie in movies_dict.items():
        if year == movie['year']:
            search_dict_movies[index] = movie

    return search_dict_movies


def search_movies():
    movies_dict = dict_of_movies

    while True:
        print("Kriterijumi za pretragu: ")
        print("1: Pretraga po imenu.")
        print("2: Pretraga po žanrovima.")
        print("3: Pretraga po trajanju.")
        print("4: Pretraga po režiserima.")
        print("5: Pretraga po glavnim ulogama.")
        print("6: Pretraga po zemljama porekla.")
        print("7: Pretraga po godini izdavanja.")
        print()

        opcija = input("Unesite po kom kriterijumu želite da pretražite filmove: ")
        if opcija == '-1':
            print()
            return
        elif opcija == '1':
            print_movie(dict_of_movie_names)
            index = input("Unesite indeks ispred imena filma: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            if index not in dict_of_movie_names.keys():
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
            movies = search_name(index)
            if movies == {}:
                print("Ne postoji film koji zadovoljava ove kriterijume. Unesite ponovo.")
                print()
                continue
            print_movies(movies)
            print_movies_more(movies)
            return
        elif opcija == '2':
            print_movie(dict_of_genres)
            index = input("Unesite indekse ispred žanrova filma: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            movies = search_genre(index)
            if movies == {}:
                print("Ne postoji film koji zadovoljava ove kriterijume. Unesite ponovo.")
                print()
                continue
            if movies == 'False':
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
            print_movies(movies)
            print_movies_more(movies)
            return
        elif opcija == '3':
            movies = search_duration_menu(movies_dict)
            if movies == {}:
                print("Ne postoji film koji zadovoljava ove kriterijume. Unesite ponovo.")
                print()
                continue
            if movies == '-1':
                print()
                return
            print_movies(movies)
            print_movies_more(movies)
            return
        elif opcija == '4':
            print_movie(dict_of_directors)
            index = input("Unesite indeks ispred režisera: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            movies = search_director(index)
            if movies == {}:
                print("Ne postoji film koji zadovoljava ove kriterijume. Unesite ponovo.")
                print()
                continue
            if movies == 'False':
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
            print_movies(movies)
            print_movies_more(movies)
            return
        elif opcija == '5':
            print_movie(dict_of_actors)
            index = input("Unesite indekse ispred glavnih uloga odvajajući ih zarezom: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            movies = search_main_roles(index)
            if movies == {}:
                print("Ne postoji film koji zadovoljava ove kriterijume. Unesite ponovo.")
                print()
                continue
            if movies == 'False':
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
            print_movies(movies)
            print_movies_more(movies)
            return
        elif opcija == '6':
            print_movie(dict_of_countries)
            index = input("Unesite indekse ispred zemalja: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            movies = search_country(index)
            if movies == {}:
                print("Ne postoji film koji zadovoljava ove kriterijume. Unesite ponovo.")
                print()
                continue
            if movies == 'False':
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
            print_movies(movies)
            print_movies_more(movies)
            return
        elif opcija == '7':
            year = input("Unesite godinu: ")
            if len(year) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if year == '-1':
                print()
                return
            movies = search_year(year)
            if movies == {}:
                print("Ne postoji film koji zadovoljava ove kriterijume. Unesite ponovo.")
                print()
                continue
            print_movies(movies)
            print_movies_more(movies)
            return
        else:
            print("Niste uneli ispravnu opciju. Unesite ponovo.")
            continue


def multicriteria_search_movies():
    movies_dict = dict_of_movies
    while True:
        print("Kriterijumi za pretragu: ")
        print("1: Pretraga po imenu.")
        print("2: Pretraga po žanrovima.")
        print("3: Pretraga po trajanju.")
        print("4: Pretraga po režiserima.")
        print("5: Pretraga po glavnim ulogama.")
        print("6: Pretraga po zemljama porekla.")
        print("7: Pretraga po godini izdavanja.")
        print()

        allowed_characters = "1234567 ,"
        opcija = input("Unesite po kojim kriterijumima želite da pretražite filmove: ")
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
            print_movie(dict_of_movie_names)
            index = input("Unesite indeks ispred imena filma: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            if index not in dict_of_movie_names.keys():
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
            movies_dict = search_name(index, movies_dict)
        if '2' in opcija:
            print_movie(dict_of_genres)
            index = input("Unesite indekse ispred žanrova filma: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            movies_dict = search_genre(index, movies_dict)
            if movies_dict == 'False':
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
        if '3' in opcija:
            movies_dict = search_duration_menu(movies_dict)
            if movies_dict == '-1':
                print()
                return
        if '4' in opcija:
            print_movie(dict_of_directors)
            index = input("Unesite indeks ispred režisera: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            movies_dict = search_director(index, movies_dict)
            if movies_dict == 'False':
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
        if '5' in opcija:
            print_movie(dict_of_actors)
            index = input("Unesite indekse ispred glavnih uloga odvajajući ih zarezom: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            movies_dict = search_main_roles(index, movies_dict)
            if movies_dict == 'False':
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
        if '6' in opcija:
            print_movie(dict_of_countries)
            index = input("Unesite indeks ispred zemlje: ")
            if len(index) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if index == '-1':
                print()
                return
            movies_dict = search_country(index, movies_dict)
            if movies_dict == 'False':
                print("Uneli ste nepostojeći indeks. Unesite ponovo.")
                print()
                continue
        if '7' in opcija:
            year = input("Unesite godinu: ")
            if len(year) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if year == '-1':
                print()
                return
            movies_dict = search_year(year, movies_dict)

        if movies_dict == {}:
            print("Ne postoji film koji zadovoljava ove kriterijume. Unesite ponovo.")
            print()
            continue

        print_movies(movies_dict)
        print_movies_more(movies_dict)
        return
    

def print_movie(movie_dict):
    print()
    print(f"{'-' * 105}")
    for key, value in movie_dict.items():
        if key != 'active':
            print(f"{key}: {value}")
    print(f"{'-' * 105}")
    print()


def print_movies(movies_dict = dict_of_movies):
    print(f"+{'-' * 5}+{'-' * 50}+{'-' * 25}+{'-' * 25}+{'-' * 10}+")
    print(f"|{'Index':<5}|{'Name':<50}|{'Genre':<25}|{'Director':<25}|{'Duration':<10}|")
    print(f"+{'-' * 5}+{'-' * 50}+{'-' * 25}+{'-' * 25}+{'-' * 10}+")

    for index, movie in movies_dict.items():
        if movie['active'] == 'True':
            print(f"|{index:<5}|{movie['name'][:50]:<50}|{movie['genre']:<25}|{movie['director'][:25]:<25}|{movie['duration']:<10}|")

    print(f"+{'-' * 5}+{'-' * 50}+{'-' * 25}+{'-' * 25}+{'-' * 10}+")
    print()


def print_movies_more(movies_dict = dict_of_movies):
    while True:
        opcija = input("Ako želite da vidite više o filmu, unesite redni broj filma, u suprotnom unesite -1: ")
        if opcija == '-1':
            print()
            return
        if opcija not in movies_dict.keys():
            print("Uneli ste neispravnu opciju. Unesite ponovo.")
            print()
            continue
        for index in movies_dict.keys():
            if (opcija == index):
                if movies_dict[opcija]['active'] == 'True':
                    print_movie(movies_dict[index])
                    return
                else:
                    print("Film nije dostupan.")
                    print()
                    return


def add_movie():
    global dict_of_movies

    while True:
        movies_index = list(dict_of_movies.keys())
        index = int(movies_index[-1]) + 1

        name = input("Unesite ime filma: ")
        if name == '-1':
            print()
            return
        if not check_movie_name(name):
            print()
            continue

        genre = input("Unesite žanr filma: ")
        if genre == '-1':
            print()
            return
        if not check_genre(genre):
            print()
            continue

        duration = input("Unesite trajanje filma: ")
        if duration == '-1':
            print()
            return
        if not check_duration(duration):
            print()
            continue

        director = input("Unesite režisere odvajajući ih zarezom: ")
        if director == '-1':
            print()
            return
        if not check_names(director):
            print()
            continue

        main_roles = input("Unesite glavne uloge u filmu odvajajući ih zarezom: ")
        if main_roles == '-1':
            print()
            return
        if not check_names(main_roles):
            print()
            continue

        country = input("Unesite zemlje porekla odvajajući ih zarezom: ")
        if country == '-1':
            print()
            return
        if not check_names(country):
            print()
            continue

        year = input("Unesite godinu izdavanja: ")
        if year == '-1':
            print()
            return
        if not check_year(year):
            print()
            continue
        
        summary = input("Unesite kratak rezime filma: ")
        if summary == '-1':
            print()
            return
        if not check_summary(summary):
            print()
            continue

        active = 'True'

        movie_dict = {
            "name": name,
            "genre": genre,
            "duration": duration,
            "director": director,
            "main_roles": main_roles,
            "country": country,
            "year": year,
            "summary": summary,
            "active": active
        }

        dict_of_movies[index] = movie_dict

        print()
        print(f"Film '{name}' je dodat uspešno.")
        print()

        add_movie_name()
        add_actor()
        add_country()
        add_director()
        add_genre()

        return
    

def add_movie_name(movies_dict = dict_of_movies):
    global dict_of_movie_names

    for movie in movies_dict.values():
        movie_name = movie['name']
        if movie_name not in dict_of_movie_names.values() and movie['active'] == 'True':
            names_index = list(dict_of_movie_names.keys())
            index = int(names_index[-1]) + 1
            dict_of_movie_names[index] = movie_name

def add_genre(movies_dict = dict_of_movies):
    global dict_of_genres

    for movie in movies_dict.values():
        genre_list = movie['genre'].split(', ')
        for genre in genre_list:
            if genre not in dict_of_genres.values() and (movie['active'] == 'True'):
                genre_index = list(dict_of_genres.keys())
                index = int(genre_index[-1]) + 1
                dict_of_genres[index] = genre


def add_country(movies_dict = dict_of_movies):
    global dict_of_countries

    for movie in movies_dict.values():
        countries_list = movie['country'].split(', ')
        for country in countries_list:
            if country not in dict_of_countries.values() and movie['active'] == 'True':
                country_index = list(dict_of_countries.keys())
                index = int(country_index[-1]) + 1
                dict_of_countries[index] = movie['country']


def add_director(movies_dict = dict_of_movies):
    global dict_of_directors

    for movie in movies_dict.values():
        director_list = movie['director'].split(', ')
        for director in director_list:
            if director not in dict_of_directors.values() and movie['active'] == 'True':
                director_index = list(dict_of_directors.keys())
                index = int(director_index[-1]) + 1
                dict_of_directors[index] = director


def add_actor(movies_dict = dict_of_movies):
    global dict_of_actors

    for movie in movies_dict.values():
        actor_list = movie['main_roles'].split(', ')
        for actor in actor_list:
            if actor not in dict_of_actors.values() and movie['active'] == 'True':
                actor_index = list(dict_of_actors.keys())
                index = int(actor_index[-1]) + 1
                dict_of_actors[index] = actor
    

def print_index(opcija, movie_dict = dict_of_movies):
    for index, movie_info in movie_dict.items():
        if movie_info['active'] == 'True':
            print(f"{index}: {movie_info['name']}")
    if opcija == '-1':
        return opcija
    elif opcija == '8':
        index = input("Unesite indeks filma koji želite da obrišete: ")
        if index in movie_dict.keys():
            print()
            return index
    elif opcija == '10':
        index = input("Unesite indeks filma koji želite da izmenite: ")
        if index in movie_dict.keys():
            print()
            return index
    print("Uneli ste neispravnu opciju. Unesite ponovo.")
    return None
 

def change_movie(index):
    name = dict_of_movies[index]['name']
    genre = dict_of_movies[index]['genre']
    duration = dict_of_movies[index]['duration']
    director = dict_of_movies[index]['director']
    main_roles = dict_of_movies[index]['main_roles']
    country = dict_of_movies[index]['country']
    year = dict_of_movies[index]['year']
    summary = dict_of_movies[index]['summary']

    while True:
        print("Odaberite podatke o filmu koje želite da izmenite: ")
        print("1: Naziv filma.")
        print("2: Žanr filma.")
        print("3: Trajanje filma.")
        print("4: Režiser(i) filma.")
        print("5: Glavne uloge u filmu.")
        print("6: Zemlja porekla filma.")
        print("7: Godina izdavanja.")
        print("8: Kratak rezime filma.")
        print()

        allowed_characters = "12345678 ,"
        opcija = input("Unesite broj ispred podatka koji želite da izmenite: ")
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
            name = input("Unesite novo ime filma: ")
            if name == '-1':
                print()
                return
            if not check_movie_name(name):
                print()
                continue
            if name == dict_of_movies[index]['name']:
                print("Ne možete da unesete staro ime filma. Unesite ponovo.")
                print()
                continue
        if '2' in opcija:
            genre = input("Unesite novi žanr filma: ")
            if genre == '-1':
                print()
                return
            if not check_genre(genre):
                print()
                continue
            if genre == dict_of_movies[index]['genre']:
                print("Ne možete da unesete stari žanr filma. Unesite ponovo.")
                print()
                continue
        if '3' in opcija:
            duration = input("Unesite novo vreme trajanje filma: ")
            if genre == '-1':
                print()
                return
            if not check_duration(duration):
                print()
                continue
            if duration == dict_of_movies[index]['duration']:
                print("Ne možete da unesete staro vreme trajanja filma. Unesite ponovo.")
                print()
                continue
        if '4' in opcija:
            director = input("Unesite nove režisere: ")
            if director == '-1':
                print()
                return
            if not check_names(director):
                print()
                continue
            if director == dict_of_movies[index]['director']:
                print("Ne možete da unesete stare režisere. Unesite ponovo.")
                print()
                continue
        if '5' in opcija:
            main_roles = input("Unesite nove glavne uloge: ")
            if main_roles == '-1':
                print()
                return
            if not check_names(main_roles):
                print()
                continue
            if main_roles == dict_of_movies[index]['main_roles']:
                print("Ne možete da unesete stare glavne uloge. Unesite ponovo.")
                print()
                continue
        if '6' in opcija:
            country = input("Unesite nove zemlje porekla filma: ")
            if country == '-1':
                print()
                return
            if not check_names(country):
                print()
                continue
            if country == dict_of_movies[index]['country']:
                print("Ne možete da unesete stare zemlje porekla filma. Unesite ponovo.")
                print()
                continue
        if '7' in opcija:
            year = input("Unesite novu godinu izdavanja filma: ")
            if year == '-1':
                print()
                return
            if not check_year(year):
                print()
                continue
            if year == dict_of_movies[index]['year']:
                print("Ne možete da unesete staru godinu izdavanja filma. Unesite ponovo.")
                print()
                continue
        if '8' in opcija:
            summary = input("Unesite novi kratki rezime filma: ")
            if summary == '-1':
                print()
                return
            if len(summary) < 1:
                print("Polje nije popunjeno. Unesite ponovo.")
                print()
                continue
            if summary == dict_of_movies[index]['summary']:
                print("Ne možete da unesete stari kratki rezime filma. Unesite ponovo.")
                print()
                continue

        dict_of_movies[index]['name'] = name
        dict_of_movies[index]['genre'] = genre
        dict_of_movies[index]['duration'] = duration
        dict_of_movies[index]['director'] = director
        dict_of_movies[index]['main_roles'] = main_roles
        dict_of_movies[index]['country'] = country
        dict_of_movies[index]['year'] = year
        dict_of_movies[index]['summary'] = summary

        add_movie_name()
        add_actor()
        add_country()
        add_director()
        add_genre()

        print()
        print(f"Uspešno ste izmenili odabrane podakte filma {index}.{name}.")
        return
    

def delete_movie_name(movie_dict):
    for index, name in dict_of_movie_names.items():
        if name == movie_dict['name']:
            del dict_of_movie_names[index]
            return


def delete_genre(movie_dict):
    genre_list = movie_dict['genre'].split(', ')
    for genre in genre_list:
        for index, genre_ in dict_of_genres.items():
            if genre ==genre_:
                del dict_of_genres[index]
                break
    return


def delete_actor(movie_dict):
    main_roles_list = movie_dict['main_roles'].split(', ')
    for main_role in main_roles_list:
        for index, actor in dict_of_actors.items():
            if actor == main_role:
                del dict_of_actors[index]
                break
    return


def delete_country(movie_dict):
    countries_list = movie_dict['country'].split(', ')
    for country in countries_list:
        for index, country_ in dict_of_countries.items():
            if country == country_:
                del dict_of_countries[index]
                break
    return


def delete_director(movie_dict):
    directors_list = movie_dict['director'].split(', ')
    for director in directors_list:
        for index, director_ in dict_of_directors.items():
            if director == director_:
                del dict_of_directors[index]
                break
    return 


def delete_movie(movie_dict):
    movie_dict['active'] = 'False'
    print(f"Film {movie_dict['name']} je uspešno obrisan.")
    print()

    delete_movie_name(movie_dict)
    delete_genre(movie_dict)
    delete_actor(movie_dict)
    delete_country(movie_dict)
    delete_director(movie_dict)

    add_movie_name()
    add_actor()
    add_genre()
    add_country()
    add_director()
    return

if __name__ == '__main__':
    load_from_file()
    #delete_movie(dict_of_movies['10'])
    add_movie_name()
    add_actor()
    add_genre()
    add_country()
    add_director()
    #print(search_director('2, 3'))
    write_to_file()