from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import User, Certificate, Internship, Role, Skill
import uuid


class CertificateViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        self.role = Role.objects.create(name='Tester')
        self.internship = Internship.objects.create(
            name='Test Internship',
            start_date='2023-01-01',
            end_date='2023-01-31'
        )
        self.skill = Skill.objects.create(name='Python')

        # Сертификат с навыком
        self.cert_with_skill = Certificate.objects.create(
            user=self.user,
            internship=self.internship,
            role=self.role
        )
        self.cert_with_skill.skills.add(self.skill)

        # Сертификат без навыков
        self.cert_without_skill = Certificate.objects.create(
            user=self.user,
            internship=self.internship,
            role=self.role
        )

    def test_get_certificate_detail(self):
        url = reverse('certificate-detail', kwargs={'certificate_id': self.cert_with_skill.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.cert_with_skill.id))
        self.assertEqual(response.data['user']['email'], 'test@example.com')
        self.assertEqual(len(response.data['skills']), 1)

    def test_get_nonexistent_certificate(self):
        fake_uuid = uuid.uuid4()
        url = reverse('certificate-detail', kwargs={'certificate_id': fake_uuid})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CertificateListViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(
            first_name='User1',
            last_name='Test',
            email='user1@example.com'
        )
        self.user2 = User.objects.create(
            first_name='User2',
            last_name='Test',
            email='user2@example.com'
        )
        self.role = Role.objects.create(name='Developer')
        self.internship = Internship.objects.create(
            name='Internship',
            start_date='2023-01-01',
            end_date='2023-02-01'
        )
        self.skill = Skill.objects.create(name='Django')

        # Сертификат с навыком
        self.cert_with_skill = Certificate.objects.create(
            user=self.user1,
            internship=self.internship,
            role=self.role
        )
        self.cert_with_skill.skills.add(self.skill)

        # Сертификат без навыков
        self.cert_without_skill = Certificate.objects.create(
            user=self.user2,
            internship=self.internship,
            role=self.role
        )

    def test_get_certificates_by_email(self):
        url = reverse('certificates-by-email')
        response = self.client.get(url, {'email': 'user1@example.com'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['certificates']), 1)
        self.assertEqual(
            response.data['certificates'][0]['user']['email'],
            'user1@example.com'
        )

    def test_get_certificates_without_skills(self):
        url = reverse('certificates-without-skills')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем что только cert_without_skill возвращается
        self.assertEqual(len(response.data['certificates']), 1)
        self.assertEqual(
            response.data['certificates'][0]['user']['email'],
            'user2@example.com'
        )