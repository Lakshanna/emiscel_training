class calc(object):
    def __init__(self, intamt=0):
        self.balance = intamt
    def deposit(self, amt):
        self.balance += amt
    def withdraw(self, amt):
    	aa=self.balance-amt
        if aa<500:
        #if self.balance>500 :
        	#and (self.balance-=amt)>500:
        	print "Sorry! You have not enough money (Min bal 500 required)"
    	else:
    	    self.balance -= amt
     #def overdrawn(self):
     #   return self.balance < 0
  			bnkac=[1,2,3,4,5]
			    acno=input("Enter Your Account No:")
			if acno in bnkac:

				if __name__ == '__main__':
					my_account = calc(500)
					a=1
					while(a):
					print '''
					  1.Cash Deposit
					  2.Cash Withdrawal
					  3.exit '''
						a= input("Please Enter Your Choice:")
						#3.overdrawn/balance

					if a==3:
						break
					elif a==1:
						   amt=input("Enter the Amount to deposit in your acc:")
						   my_account.deposit(amt)
						   print my_account.balance

					elif a==2:
						amt=input("Enter the Amount to withdraw from your acc:")
						my_account.withdraw(amt)
						print my_account.balance
					#elif a==3:
					#	my_account.overdrawn1(5)
			     	#	print my_account.balance
			     	else:
			     		print "Sorry! Invalid Input. Please try again"

		else
		print("You not having account in this bank")  
