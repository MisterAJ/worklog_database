import unittest
import datetime
from model import task
import worklog


class TaskTests(unittest.TestCase):
    def test_bad_time(self):
        with self.assertRaises(ValueError):
            task.Task.create(employee='employee', name='name',
                             time='string', notes='notes',
                             date=datetime.datetime.now().strftime('%m/%d/%Y'))


class LogTests(unittest.TestCase):

    def test_empty_employee_search(self):
        self.assertFalse(worklog.by_employee('tahoedtnheoutehui'))

    def test_empty_date_search3(self):
        self.assertFalse(worklog.by_date('tahoedtnheoutehui'))

    def test_empty_term_search4(self):
        self.assertFalse(worklog.by_term('tahoedtnheoutehui'))

    def test_empty_time_search2(self):
        self.assertFalse(worklog.by_time(100))

if __name__ == '__main__':
    unittest.main()
