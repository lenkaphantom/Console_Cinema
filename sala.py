from globalne_promenljive import *
from funkcije_provere import *

def load_from_file(filename='sala.txt'):
    with open(filename, 'r', encoding="utf-8") as sala:
        for line in sala:
            auditorium = line.strip().split(" | ")
            if len(auditorium) == 4:
                passcode, name, number_of_rows, seats = auditorium
                auditorium_dict = {
                    "passcode": passcode,
                    "name": name,
                    "number_of_rows": number_of_rows,
                    "seats": seats,
                }
                dict_of_auditoriums[passcode] = auditorium_dict


def write_to_file(filename='sala.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for auditorium in dict_of_auditoriums.values():
            file.write(f"{auditorium['passcode']} | {auditorium['name']} | {auditorium['number_of_rows']} | {auditorium['seats']}\n")


def print_seats_rows(seats_dict):
    for row in seats_dict.keys():
        print(f"red {row:<4} |", end=" ")
        seat_list = seats_dict[row]
        for seat in seat_list:
            print(f"{seat:<4}", end="")
        print()
    return


def print_auditorium():
    auditorium_backup = {}
    index = 1
    for passcode in dict_of_auditoriums.keys():
        print(f"{index}: {passcode}")
        auditorium_backup[str(index)] = passcode
        index += 1
    return auditorium_backup


if __name__ == '__main__':
    load_from_file()
    seats_dict = {
        1: ['A', 'B', 'C'],
        2: ['A', 'B', 'C']
    }
    print(print_seats_rows(seats_dict))
    write_to_file()