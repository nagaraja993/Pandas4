import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = sorted(employee['salary'].unique(), reverse= True)
    if len(salary) >= 2:
        df =  pd.DataFrame([salary[1]], columns = [f'SecondHighestSalary'])
    else:
        df =  pd.DataFrame([None], columns = [f'SecondHighestSalary'])
    return df
    