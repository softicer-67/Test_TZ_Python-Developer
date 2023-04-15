from unittest import TestCase
from rest_framework.test import APIClient
import pytest
from rest_framework import status
from app.models import EducationModule
from app.serializers import EducationModuleSerializer


@pytest.mark.django_db
class EducationModuleModelTestCase(TestCase):
    """Тестирование модели Образовательные модули."""

    def setUp(self):
        self.number = 1
        self.name = "Test Module"
        self.description = "This is a test module."
        self.education_module = EducationModule.objects.create(
            number=self.number,
            name=self.name,
            description=self.description
        )

    def test_education_module_model(self):
        education_module = EducationModule.objects.get(id=self.education_module.id)
        self.assertEqual(education_module.number, self.number)
        self.assertEqual(education_module.name, self.name)
        self.assertEqual(education_module.description, self.description)


@pytest.mark.django_db
class EducationModuleSerializerTestCase(TestCase):
    """Тестирование сериализатора Образовательные модули."""

    def setUp(self):
        self.number = 1
        self.name = "Test Module"
        self.description = "This is a test module."
        self.education_module_data = {
            'number': self.number,
            'name': self.name,
            'description': self.description
        }
        self.education_module = EducationModule.objects.create(
            number=self.number,
            name=self.name,
            description=self.description
        )
        self.serializer = EducationModuleSerializer(instance=self.education_module)

    def test_education_module_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['number'], self.number)
        self.assertEqual(data['name'], self.name)
        self.assertEqual(data['description'], self.description)


@pytest.mark.django_db
class EducationModuleViewTestCase(TestCase):
    """Тестирование вида CRUD для Образовательных модулей."""

    def setUp(self):
        self.client = APIClient()
        self.number = 1
        self.name = "Test Module"
        self.description = "This is a test module."
        self.education_module = EducationModule.objects.create(
            number=self.number,
            name=self.name,
            description=self.description
        )
        self.valid_payload = {
            'number': 2,
            'name': 'New Module',
            'description': 'This is a new module.'
        }
        self.invalid_payload = {
            'number': '',
            'name': '',
            'description': ''
        }

    def test_get_all_education_modules(self):
        response = self.client.get('/education_modules/')
        education_modules = EducationModule.objects.all()
        serializer = EducationModuleSerializer(education_modules, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_education_module(self):
        response = self.client.post('/education_modules/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_education_module(self):
        response = self.client.post('/education_modules/', self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_valid_single_education_module(self):
        response = self.client.get('/education_modules/{0}/'.format(self.education_module.pk))
        education_module = EducationModule.objects.get(pk=self.education_module.pk)
        serializer = EducationModuleSerializer(education_module)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_education_module(self):
        response = self.client.get('/education_modules/{0}/'.format(100000))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_education_module(self):
        response = self.client.put(
            '/education_modules/{0}/'.format(self.education_module.pk),
            self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_education_module(self):
        response = self.client.put(
            '/education_modules/{0}/'.format(self.education_module.pk),
            self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_education_module(self):
        response = self.client.delete('/education_modules/{0}/'.format(self.education_module.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_education_module(self):
        response = self.client.delete('/education_modules/{0}/'.format(100000))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

