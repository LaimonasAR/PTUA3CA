
from typing import List     

class Employee:
    def __init__(self, name : str, salary: float) -> None:
        self.name = name
        self.salary = salary
        
    @staticmethod
    def calculate_payroll(employee_list: List['Employee']):
        # summed_salaries = 0
        # for employee in employee_list:
        #     summed_salaries += summed_salaries
        # return summed_salaries
        return sum(employee.salary for employee in employee_list)

