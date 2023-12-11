import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random 
from django.utils import timezone
from jobs.models import Company , Category , Job

def add_companies(n):
    images=['1.png','2.png']
    fake=Faker()
    for n in range(n):
        Company.objects.create(
            name=fake.name(),
            logo=f"company/{images[random.randint(0,1)]}",
            presentation=fake.text(),
            website=fake.domain_name(),
            email=fake.ascii_email(),
        )
    print(f'{n} Companies was created successfully')

def add_categories(n):
    images=['1.png','2.png']
    fake=Faker()
    for n in range(n):
        Category.objects.create(
            name=fake.name(),
            image=f"categorys/{images[random.randint(0,1)]}",
            job_count=random.randint(0,1),

        )
    print(f'{n} Categories was created successfully')

def add_jobs(n):
   fake=Faker()
   categories = Category.objects.all()
   companies = Company.objects.all()
   natures=['Full Time','Part Time','Remote','Freelance']
   for n in range(n):
        category = random.choice(categories)
        agency = random.choice(companies)
        current_date = timezone.now()
        Job.objects.create(
            title=fake.name(),
            category=category,
            agency=agency,
            location=fake.city(),
            salary=random.randint(500,90000),
            created_at=current_date,
            vacancy=random.randint(0,10),
            job_nature=natures[random.randint(0,3)],
            application_date=fake.date_time(),
            description=fake.text(),
            knowledge_requirements=fake.text(),
            education_experience=fake.text(),

        )
        print(f'{n} Jobs was created successfully')

add_companies()
add_categories()
add_jobs(0)