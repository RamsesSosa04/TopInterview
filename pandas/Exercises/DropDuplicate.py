import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'], keep='first')
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@gmail.com', 'michael@gmail.com', 'sarah@gmail.com', 
    'john@gmail.com', 'john@gmail.com', 'alice@gmail.com']
}
