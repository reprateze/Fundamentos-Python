import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
    

dados = {
    "employee_id": ["3", "90", "9", "60", "49", "43"],
    "Name": ["Bob", "Alice", "Tatiana", "Annabelle", "Jonathan", "Khaled"],
    "Department": [
        "Operations",
        "Sales",
        "Engineering",
        "InformationTechnology",
        "HumanResources",
        "Administration"
    ],
    "Salary": [48675, 11096, 33805, 37678, 23793, 40454]
}

employees = pd.DataFrame(dados)

print(selectFirstRows(employees))





