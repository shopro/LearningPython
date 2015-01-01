a=int(input('Enter number: '))
#i=0
ls=[]
for i in range(0,a):
	#print i
	z=int(input('n : '))
	#print z
	ls.append(z)
	i=i+1
print ' start'

n=10
def fn(n,z):
	n=n+1
	print n
	print 'z:',z
	for j in range(0,len(ls),2):
		print j
		ls[j]=ls[j]+1
	#j=j+2
		print j
	return j

print ls
n=11
a=fn(11)
print 'a :',a
#ls.insert(0,99)
#j=0
#length = len(ls)
#length=length+5
#print 'Length is : ',length

print 'exit'

