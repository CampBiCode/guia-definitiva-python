import pandas as pd

def generate_data(columns:int, rows:int) -> pd.DataFrame:
    data = {}
    for col in range(columns):
        data[col] = []
        for row in range(rows):
            data[col].append(row)
    
    df = pd.DataFrame(data) 
    return df

