from django.test import TestCase
from ford3.models.qualifications import Qualification


class TestQualifications(TestCase):
    def setUp(self):
        Qualification.objects.create(
            id=10,
            subfield_of_study_id=2,
            qualification_id=3 ,
            saqa_id=4,
            name='Qualification Name',
            short_description='Some short description',
            long_description='Some very long description that just goes on',
            NQF_level=6,
            duration_in_months=12,
            full_time=True,
            part_time=False,
            credits_after_completion=200,
            distance_learning=False,
            estimated_annual_fee=100000,
            campus_id=55)

    def test_qualificatoin_description(self):
        newQualification = Qualification.objects.get(id=10)
        self.assertEqual(newQualification.__str__(), 'Qualification Name')
