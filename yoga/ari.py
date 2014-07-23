import ipdb;
class arith(object):
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def add(self):
      return self.a+self.b
   def sub(self):
      return self.a-self.b
   def mul(self):
      return self.a*self.b
   def div(self):
      return self.a/self.b
ipdb.set_trace()
if __name__ == '__main__':
 um = 'y'
 while (um == 'y' or um == 'Y'):
   print "\nEnter any two non-zero values\n"
   a = input("Enter first value  = ")
   b = input("Enter second value = ")
   print "Here assign values of a and b to class object\n\n" 
   ari1 = arith(a,b)
   option = raw_input("\nEnter which operation you want (A)dd, (S)ubtract, (M)ultiply, (D)ivision")
   if option == 'A' or option == 'a':
      print "Addition is "
      print ari1.add()
   if option == "S" or option == 's':
      print "\nSubstraction is "
      print ari1.sub()
   if option == "M" or option == 'm':
      print "\nMultiplication is "
      print ari1.mul()
   if option == "D" or option == 'd':
      print "\nDiivision is "
      print ari1.div()
   um = raw_input("\n\n   Do you want to Continue (Y)es or (N)o ")
 print "\n\nW E L C O M E   A G A I N"
   

