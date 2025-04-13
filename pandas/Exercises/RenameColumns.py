#2885. Rename Columns
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    rename = {
        'id' : ' students_id',
        'first' : 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }
