name = input("Enter the employee's name: ")
id_number = input("Employee's ID number: ")
position = input("Employee's position: ")
monthly_salary = float(input("Enter the employee's monthly salary: "))
employee = (name, id_number, position, monthly_salary)
gross_pay = employee[3] * 12 
pf = gross_pay * 0.1  
net_pay = gross_pay - pf  
print("\n\n***********EMPLOYEE PAYROLL***********")
print("Name:", employee[0])
print("ID Number:", employee[1])
print("Position:", employee[2])
print("Monthly Salary:", employee[3])
print("Provident Fund (PF):", pf)
print("Net Pay:", net_pay)
print("************")
