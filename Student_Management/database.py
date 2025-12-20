import pandas as pd
import numpy as np
from utils import get_data


def add_student(file_path, name, id, department):
    data = get_data(file_path)
    new_student = pd.DataFrame([[name, id, department]], columns=data.columns)
    data = pd.concat([data, new_student], ignore_index=True)
    data.to_csv(file_path, index=False)

def view_students(file_path):
    return get_data(file_path)

def search_student(file_path, id):
    data = get_data(file_path)
    result = data[data['ID'] == int(id)]
    if result.empty:
        print("⚠️ Student not found.")
    else:
        print("✅ Student found:")
        print(result)