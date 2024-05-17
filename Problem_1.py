import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = sorted(employee['salary'].unique(), reverse= True)
    if len(salary) >= N and N >= 1:
        df =  pd.DataFrame([salary[N-1]], columns = [f'getNthHighestSalary({N})'])
    else:
        df =  pd.DataFrame([None], columns = [f'getNthHighestSalary({N})'])
    return df