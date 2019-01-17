#coding=utf-8
"""Factories for building model instances for testing."""

import factory
from ford3.django_project.ford3.models.requirements import Requirements

class RequirementsF(factory.DjangoModelFactory):
    class Meta:
        model = Requirements
