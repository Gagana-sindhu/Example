num = 4
factors=0
for i in range(1, num + 1):
               if num % i==0:
                       factors += 1
if factors > 2:
        print("is not a prime number")
else:
        print("is a prime number")