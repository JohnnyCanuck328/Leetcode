SELECT emp.Name AS 'Employee'
FROM Employee AS emp, Employee AS mana
WHERE
    emp.ManagerId = mana.Id AND 
    emp.Salary > mana.Salary;