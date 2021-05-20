from datetime import date

from django.test import TestCase

from courses.models import Course
from students.models import Student
from teachers.models import Teacher


class StudentTestCase(TestCase):

    def setUp(self) -> None:
        teacher = Teacher.objects.create(first_name='Вася', last_name="Пупкин", email='pupkin@mail.com',
                                         phone='+380971234567', date_of_birth=date(1970, 1, 1))

        course1 = Course.objects.create(name='Python',
                                        description="Python can be easy to pick up whether you're a first time "
                                                    "programmer or you're experienced with other languages.",
                                        teacher=teacher,
                                        start=date(2021, 9, 1),
                                        end=date(2022, 9, 1))
        student = Student.objects.create(first_name='Маша', last_name='Ефросинина', email='masha@mail.com',
                                         phone='+380997654321',date_of_birth=date(1986, 1, 1))
        student.courses.add(course1)

    def test_student_exists(self):
        student = Student.objects.first()
        self.assertEqual(student.first_name, 'Маша')
