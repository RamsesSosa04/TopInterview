import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    rename = {
        'id' : ' students_id',
        'first' : 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }
    students = students.rename(columns=rename)
    return students