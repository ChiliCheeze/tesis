from faker import Faker
import pandas as pd
import numpy as np
import random 
import re

#Remove yung mga additional information about the individual
def remove_suffix(name):
    return re.sub(r'\b(Jr\.|Sr\.|II|III|IV|V)\b', '', name).strip()

#Ginawa to para ma call siya sa other notebook, so kapag tinawag to maaccess yung dataframe 
def respondents(nRespondents = 239,seed=42): #Yung seed naman para kapag kada run hindi pabago bago yung data na igegenerate nya like stick lang siya dun sa unang nagenerate nya, Pwede siya baguhin if gusto mo na ibang data naman
    fake = Faker('en_PH') #Instantiate yung Faker, Ito naman pang generate to ng mga random names, addresses ganyan, tas kaya may 'en_PH' para nakabase siya sa Philippines     
    
    Faker.seed(seed) #same concept dun sa parameter, kinocall lang natin siya dito para alam ng system kung san sya mag ffunction
    random.seed(seed)


    scale = ['Always','Often', 'Sometimes', 'Never'] #Ito gagamitin natin siya para sa random choice dito siya mamimili kung anong bet nya 
    data = { 
        'sName' : [fake.name() for i in range(nRespondents)], #itong .name() object siya sa faker pang generate ng mga random names, then yung range() yung nRespondent diba ang value nya 239 so mag lloop siya ng 239 
         'Level of Identity' : [
            {
                'Q1': random.choice(scale),
                'Q2': random.choice(scale),
                'Q3': random.choice(scale),
                'Q4': random.choice(scale)
            }
            for i in range(nRespondents)
        ],
        'Level of Skills' : [
            {
                'Q1': random.choice(scale),
                'Q2': random.choice(scale),
                'Q3': random.choice(scale),
                'Q4': random.choice(scale)
            }
            for i in range(nRespondents)
        ],
        'Level of Knowledge' : [
            {
                'Q1': random.choice(scale),
                'Q2': random.choice(scale),
                'Q3': random.choice(scale),
                'Q4': random.choice(scale)
            }
            for i in range(nRespondents)
        ],
        'Context of Performance' : [
            {
                'Q1': random.choice(scale),
                'Q2': random.choice(scale),
                'Q3': random.choice(scale),
                'Q4': random.choice(scale)
            }
            for i in range(nRespondents)
        ],
        'Personal Factors' : [
            {
                'Q1': random.choice(scale),
                'Q2': random.choice(scale),
                'Q3': random.choice(scale),
                'Q4': random.choice(scale)
            }
            for i in range(nRespondents)
        ],
        'Fixed Factors' : [
            {
                'Q1': random.choice(scale),
                'Q2': random.choice(scale),
                'Q3': random.choice(scale),
                'Q4': random.choice(scale)
            }
            for i in range(nRespondents)
        ]
    }
    
    df = pd.DataFrame(data)
    
    map = {'Never': 1, 'Sometimes':2, 'Often':3, 'Always':4} 

    def replace_values(d): #Function to na pang map nung mga scale natin para machange siya into numerical, so ang nangyayari dito is 
        return {k: map.get(v, v) for k, v in d.items()} #gagawa siya ng bagong dictionary (d) so sa d na yun may key (k) then yung v ito yung im-map natin, kaya (v, v) yun kasi yung namap niya na value irereplace nya yun dun sa equivalent value niya

    df['Level of Identity'] = df['Level of Identity'].apply(replace_values)
    df['Level of Skills'] = df['Level of Skills'].apply(replace_values)
    df['Level of Knowledge'] = df['Level of Knowledge'].apply(replace_values)
    df['Context of Performance'] = df['Context of Performance'].apply(replace_values)
    df['Personal Factors'] = df['Personal Factors'].apply(replace_values)
    df['Fixed Factors'] = df['Fixed Factors'].apply(replace_values)


    df['Avg_Identity'] = df['Level of Identity'].apply(lambda x: sum(x.values()) / len(x)) #ito naman kinokompute niya yung average ng mga answers 
    df['Avg_Skills'] = df['Level of Skills'].apply(lambda x: sum(x.values()) / len(x))
    df['Avg_Knowledge'] = df['Level of Knowledge'].apply(lambda x: sum(x.values()) / len(x))
    df['Avg_cPerfromance'] = df['Context of Performance'].apply(lambda x: sum(x.values()) / len(x))
    df['Avg_pFactors'] = df['Personal Factors'].apply(lambda x: sum(x.values()) / len(x))
    df['Avg_fFactors'] = df['Fixed Factors'].apply(lambda x: sum(x.values()) / len(x))

    df['Overall'] = df[['Avg_Identity', 'Avg_Skills', 'Avg_Knowledge', 'Avg_cPerfromance', 'Avg_pFactors', 'Avg_fFactors']].mean(axis=1).round(2)

    return df