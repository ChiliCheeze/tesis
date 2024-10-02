import random
import pandas as pd
from stdInfo import Student

class StudyHabitsSurvey(Student):
    def __init__(self, name, year, total_respondents, answered_respondents):
        super().__init__(name, year)
        self.total_respondents = total_respondents
        self.answered_respondents = answered_respondents
    
    def generate_study_habits_data(self):
        scale = ['Strongly Agree', 'Agree', 'Disagree', 'Strongly Disagree']
        
        # Prepare an empty dictionary to store the survey data
        data = {
            'Homework/Assignment Q1': [],
            'Homework/Assignment Q2': [],
            'Homework/Assignment Q3': [],
            'Time Allocation Q1': [],
            'Time Allocation Q2': [],
            'Time Allocation Q3': [],
            'Reading and Note-Taking Q1': [],
            'Reading and Note-Taking Q2': [],
            'Reading and Note-Taking Q3': [],
            'Study Period Procedure Q1': [],
            'Study Period Procedure Q2': [],
            'Study Period Procedure Q3': [],
            'Written Works Q1': [],
            'Written Works Q2': [],
            'Written Works Q3': [],
            'Examination Taking Q1': [],
            'Examination Taking Q2': [],
            'Examination Taking Q3': [],
            'Teachers Consultation Q1': [],
            'Teachers Consultation Q2': [],
            'Teachers Consultation Q3': []
        }
        
        # Generate answers for those who answered the survey
        for _ in range(self.answered_respondents):
            data['Homework/Assignment Q1'].append(random.choice(scale))
            data['Homework/Assignment Q2'].append(random.choice(scale))
            data['Homework/Assignment Q3'].append(random.choice(scale))
            data['Time Allocation Q1'].append(random.choice(scale))
            data['Time Allocation Q2'].append(random.choice(scale))
            data['Time Allocation Q3'].append(random.choice(scale))
            data['Reading and Note-Taking Q1'].append(random.choice(scale))
            data['Reading and Note-Taking Q2'].append(random.choice(scale))
            data['Reading and Note-Taking Q3'].append(random.choice(scale))
            data['Study Period Procedure Q1'].append(random.choice(scale))
            data['Study Period Procedure Q2'].append(random.choice(scale))
            data['Study Period Procedure Q3'].append(random.choice(scale))
            data['Written Works Q1'].append(random.choice(scale))
            data['Written Works Q2'].append(random.choice(scale))
            data['Written Works Q3'].append(random.choice(scale))
            data['Examination Taking Q1'].append(random.choice(scale))
            data['Examination Taking Q2'].append(random.choice(scale))
            data['Examination Taking Q3'].append(random.choice(scale))
            data['Teachers Consultation Q1'].append(random.choice(scale))
            data['Teachers Consultation Q2'].append(random.choice(scale))
            data['Teachers Consultation Q3'].append(random.choice(scale))

        # Fill in 'None' for respondents who didn't answer the survey
        for _ in range(self.answered_respondents, self.total_respondents):
            data['Homework/Assignment Q1'].append(None)
            data['Homework/Assignment Q2'].append(None)
            data['Homework/Assignment Q3'].append(None)
            data['Time Allocation Q1'].append(None)
            data['Time Allocation Q2'].append(None)
            data['Time Allocation Q3'].append(None)
            data['Reading and Note-Taking Q1'].append(None)
            data['Reading and Note-Taking Q2'].append(None)
            data['Reading and Note-Taking Q3'].append(None)
            data['Study Period Procedure Q1'].append(None)
            data['Study Period Procedure Q2'].append(None)
            data['Study Period Procedure Q3'].append(None)
            data['Written Works Q1'].append(None)
            data['Written Works Q2'].append(None)
            data['Written Works Q3'].append(None)
            data['Examination Taking Q1'].append(None)
            data['Examination Taking Q2'].append(None)
            data['Examination Taking Q3'].append(None)
            data['Teachers Consultation Q1'].append(None)
            data['Teachers Consultation Q2'].append(None)
            data['Teachers Consultation Q3'].append(None)
        
        # Convert the dictionary to a pandas DataFrame
        std_habits_df = pd.DataFrame(data)
        return std_habits_df


