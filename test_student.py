import unittest
from datetime import date, timedelta
from student import Student
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')
        
    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)
    
    def test_is_exemplary(self):
        print('test_is_exemplary')
        self.student.is_exemplary()
        self.assertTrue(self.student.exemplary_list)

    def test_email(self):
        print('test_email')
        expected_email = "johndoe@email.com"
        self.assertEqual(self.student.email, expected_email)

    def test_apply_extension(self):
        original_end_date = self.student.end_date
        self.student.apply_extension(20)
        expected_end_date = original_end_date + timedelta(20)
        self.assertEqual(self.student.end_date, expected_end_date)

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")
    
    def test_course_schedule_fail(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")

if __name__ == '__main__':
    unittest.main()