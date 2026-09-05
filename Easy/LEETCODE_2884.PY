import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
   employees["salary"] =  employees["salary"] * 2 
   return employees

employees = pd.DataFrame({
    "name": ["Jack", "Piper", "Mia", "Ulysses"],
    "salary": [19666, 74754, 62509, 54866]
})

print(modifySalaryColumn(employees))