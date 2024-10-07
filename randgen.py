import random as rd
numval=int(input('Enter Number of values: '))
lowlim=int(input('Enter lower limit: '))
uplim=int(input('Enter upper limit: '))
filename=input('Enter filename: ')

fd=open(filename,'w')
for i in range(numval):
	val = rd.randrange(lowlim,uplim)
	fd.write(f"{val},")
val = rd.randrange(lowlim,uplim)
fd.write(f"{val}")
fd.close()

