from django.test import TestCase
from ford3.tests.models.model_factories import ModelFactories


class TestQualification(TestCase):
    def setUp(self):
        self.qualification = ModelFactories.get_qualification_test_object()

    def test_mark_qualification_as_deleted(self):
        self.new_campus = ModelFactories.get_campus_test_object()
        self.new_qualification1 = (
            ModelFactories.get_qualification_test_object())
        self.new_qualification2 = (
            ModelFactories.get_qualification_test_object())
        self.new_qualification3 = (
            ModelFactories.get_qualification_test_object())
        self.new_qualification1.campus = self.new_campus
        self.new_qualification2.campus = self.new_campus
        self.new_qualification3.campus = self.new_campus
        self.new_qualification1.save()
        self.new_qualification2.save()
        self.new_qualification3.save()

        form_data = {
            'saqa_ids': '{} {}'.format(
                self.new_qualification1.saqa_qualification_id,
                self.new_qualification2.saqa_qualification_id)
        }
        self.assertEqual(len(self.new_campus.qualifications), 3)
        self.new_campus.delete_qualifications(form_data)
        self.assertTrue(self.new_campus)
        # It should delete all but the form data
        self.assertEqual(len(self.new_campus.qualifications), 2)
        self.assertEqual(len(self.new_campus.qualifications), 1)
        self.assertEqual(
            str(self.qualification),
            'SAQAQualification name')


class TestQualificationOccupations(TestCase):
    def setUp(self):
        self.qualification = ModelFactories.get_qualification_test_object()
        self.occupation = ModelFactories.get_occupation_test_object()

    def test_toggle_occupations(self):

        # ModelFactories.get_qualification_test_object()
        # already adds one occupation
        self.assertEqual(self.qualification.occupations.count(), 1)

        occupation_ids = ' '.join([
            str(self.occupation.id)
        ])

        self.qualification.toggle_occupations(occupation_ids)
        self.assertEqual(self.qualification.occupations.count(), 1)
