from django.test import TestCase
from django.core.exceptions import ValidationError
from certificates.models import User, School, Skill, Role, Internship, Certificate
from datetime import date, timedelta
import uuid


class UserModelTest(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com'
        )

    def test_first_name_label(self):
        field_label = self.user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_email_unique(self):
        # Попытка создать пользователя с таким же email должна вызвать ошибку
        with self.assertRaises(Exception):
            User.objects.create(
                first_name='Jane',
                last_name='Doe',
                email='john@example.com'
            )


class CertificateModelTest(TestCase):
    def setUp(self):
        # Создаем все необходимые объекты
        self.user = User.objects.create(
            first_name='Alice',
            last_name='Smith',
            email='alice@example.com'
        )
        self.role = Role.objects.create(name='Developer')
        self.internship = Internship.objects.create(
            name='Summer 2023',
            start_date=date(2023, 6, 1),
            end_date=date(2023, 8, 31)
        )

        # Создаем сертификат
        self.certificate = Certificate.objects.create(
            user=self.user,
            internship=self.internship,
            role=self.role
        )

    def test_certificate_str(self):
        self.assertEqual(
            str(self.certificate),
            f"Certificate {self.certificate.id} for Alice Smith"
        )

    def test_issued_at_auto_now_add(self):
        self.assertIsNotNone(self.certificate.issued_at)


class InternshipModelTest(TestCase):
    def setUp(self):
        # Создаем тестовую стажировку
        self.start_date = date(2023, 1, 1)
        self.end_date = date(2023, 1, 10)
        self.internship = Internship.objects.create(
            name='Test Internship',
            start_date=self.start_date,
            end_date=self.end_date
        )

    def test_duration_property(self):
        expected_duration = (self.end_date - self.start_date).days
        self.assertEqual(self.internship.duration, expected_duration)