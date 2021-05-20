from datetime import date

from django.test import TestCase

from courses.models import Course
from teachers.models import Teacher


class CourseTestCase(TestCase):

    def setUp(self) -> None:
        teacher = Teacher.objects.create(first_name='Вася', last_name="Пупкин", email='pupkin@mail.com',
                                         phone='+380971234567', date_of_birth=date(1970, 1, 1))
        Course.objects.create(name='Python',
                              description="Python can be easy to pick up whether you're a first time programmer "
                                          "or you're experienced with other languages.",
                              teacher=teacher,
                              start=date(2021, 9, 1),
                              end=date(2022, 9, 1))

    def test_course_exists(self):
        course = Course.objects.first()
        self.assertEqual(course.name, 'Python')
        self.assertEqual(course.description, "Python can be easy to pick up whether you're a first time programmer "
                                             "or you're experienced with other languages.")
        self.assertEqual(course.teacher, Teacher.objects.first())
        self.assertEqual(course.start, date(2021, 9, 1))
        self.assertEqual(course.end, date(2022, 9, 1))