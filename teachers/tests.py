from datetime import date

from django.test import TestCase

from teachers.models import Teacher


class TeacherTestCase(TestCase):

    def setUp(self) -> None:
        Teacher.objects.create(first_name='Вася', last_name="Пупкин", email='pupkin@mail.com',
                               phone='+380971234567', date_of_birth=date(1970, 1, 1))

    def test_vasja_exists(self):
        teacher = Teacher.objects.first()
        self.assertEqual(teacher.first_name, 'Вася')
        self.assertEqual(teacher.last_name, 'Пупкин')
        self.assertEqual(teacher.email, 'pupkin@mail.com')
        self.assertEqual(teacher.phone, '+380971234567')
        self.assertEqual(teacher.date_of_birth, date(1970, 1, 1))

    def test_overload_string(self):
        teacher = Teacher.objects.first()
        self.assertEqual(str(teacher), 'Вася Пупкин')
