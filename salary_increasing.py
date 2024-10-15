#Initializing variables
current_salary = 0
increase_percentage = 0
increase_amount = 0
final_salary = 0

#input
current_salary = float(input("Enter your current salary :"))
increase_percentage = float(input("Enter  the increase percentage :"))

#operation
increase_amount  = current_salary*(increase_percentage/100) #finding the amount of increasing
final_salary = increase_amount + current_salary

#output
print("New Salary Amount is : ",final_salary)
