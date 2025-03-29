import pandas as pd

def select_student(students : pd.DataFrame):
    mask = students['student_id']==101
    filter = students[mask]
    result = filter[['name', 'age']]
    return result
