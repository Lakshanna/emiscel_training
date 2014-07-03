fin=open("foo1.txt","w")
fin1=open("foo.txt")
for line in fin1:
	fin.write(line)
fin1.close()
fin.close()
