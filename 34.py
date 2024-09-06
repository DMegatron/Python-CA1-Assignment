balance = 0

while True:
    transaction = input("Enter transaction (D/W amount) or press Enter to finish: ")
    
    if transaction == '':
        break
    
    transaction_type, amount = transaction.split()
    amount = int(amount)
    
    if transaction_type == 'D':
        balance += amount
    elif transaction_type == 'W':
        balance -= amount
    else:
        print("Invalid transaction type. Please use 'D' for deposit or 'W' for withdrawal.")

print("Final balance:", balance)
