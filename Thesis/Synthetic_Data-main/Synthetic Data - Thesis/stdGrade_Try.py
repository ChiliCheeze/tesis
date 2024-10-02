import random
from stdInfo import Student

# Inheriting Student attributes for student information 
class grd_system(Student): 
    # Identify and define year level curriculum
    curriculum = {
        1: {
            "subjects": 5,
            "units": [2, 3, 3, 3, 3]
        },
        2: {
            "subjects": 8,
            "units": [2, 3, 3, 3, 3, 3, 3, 3]
        },
        3: {
            "subjects": 7,
            "units": [3, 3, 3, 3, 3, 3, 3]
        },
        4: {
            "subjects": 5,
            "units": [3, 3, 3, 3, 3]
        }
    }
    
    def __init__(self, name, year):
        super().__init__(name, year)
        self.grades = self.std_grade()
        self.tgp, self.total_units, self.final_grade, self.sub_failed = self.calculate_final_grade()

    # Generation of grades 
    def std_grade(self):
        grade_scale = [1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 4.00, 5.00]
        std_year_curriculum = self.curriculum[self.year]
        grades = [random.choice(grade_scale) for _ in range(std_year_curriculum["subjects"])]
        return grades
    
    # Computation of grades 
    def calculate_final_grade(self):
        std_year_curriculum =  self.curriculum[self.year]
        tgp = 0  
        valid_units = 0  # Valid units that correspond to passing grades
        sub_failed = 0  # Track units of failed subjects

        for grade, units in zip(self.grades, std_year_curriculum["units"]):
            if grade < 4.00:  # Only count valid grades
                tgp += grade * units
                valid_units += units  # Only count units for passing grades
            else:
                sub_failed += 1  # Track failed subjects

        final_grade = tgp / valid_units if valid_units > 0 else "N/A"
        return round(tgp, 2), valid_units, round(final_grade, 2) if final_grade != "N/A" else final_grade, sub_failed

    def __str__(self):
        return (f"Student Name: {self.name}, Year Level: {self.year}, "
                f"Student Number: {self.stdNum}, Grades: {self.grades}, "
                f"Final Grade: {self.final_grade}, Failed Units: {self.sub_failed}")

import random
import pandas as pd
from faker import Faker
from stdInfo import Student

# Setting a seed, so that results will consistent across different runs
FAKER_SEED = 43
RANDOM_SEED = 43

# Library for generating synthetic names 
fake = Faker('en_PH')
Faker.seed(FAKER_SEED)

random.seed(RANDOM_SEED)

# Inheriting Student attributes for student information 
class GrdSystem(Student): 
    # Define the year level curriculum
    curriculum = {
        1: {
            "subjects": 5,
            "units": [2, 3, 3, 3, 3]
        },
        2: {
            "subjects": 8,
            "units": [2, 3, 3, 3, 3, 3, 3, 3]
        },
        3: {
            "subjects": 7,
            "units": [3, 3, 3, 3, 3, 3, 3]
        },
        4: {
            "subjects": 5,
            "units": [3, 3, 3, 3, 3]
        }
    }
    
    def __init__(self, students):
        super().__init__(students)
        self.std_info = self.std_info_dt()  # Get student information
        self.grades = self.std_grade()  # Generate grades
        # self.tgp, self.total_units, self.final_grade, self.sub_failed = self.calculate_final_grade()

    def std_grade(self):
        # Grade scale based on common grading systems
        grade_scale = [1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 4.00, 5.00]
        all_student_grades = []

        for i, row in self.std_info.iterrows():
            year = row["Year"]  # Identify the student's year
            std_year_curriculum = self.curriculum[year]  # Get curriculum for that year
            
            grades = {}
            for subs in range(std_year_curriculum["subjects"]):  # Generate grades for subjects
                grade = random.choice(grade_scale)
                grades[f'Subject_{subs + 1}'] = grade  # Assign grades for each subject

            all_student_grades.append(grades)  
        
        return pd.DataFrame(all_student_grades)  

    def overall_dt_stdGrades(self):
        # Concatenate student info and grades
        return pd.concat([self.std_info, self.grades], axis=1)