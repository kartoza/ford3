from ford3.models import import_qualifcations_from_scraped_file, SubFieldOfStudy

import csv

with open('django_project/ford3/scraping/SAQAData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif line_count < 8:
            # Create a qualification object for the row

            # For each of the columns with a subfield of study, get the
            # subfield of study from the populated list of subfields of study

            #
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
