import random
import pandas as pd
from stdInfo import Student


class StudyHabitsSurvey(Student):
    def __init__(self, name, year, total_respondents, answered_respondents):
        super().__init__(name, year)
        self.total_respondents = total_respondents
        self.answered_respondents = answered_respondents
        self.sections = [
            "Homework/assignment",
            "Time allocation",
            "Reading and note-taking",
            "Study period procedure",
            "Written works",
            "Examination taking",
            "Teachers consultation"
        ]
        
        self.likert_scale = {
            1: "Strongly Disagree",
            2: "Disagree",
            3: "Agree",
            4: "Strongly Agree",
        }

    def generate_answers(self):
        # List of possible answers, including None (null)
        possible_answers = list(self.likert_scale.values()) + [None]
        return [random.choice(possible_answers) for _ in range(3)]

    def create_dataframe(self):
        # Initialize a dictionary to hold the data
        data = {section: [] for section in self.sections}
        
        # Iterate over the number of respondents
        for i in range(self.total_respondents):
            if i < self.answered_respondents:
                # Generate answers for those who answered
                for section in self.sections:
                    data[section].extend(self.generate_answers())
            else:
                # All answers are None for those who didn't answer
                for section in self.sections:
                    data[section].extend([None, None, None])
        
        # Convert the data dictionary into a DataFrame
        df = pd.DataFrame(data)
        return df


