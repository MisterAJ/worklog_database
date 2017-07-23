#!/usr/bin/env python3

from model import task
from peewee import *
from collections import OrderedDict
import datetime

Task = task.Task


def menuloop():
    """Function for the menu loop"""
    toggle = None
    while toggle != 'q':
        print('')
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        toggle = input('\nMake a selection (q to save and quit): ') \
            .lower().strip()
        if toggle == 'a':
            employee = input('\nEmployee Name\n>>> ')
            name = input('\nName\n>>> ')
            time = input('Time Taken (min)\n>>> ')
            notes = input('Notes\n>>> ')
            add_entry(employee, name, time, notes)
        if toggle == 'v':
            view_entries()
        if toggle == 's':
            search_loop()


def add_entry(employee, name, time, notes):
    """Add an Entry"""
    try:
        Task.create(employee=employee, name=name, time=time, notes=notes,
                    date=datetime.datetime.now().strftime('%m/%d/%Y'))
    except IntegrityError:
        print("This Task already exists")
    except ValueError:
        print('Invalid input - Security Bots have been initialized')


def view_entries(date_query=None, time_query=None,
                 employee_query=None, term_query=None):
    """View Entries"""
    entries = Task.select().order_by(Task.date.desc())
    if date_query:
        entries = entries.where(Task.date.contains(date_query))

    if time_query:
        entries = entries.where(Task.time == time_query)

    if employee_query:
        entries = entries.where(Task.employee.contains(employee_query))

    if term_query:
        entries = entries.where(Task.name.contains(term_query)
                                | Task.notes.contains(term_query))

    for entry in entries:
        entry.print()
        print("N) next entry\nq) return to main menu")

        next_action = input("Action: [Nq] ").lower().strip()

        if next_action == "q":
            print("\nReturning to main menu\n")
            break


def by_date(search_string):
    """Search by Date"""
    view_entries(date_query=search_string)


def by_time(search_string):
    """Search by Time"""
    view_entries(time_query=search_string)


def by_employee(search_string):
    """Search by Employee"""
    view_entries(employee_query=search_string)


def by_term(search_string):
    """Search by Name or Notes"""
    view_entries(term_query=search_string)


def search_loop():
    """Search for tasks"""
    toggle = None
    while toggle != 'b':
        for key, value in search_menu.items():
            print('{}) {}'.format(key, value.__doc__))
        toggle = input('\nMake a selection '
                       '(b to return to the main menu): ').lower().strip()
        if toggle == 'd':
            by_date(input('Please enter a date - MM/DD/YYYY '))
        if toggle == 't':
            by_time(input('Please enter number of minutes '))
        if toggle == 'e':
            by_employee(input('Please enter exact phrase to search by '))
        if toggle == 'p':
            by_term(input('Please enter a search term '))

search_menu = OrderedDict([
    ('d', by_date), ('t', by_time), ('e', by_employee), ('p', by_term)
])

menu = OrderedDict([
    ('a', add_entry), ('v', view_entries), ('s', search_loop)
])

if __name__ == '__main__':
    task.initialize()
    menuloop()
