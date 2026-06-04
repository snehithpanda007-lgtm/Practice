expenses_length = int(input("Enter number of expenses: "))
expenses = []

for i in range(expenses_length):
    amount = float(input("Enter amount: "))
    expenses.append(amount)

total = sum(expenses)
average = total/expenses_length

print("Total: ", str(total))
print("Average: ", str(average))
print("Highest Expense:", max(expenses))
print("Lowest Expense:", min(expenses))