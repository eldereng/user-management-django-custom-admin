from django.test import TestCase
from people.models import Person


class PersonModelTestCase(TestCase):
    def setUp(self) -> None:
        Person.objects.create(name="John Doe")
        Person.objects.create(name="Jane Doe", cpf="82697953051")

    def test_formatted_cpf(self):
        jane = Person.objects.get(name="Jane Doe")
        self.assertEqual(jane.formatted_cpf, "826.979.530-51")

    def test_create_all_people(self):
        people = Person.objects.all()
        self.assertEqual(len(people), 2)