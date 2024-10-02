from faker import Faker
import pandas as pd
import random 
import re

def remove_suffix(name):
    return re.sub(r'\b(Jr\.|Sr\.|II|III|IV|V)\b', '', name).strip()

def students(nStd = 239,seed=42):
    fake = Faker('en_PH')
    
    Faker.seed(seed)
    random.seed(seed)

    gPoint = [1.00, 1.25,1.50,1.75,2.00,2.25,2.50,2.75,3.00,4.00,6.00,9.00]
    weights = [50,65,60,65,50,50,50,50,50,1,0.5,0.5]

    Data = {
        'sName' : [fake.name() for i in range(nStd)],
        'Sub1': [random.choices(gPoint, weights=weights, k=1)[0]  for _ in range(nStd)],
        'Sub2': [random.choices(gPoint, weights=weights, k=1)[0]  for _ in range(nStd)],
        'Sub3': [random.choices(gPoint, weights=weights, k=1)[0]  for _ in range(nStd)],
        'Sub4': [random.choices(gPoint, weights=weights, k=1)[0]  for _ in range(nStd)],
        'Sub5': [random.choices(gPoint, weights=weights, k=1)[0]  for _ in range(nStd)],
        'Sub5': [random.choices(gPoint, weights=weights, k=1)[0]  for _ in range(nStd)],
        'Sub6': [random.choices(gPoint, weights=weights, k=1)[0]  for _ in range(nStd)],
        'Sub7': [random.choices(gPoint, weights=weights, k=1)[0]  for _ in range(nStd)],
        'Sub8': [random.choices(gPoint, weights=weights, k=1)[0]  for _ in range(nStd)]   
    }

    df = pd.DataFrame(Data)

    df['GWA'] = df[['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5', 'Sub6', 'Sub7', 'Sub8']].mean(axis=1, skipna=True).round(2)

    
    def grade_func(grade):
        if grade in {4.00, 9.00}:
            return 5.00
        elif grade == 6.00:
            return None
        else: 
            return grade

    for col in ['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5', 'Sub6', 'Sub7', 'Sub8']:
        df[col] = df[col].apply(grade_func)

    return df


