from reader import read_csv, get_hourly_rate
from models import Employee
from typing import List

def parse_employees(filepaths: List[str]) -> List[Employee]:
    employees = []
    for filepath in filepaths:
        rows = read_csv(filepath)
        for row in rows:
            employees.append(Employee(
                name=row['name'],
                department=row['department'],
                hours=float(row['hours_worked']),
                rate=get_hourly_rate(row)
            ))
    return employees
