import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import json

with open('student.json', 'rb') as f:
    payload=json.load(f)


os.environ['OPENAI_API_KEY']=""

model=ChatOpenAI(model='gpt-4', temperature=1.0)

prompt=ChatPromptTemplate.from_template('''
Student Name: {name}
Field of Study: {field_of_study}
Year of Study: {year_of_study}
List of Subjects: {list_of_subjects}`
Preferred Learning Style: {preferred_learning_style}
Personal Objectives Challenges: {personal_objectives_challenges}
Extracurricular acitivities: {extracurricular_activities}

You are a student counselor. Your job is to use the information given about a student and create a study plan that not only addresses academic requirements but also aligns with each student's unique needs and aspirations. 

The output format should be: 
1. <overview of the current student>
2. <do the extracurricular activities align with the student's field of study?>
3. <study plan including how many hours to study, how many to hours to give extracurricular activites>
4. <how can the student improve?>

Your response should be brief.

''')

output_parser=StrOutputParser()

chain= prompt | model | output_parser



for p in payload:
    print('Study plan for ', p['Name'])
    print(chain.invoke({"name":p['Name'], 
                        "field_of_study": p['Field_of_study'],
                        "year_of_study": p['Year_of_study'],
                        "list_of_subjects": p['List_of_subjects'],
                        "preferred_learning_style": p['Preferred_Learning_Styles'],
                        "personal_objectives_challenges": p['Personal_Objectives_Challenges'],
                        "extracurricular_activities": p['Extracurricular_activities']
                        }))
    print()