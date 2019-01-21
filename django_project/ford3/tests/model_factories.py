#coding=utf-8
'''Factories for building model instances for testing.'''

import factory
from ford3.models.requirement import Requirement
from ford3.models.qualification import Qualification
from ford3.models.campus import Campus
from ford3.models.field_of_study import FieldOfStudy
from ford3.models.module import Module
from ford3.models.occupation import Occupation
from ford3.models.provider import Provider
from ford3.models.secondary_institution_type import SecondaryInstitutionType
from ford3.models.sub_field_of_study import SubFieldOfStudy
from ford3.models.subject import Subject





class RequirementsF(factory.DjangoModelFactory):
    class Meta:
        model = Requirement

def get_qualification_test_object():
    qualification_test_object_instance =  Qualification.objects.create(
            id=10,
            subfield_of_study_id=2,
            qualification_id=3 ,
            saqa_id=4,
            name='Qualification Name',
            short_description='Some short description',
            long_description='Some very long description that just goes on...',
            nqf_level=6,
            duration_in_months=12,
            full_time=True,
            part_time=False,
            credits_after_completion=200,
            distance_learning=False,
            estimated_annual_fee=100000,
            campus_id=55)
    return qualification_test_object_instance

def get_requirement_test_object():
    requirement_test_object_instance = Requirement.objects.create(
            id=1,
            description='Requirement Description',
            qualification_id=get_qualification_test_object(),
            assessment=True,
            interview=True,
            admission_point_score=24,
            min_qualification=1234)

    return requirement_test_object_instance

def get_secondary_institution_type_test_object():
    secondary_institution_type_test_object_instance = \
        SecondaryInstitutionType.objects.create(
            id=1,
            name='Object Test Name',
            description='Some long description that goes on...'
        )
    return secondary_institution_type_test_object_instance

def get_campus_test_object():
    campus_test_object_instance = Campus.objects.create(
        id=1,
        provider_id=get_provider_test_object(),
        name='Object Test Name',
        location='I dunno yet'
    )

    return campus_test_object_instance


def get_module_test_object():
    module_test_object_instance = Module.objects.create(
        id=1,
        name='Object Test Name',
        description='Some long description that goes on...'
    )

    return module_test_object_instance


def get_field_of_study_test_object():
    field_of_study_test_object_instance = FieldOfStudy.objects.create(
        id=1,
        name='Object Test Name'
    )

    return field_of_study_test_object_instance


def get_occupation_test_object():
    occupation_test_object_instance = Occupation.objects.create(
        id=1,
        name='Object Test Name',
        description='Some long description that goes on...'
    )

    return occupation_test_object_instance


def get_provider_test_object():
    provider_test_object_instance = Provider.objects.create(
        id=1,
        name='Object Test Name',
        website='www.mytest.com',
        logo_url='http://sometestplaceholder/logo.png',
        email='Test@test.com',
        admissions_contact_no='0137527576',
        postal_address='1200'
    )

    return provider_test_object_instance


def get_sub_field_of_study_test_object():
    sub_field_of_study_test_object_instance = SubFieldOfStudy.objects.create(
        id=1,
        name='Object Test Name',
        field_of_study_id=get_field_of_study_test_object(),
    )

    return sub_field_of_study_test_object_instance


def get_subject_test_object():
    subject_test_object_instance = Subject.objects.create(
        id=1,
        name='Object Test Name',
        description='Some long description that goes on',
        # secondary_institution_types =
    )

    return subject_test_object_instance