import csv
from django.core.management.base import BaseCommand
from ford3.models import Qualification, SubFieldOfStudy

class Command(BaseCommand):
    """
    Import SAQA Qualifications from scraped CSV
    """
    def handle(self, *args, **options):
        with open('SAQAData.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                elif line_count < 8:
                    # Create a qualification object for the row
                    saqa_id = row[0]
                    name = row[1]
                    type = row[2]

                    new_qualification = Qualification() # type: Qualification
                    new_qualification.name = name
                    new_qualification.saqa_id = saqa_id
                    # Compile subfield of study
                    this_subfield_of_study = ''
                    for x in range(4, 8):
                        if len(row[x]) > 0:
                            this_subfield_of_study += ',' + row[x]

                    # For each subfield of study, get the subfield of study from
                    # the list of subfields of study in the database
                    subfield_of_study_object = SubFieldOfStudy.objects.filter(
                        name = this_subfield_of_study
                    )

                    new_qualification.sub_field_of_study = subfield_of_study_object.first()
                    new_qualification.save()
                    line_count += 1
        print(f'Processed {line_count} lines.')
