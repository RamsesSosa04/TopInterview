import pandas as pd

def createDataframe(student_data) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

student_data = [
    [1, 12],
    [2, 14],
    [3, 13],
    [4, 12]
] 
df = createDataframe(student_data)
print(df)