
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
if __name__ == '__main__':
	my_account = BankAccount(15)
	a=1
	while(a):
		print '''
				  1.deposit
				  2.withdraw
				  3.overdrawn/balance
				  4.exit '''
		a= input("Please Enter Your Choice:")
		if a==4:
			break
		elif a==1:
			amount=input("Enter the Amount to deposit in your acc:")
			my_account.deposit(amount)
			print my_account.balance
		elif a==2:
			amount=input("Enter the Amount to withdraw from your acc:")
			my_account.withdraw(amount)
			print my_account.balance
		elif a==3:
			my_account.overdrawn1(5)
     		print my_account.balance
     	else:
     		print "Sorry! Invalid Input. Please try again"
