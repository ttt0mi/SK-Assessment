

def account_balance_check(account_balance):
	
	if not account_balance or account_balance.isspace():
		return "account balance cannot be empty"

	temp = account_balance.replace('.','',1)
	temp2 = temp.replace('-','',1)	

	if not temp2.isdecimal():
		return "invalid characters present"

	if temp2.startswith('0'):
		return "account balance cannot start with 0"
	
	account_balance = round(float(account_balance), 2)

	if account_balance <= 0:
		return "account balance must be a positive number"

	if account_balance < 1000:
		return "minimum account balance limit not exceeded"
	else:
		return account_balance




def amount_check(account_balance, amount):

	if not amount or amount.isspace():
		return "amount cannot be empty"

	temp = amount.replace('.','',1)
	temp2 = temp.replace('-','',1)

	if not temp2.isdecimal():
		return "invalid characters present"

	if temp2.startswith('0'):
		return "amount cannot start with 0"

	amount = float(amount)

	if amount != round(amount, 2) or amount <= 0:
		return "invalid amount entered"
	elif amount > 20000:
		return "maximum withdrawal limit reached"
	elif amount % 500 != 0:
		return "invalid amount, only multiples of £500/£1000 allowed"
	elif amount > (account_balance * 0.9):
		return "invalid amount, cannot withdraw more than 90% of account balance"
	else:
		return amount



def withdraw(account_balance, transactions, amount):

	account_balance -= (amount + 100)
	
	transactions.append({'withdrawal amount' : amount, 'withdrawal fee' : 100, 'remaining balance' : account_balance})
	return (account_balance, "Transaction Successful")



def withdrawal_details(transactions):
	for transaction in transactions:
		for iden, info in transaction.items():
			print(f"{iden}: £{info}")
		print()



"""

transactions = []
proceed = True


while proceed:
	account_balance = str(input("What is your account balance: "))

	if type(account_balance_check(account_balance)) != float:
		print(account_balance_check(account_balance))
		continue

	account_balance = account_balance_check(account_balance)
	print(f"Your current balance: £{account_balance}")


	while proceed:
		amount = str(input("how much do you want to withdraw(multiples of £500/£1000): "))

		if type(amount_check(account_balance, amount)) != float:
			print(amount_check(account_balance, amount))
			continue

		amount = amount_check(account_balance, amount)

		account_balance, word = withdraw(account_balance, transactions, amount)
		print(word)
		withdrawal_details(transactions)


		while proceed:
			choice = str(input("do you want to make another withdrawal. |yes or no|: "))
			choice = choice.upper()

			match choice:
				case "YES":
					break

				case "NO":
					proceed = False
					break

				case _:
					print("invalid choice, try again")
					continue


print("bye")

"""










		