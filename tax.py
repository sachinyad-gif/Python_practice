bp = float(input("Enter your basic pay"))

# HRA calculation
print("Enter 50 if you live in a Metro City & 40 if you live in non Metro City")
hra = int(input())
HRA = bp*(hra/100)

# Speacial Allowance Calculation
sp_al=float(input("Enter amount of Speacial Allowance if you get any"))

total_salary = bp + HRA + sp_al
print("------------------------------------")
print("")
print("Thus , Your Total Salary = ",total_salary)
print("")

# Fee Exemption 
if total_salary <= 1200000:
    taxable = 1200000 - 75000   #taxable means taxable salary
else:
    taxable = total_salary

# Tax Calculation
if taxable <= 400000:
    tax = 0
elif taxable <= 800000:
    tax = (taxable-400000)*0.05
elif taxable <= 1200000:
    tax = (400000*0.05) + (taxable-800000)*0.10
elif taxable <= 1600000:
    tax = (400000*0.05) + (400000*0.10) + (taxable-1200000)*0.15
elif taxable <= 2000000:
    tax = (400000*0.05) + (400000*0.10) + (400000*0.15) + (taxable-1600000)*0.20
elif taxable <= 2400000:
    tax = (400000*0.05) + (400000*0.10) + (400000*0.15) + (400000*0.20) + (taxable-2000000)*0.25
else:
    tax = (400000*0.05) + (400000*0.10) + (400000*0.15) + (400000*0.20) + (400000*0.25) + (taxable-2400000)*0.30

# Calculate 4% Health & Education cess on basic tax
cess_tax = tax*0.04
total_tax = tax + cess_tax
inhand_salary = (total_salary - total_tax)
print("----------Result-----------")
print("")
print("Your Tax amount = ",total_tax)
print("")
print("Your Inhand Salary = ",inhand_salary) 


