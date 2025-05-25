user_monthly_income = float(input("Enter your monthly income:"))
user_monthly_expense = float(input("Enter your total monthly expenses:"))

monthly_savings = user_monthly_income - user_monthly_expense
interest_rate = 0.05

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

print("Your monthly savings are $" , monthly_savings)
print("Projected savings after one year, with interest, is:", "$", projected_savings)