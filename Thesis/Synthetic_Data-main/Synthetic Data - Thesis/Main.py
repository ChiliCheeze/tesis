from stdGrade import grd_system  # Import grd_system from grade_system.py
from faker import Faker
import random
import pandas as pd

# Setting a seed, so that results will consistent across different runs
FAKER_SEED = 42
RANDOM_SEED = 42

# Library for generating synthetic names 
fake = Faker('en_PH')
Faker.seed(FAKER_SEED)

random.seed(RANDOM_SEED)

# List for randomly picking year level 
yrLvl = [1, 2, 3, 4]

#Dataframe
tbl1 = []

# Create a random student and generate their grades
for _ in range(239):
    student = grd_system(fake.name(), random.choice(yrLvl))

    tbl1.append({
        "Student Name": student.name,
        "Year Level": student.year,
        "Student Number": student.stdNum,
        "Grades": student.grades,
        "GWA": student.final_grade,
        "Failed Subjects": student.sub_failed
    })

table_1 = pd.DataFrame(tbl1)

# Print the student's details and grades
print(student)