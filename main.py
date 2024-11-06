# input statements
salary = float(1250.0)
numDependents = int(2)

# calculate taxes here
stateTax = float (salary*0.065)
federalTax = float (salary*.28)
dependentDeduction = float (salary*(.025*numDependents))
totalWithholding = float (stateTax + federalTax + dependentDeduction)
takeHomePay = float (salary - totalWithholding)

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" +str(federalTax))
print("Dependents: $" +str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))