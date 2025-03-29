import pandas as pd

def select_student(students):
    df = pd.DataFrame(students)
    mask = df['student_id']==101
    filter = df[mask]
    result = filter[['name', 'age']]
    return result
students = [
    {"student_id" : 101, "name" : "Ulises", "age" : 29},
    {"student_id" : 102, "name" : "Ramses", "age" : 20},
    {"student_id" : 103, "name" : "Aurelio", "age" : 53}
]
print(select_student(students))
