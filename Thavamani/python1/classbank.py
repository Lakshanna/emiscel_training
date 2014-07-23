class Bank(object):
	#global initial_balance
	def __init__(self,initial_balance=500):
			self.initial_balance=initial_balance
			
	def withdraw(self,amount):
		#print "%d" % initial_balance
		if amount<=0 :
			return("Cann't Withdraw")
		elif amount>=self.initial_balance :
			return("Amount exceeds Balance available")
		else:
			self.initial_balance -=amount
			return("Thank you...")

	def deposit	(self,amount):
		self.initial_balance +=amount
		return(self.initial_balance)

	def accbal(self):
		return(self.initial_balance)

	def menu(self):
		print "\t\t\t WELCOME"
		print "\t\t\t ~~~~~~~"
		print "\t\t CHOOSE UR CHOICE"
		print "\t\t\t 1.WITHDRAW"
		print "\t\t\t 2.DEPOSIT"
		print "\t\t\t 3.BALANCE ENQUIRY"
		print "\t\t\t 4.Quit\n"


if __name__=='__main__':
	customer=Bank(500)
	#customer.menu()
	while (1):
		customer.menu()
		print "\t Enter your wish...."
		choice=input("Enter your Choice")
		if choice==1:
			amt=input("\nAmount:")
			print("{0}".format(customer.withdraw(amt)))
		elif choice==2:
			amt=input("Amount")
			print("\nAmount Deposited Successfully\n")
			print("\nAvailable balance in your account is {0}\n".format(customer.deposit(amt)))
		elif choice==3:
			print("\nAvailable balance in your account is {0}\n".format(customer.accbal()))
		elif choice==4:
		 	print("\nThank u")
		 	break
		else:
		 	print "\nInvalid choice"






