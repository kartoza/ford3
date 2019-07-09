# Generated by Django 2.1.7 on 2019-05-30 13:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ford3.enums.saqa_qualification_level


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_province', models.BooleanField(default=False, verbose_name='province status')),
                ('is_provider', models.BooleanField(default=False, verbose_name='provider status')),
                ('is_campus', models.BooleanField(default=False, verbose_name='campus status')),
                ('account_activated', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the campus', max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, help_text='The spatial point position of the campus', null=True, srid=4326)),
                ('photo', models.FileField(help_text='Representative photo of campus', null=True, upload_to='campus/photo')),
                ('telephone', models.CharField(help_text="The campus' telephone number", max_length=255, null=True)),
                ('email', models.EmailField(help_text="The campus' email", max_length=255, null=True)),
                ('max_students_per_year', models.PositiveIntegerField(help_text='Maximum number of students', null=True)),
                ('physical_address_line_1', models.CharField(help_text="The campus' physical address details", max_length=255, null=True)),
                ('physical_address_line_2', models.CharField(help_text="The campus' physical address details", max_length=255, null=True)),
                ('physical_address_city', models.CharField(help_text="The campus' physical address city", max_length=255, null=True)),
                ('physical_address_postal_code', models.CharField(help_text="The campus' physical address post code", max_length=255, null=True)),
                ('postal_address_differs', models.BooleanField(default=False, help_text='Is the postal address different from the physical address?', null=True)),
                ('postal_address_line_1', models.CharField(help_text="The campus' postal address", max_length=255, null=True)),
                ('postal_address_line_2', models.CharField(help_text="The campus' postal address", max_length=255, null=True)),
                ('postal_address_city', models.CharField(help_text="The campus' postal address city", max_length=255, null=True)),
                ('postal_address_postal_code', models.CharField(help_text="The campus' postal adress code", max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, help_text='Campus has been deleted')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campus_created_by', to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campus_edited_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CampusEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of this event', max_length=255)),
                ('date_start', models.DateField(help_text='The date on which the event starts')),
                ('date_end', models.DateField(help_text='The date on which the event ends')),
                ('http_link', models.URLField(blank=True, help_text='A link to a web page containing additional details regarding this event', max_length=255, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="The field of study's name", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A short identifier for the interest', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="The occupation's name", max_length=255)),
                ('description', models.TextField(blank=True, help_text='A short description of the occupation', null=True)),
                ('green_occupation', models.BooleanField(default=False, help_text='Is this an occupation suited as a good first job')),
                ('scarce_skill', models.BooleanField(default=False, help_text='Would this occupation be consider a scarce skill')),
                ('tasks', models.TextField(blank=True, help_text='A short summary of tasks involved with this occupation', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Prospect first and last name', max_length=150, verbose_name='Name (required)')),
                ('telephone', models.CharField(blank=True, help_text='Prospect telephone number', max_length=150)),
                ('email', models.EmailField(help_text='Prospect email address', max_length=254, verbose_name='Email (required)')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text="The provider's name", max_length=255)),
                ('provider_type', models.CharField(default='', help_text='The type of the institution', max_length=255)),
                ('telephone', models.CharField(help_text="The provider's telephone number", max_length=12, null=True)),
                ('website', models.CharField(blank=True, help_text="The provider's main web page", max_length=255, null=True)),
                ('email', models.CharField(help_text='The email address interested parties can reach you at', max_length=255)),
                ('admissions_contact_no', models.CharField(help_text='A contact number students interested in applying can use', max_length=255, null=True)),
                ('physical_address_postal_code', models.CharField(help_text="The provider's 4 digit post code", max_length=4)),
                ('physical_address_line_1', models.CharField(help_text="Details of the provider's physical address", max_length=255, null=True)),
                ('physical_address_line_2', models.CharField(help_text="Details of the provider's physical address", max_length=255, null=True)),
                ('physical_address_city', models.CharField(help_text='The city which the provider is in', max_length=255, null=True)),
                ('provider_logo', models.ImageField(blank=True, help_text="The provider's logo", upload_to='provider_logo')),
                ('postal_address_differs', models.BooleanField(blank=True, default=False, null=True)),
                ('postal_address_postal_code', models.CharField(blank=True, max_length=4, null=True)),
                ('postal_address_line_1', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_address_city', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, help_text='Provider has been deleted')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_created_by', to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_edited_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the province', max_length=255)),
                ('location', models.CharField(help_text="The province's location", max_length=255, null=True)),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="The qualification's name", max_length=255)),
                ('short_description', models.CharField(blank=True, help_text='A short description of what the qualification entails', max_length=120, null=True)),
                ('long_description', models.CharField(blank=True, help_text='A longer description of the qualification for the student who is interested and would like to know more', max_length=500, null=True)),
                ('duration_in_months', models.IntegerField(blank=True, help_text='How long the qualification takes to complete (in months)', null=True)),
                ('full_time', models.BooleanField(blank=True, default=False, help_text='Can this qualification be completed on a full-time basis?', null=True)),
                ('part_time', models.BooleanField(blank=True, default=False, help_text='Can this qualification be completed on a part-time basis?', null=True)),
                ('credits_after_completion', models.IntegerField(blank=True, help_text='How many credits are awarded after completion?', null=True)),
                ('distance_learning', models.BooleanField(blank=True, default=False, help_text='Does this qualification have a distance learning option?', null=True)),
                ('completion_rate', models.IntegerField(blank=True, default=0, help_text='What has the completion rate for this qualifcation been?', null=True)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, help_text='What is the total cost to complete this qualification?', max_digits=20, null=True)),
                ('total_cost_comment', models.CharField(blank=True, help_text='Any comments regarding the cost and payment options of this qualification should be filled in here', max_length=255, null=True)),
                ('critical_skill', models.BooleanField(blank=True, default=False, help_text='Would the skill obtained by completing this qualification be considered a critical skill?', null=True)),
                ('green_occupation', models.BooleanField(blank=True, default=False, help_text='Would the occupations this qualification prepares you for be considered environmentally friendly?', null=True)),
                ('high_demand_occupation', models.BooleanField(blank=True, default=False, help_text='Are the occupations this qualification prepares you for in high demand?', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, help_text='Qualification has been deleted')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Campus')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_created_by', to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_edited_by', to=settings.AUTH_USER_MODEL)),
                ('interests', models.ManyToManyField(blank=True, to='ford3.Interest')),
                ('occupations', models.ManyToManyField(blank=True, to='ford3.Occupation')),
            ],
        ),
        migrations.CreateModel(
            name='QualificationEntranceRequirementSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_score', models.IntegerField(blank=True, help_text='The minimum score required for this subject', null=True)),
                ('required', models.BooleanField(blank=True, default=False, help_text='Is this subject required?', null=True)),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ford3.Qualification')),
            ],
        ),
        migrations.CreateModel(
            name='QualificationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A short identifier for the event', max_length=255)),
                ('date_start', models.DateField(help_text='When does this event start?')),
                ('date_end', models.DateField(help_text='When does this event end?')),
                ('event_date', models.DateField(blank=True, null=True)),
                ('other_event', models.CharField(blank=True, max_length=255, null=True)),
                ('http_link', models.URLField(blank=True, help_text='A link to a web page with additional details regarding this event', max_length=255, null=True)),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Qualification')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, help_text='A summary of the requirements and type of requirements required for the assocaited qualification', max_length=255, null=True)),
                ('assessment', models.BooleanField(blank=True, default=False, help_text='Is there an assessment as part of the application process?', null=True)),
                ('interview', models.BooleanField(blank=True, default=False, help_text='Is there an interview as part of the application process?', null=True)),
                ('admission_point_score', models.IntegerField(blank=True, help_text='The admission point score required for the qualification', null=True)),
                ('min_nqf_level', models.CharField(blank=True, choices=[(ford3.enums.saqa_qualification_level.SaqaQualificationLevel('Grade 9'), 'Grade 9'), (ford3.enums.saqa_qualification_level.SaqaQualificationLevel('Grade 10 and National (vocational) Certificates level 2'), 'Grade 10 and National (vocational) Certificates level 2'), (ford3.enums.saqa_qualification_level.SaqaQualificationLevel('Grade 11 and National (vocational) Certificates level 3'), 'Grade 11 and National (vocational) Certificates level 3'), (ford3.enums.saqa_qualification_level.SaqaQualificationLevel('Grade 12 (National Senior Certificate) and National (vocational) Cert.'), 'Grade 12 (National Senior Certificate) and National (vocational) Cert.'), (ford3.enums.saqa_qualification_level.SaqaQualificationLevel('Higher Certificates and Advanced National (vocational) Cert.'), 'Higher Certificates and Advanced National (vocational) Cert.'), (ford3.enums.saqa_qualification_level.SaqaQualificationLevel('National Diploma and Advanced certificates'), 'National Diploma and Advanced certificates'), (ford3.enums.saqa_qualification_level.SaqaQualificationLevel("Bachelor's degree, Advanced Diplomas, Post Graduate Certificate and B-tech"), "Bachelor's degree, Advanced Diplomas, Post Graduate Certificate and B-tech"), (ford3.enums.saqa_qualification_level.SaqaQualificationLevel('Honours degree, Post Graduate diploma and Professional Qualifications'), 'Honours degree, Post Graduate diploma and Professional Qualifications'), (ford3.enums.saqa_qualification_level.SaqaQualificationLevel("Master's degree"), "Master's degree"), (ford3.enums.saqa_qualification_level.SaqaQualificationLevel("Doctor's degree"), "Doctor's degree")], help_text='The minimum NQF level a person needs to have obtained to apply for this qualification', max_length=120, null=True)),
                ('portfolio', models.BooleanField(blank=True, default=False, help_text='Does the applicant need to submit a portfolio as part of the application process?', null=True)),
                ('portfolio_comment', models.CharField(blank=True, help_text='Additional information regarding the portfolio to be submitted', max_length=255, null=True)),
                ('aps_calculator_link', models.URLField(blank=True, help_text='A link a calculator or the specifications for calculating the required APS score.', null=True)),
                ('require_aps_score', models.BooleanField(blank=True, default=False, help_text='Does the applicant need to acheive a certain APS score?', null=True)),
                ('require_certain_subjects', models.BooleanField(blank=True, default=False, help_text='Are there specific subjects listed as a prerequisite for this qualification', null=True)),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Qualification')),
            ],
        ),
        migrations.CreateModel(
            name='SAQAQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saqa_id', models.IntegerField(help_text='The ID of the qualification as listed in the SAQA database')),
                ('name', models.CharField(help_text='The name of the qualification as approved by SAQA', max_length=255, null=True)),
                ('nqf_level', models.IntegerField(blank=True, help_text='The NQF level SAQA has attributed to this qualification', null=True)),
                ('accredited', models.BooleanField(default=True)),
                ('creator_provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ford3.Provider')),
                ('field_of_study', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ford3.FieldOfStudy')),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryInstitutionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the secondary institution type', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubFieldOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A short identifier for the sub field of study', max_length=255)),
                ('field_of_study', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ford3.FieldOfStudy')),
                ('occupation_id', models.ManyToManyField(to='ford3.Occupation')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the subject', max_length=255)),
                ('description', models.CharField(blank=True, help_text='A short description of what the learner can expect to learn whilst completing this subject', max_length=500, null=True)),
                ('secondary_institution_types', models.ManyToManyField(to='ford3.SecondaryInstitutionType')),
            ],
        ),
        migrations.AddField(
            model_name='saqaqualification',
            name='sub_field_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ford3.SubFieldOfStudy'),
        ),
        migrations.AddField(
            model_name='qualificationentrancerequirementsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ford3.Subject'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='saqa_qualification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ford3.SAQAQualification'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='subjects',
            field=models.ManyToManyField(through='ford3.QualificationEntranceRequirementSubject', to='ford3.Subject'),
        ),
        migrations.AddField(
            model_name='provider',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ford3.Province'),
        ),
        migrations.AddField(
            model_name='campus',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Provider'),
        ),
        migrations.AddField(
            model_name='user',
            name='provinces',
            field=models.ManyToManyField(blank=True, to='ford3.Province'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='CampusUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ford3.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProviderUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ford3.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProvinceUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ford3.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
