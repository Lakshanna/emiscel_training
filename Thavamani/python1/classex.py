class myclass(object):
		def __init__(self,first,last):
			self.first=first
			self.last=last
			self.status="NEW"

		def change_status(self,status):
			self.status=status

my=myclass('muthu','selvam')
print my.first
print self.first

