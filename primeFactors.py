# long=600851475143
# for i in range(2,long):
# 	if(long%i==0):
# 		for j in range(2,i):
# 			if(i%j==0):
# 				break
# 		else:
# 			print("This is a prime factor= ",i)
num=600851475143
for i in range(2,num//2):
	if(num%i==0):
		for j in range(2,i):
			if(i%j==0):
				break
		else:
			print("This is prime factor=",i)
