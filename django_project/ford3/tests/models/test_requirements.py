from django.test import TestCase
from ford3.models.requirement import Requirement
from ford3.models.qualification import Qualification


class TestRequirements(TestCase):
    def setUp(self):
        Requirement.objects.create(
            id=1,
            description='Requirement Description',
            qualification_id=Qualification.objects.create(
                id=1,
                subfield_of_study_id=1,
                qualification_id=1,
                saqa_id=1,
                name="Qualification Name",
                short_description="This is a short description",
                long_description="This is a long description",
                nqf_level=5,
                duration_in_months=3,
                full_time=False,
                part_time=True,
                credits_after_completion=12,
                distance_learning=True,
                estimated_annual_fee=3000,
                campus_id=5
            ),
            assessment=True,
            interview=True,
            admission_point_score=24,
            min_qualification=1234)

    def test_requirement_description(self):
        newRequirement = Requirement.objects.get(id=1)
        self.assertEqual(newRequirement.__str__(), 'Requirement Description')