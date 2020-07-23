#Check Prime Number
number = int(input("Number:"))

if number > 1:
	for i in range(2, number):
		if (number % i) == 0:
			print(f" {number}, is not a prime number")
			print(f"{i} times {number//i} is {number}")
			break
	else:
			print(f"{number}, This is prime")
