for number in [1,2,3,4,5]:
	print number

a={'a':1,'b':2}
for i in a.itervalues():
	print i
for i in a.iterkeys():
	print i
for i,j in a.items():
	print i,j