import re
import datetime

from peewee import *

db = SqliteDatabase('work_log.db')


class Task(Model):
    """Class for the Task"""
    employee = CharField(max_length=255)
    name = CharField(max_length=255, unique=True)
    date = DateTimeField(default=datetime.datetime.now)
    notes = TextField()
    time = IntegerField(default=0)

    def print(self):
        print('\nEmployee Name   - {}'
              '\nName            - {}'
              '\nTime Taken(min) - {}'
              '\nDate            - {}'
              '\nNotes           - {}\n'
              '\n----------------------------\n'
              .format(self.employee, self.name, self.time,
                      self.date, self.notes))

    def string(self):
        return (self.name + ',' + self.time +
                ',' + self.date + ',' + self.notes
                + '\n')

    class Meta:
        database = db


def initialize():
    """Create the database and table if they don't already exist"""
    db.connect()
    db.create_tables([Task], safe=True)

if __name__ == '__main__':
    pass
