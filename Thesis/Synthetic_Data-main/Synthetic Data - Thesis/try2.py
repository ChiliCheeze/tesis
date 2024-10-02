import random
import pandas as pd  # Import pandas to use DataFrame
from stdInfo import Student

class S_H_Survey(Student):

    def __init__(self, name, year, Total_respondents, Respondents_ans):
        super().__init__(name, year)
        self.category = [
            "Homework",
            "Time Allocation",
            "Reading and Note Taking",
            "Study Period Procedures",
            "Written Works",
            "Examination"
        ]
        self.question = 3  # 3 questions per category
        self.Total_respondents = Total_respondents  # Total number of respondents
        self.Respondents_ans = Respondents_ans  # Number of respondents who will answer questions

    def answers(self):
        # Likert scale responses
        scale = ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"]

        all_total_respondents = []  # Storage for all respondents' answers

        # Loop over each respondent
        for i in range(self.Total_respondents):
            respondents = {}  # Storage for a single respondent's answers

            # If the respondent is supposed to answer questions
            if i < self.Respondents_ans:
                for section in self.category:  # Loop through each category
                    for q in range(1, self.question + 1):  # For each question in the section
                        response = random.choice(scale)  # Random response from the scale
                        # Store response with a key like 'Homework_Q1', 'Homework_Q2', etc.
                        respondents[f"{section}_Q{q}"] = response
            else:
                # If the respondent is not supposed to answer, mark all answers as None
                for section in self.category:
                    for q in range(1, self.question + 1):
                        respondents[f"{section}_Q{q}"] = None

            all_total_respondents.append(respondents)  # Append this respondent's data

        # Convert the list of dictionaries into a DataFrame
        df = pd.DataFrame(all_total_respondents)
        return df

# Example usage:
# survey = S_H_Survey("Example University", "2024", 10, 5)
# df_results = survey.answers()
# print(df_results)
